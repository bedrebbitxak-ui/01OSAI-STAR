# auto_chains.py
# Auto-Chains v1 — LLM-конструктор цепочек v2

from core.utils import log
from chains_v2 import (
    Chain,
    LLMStep,
    PythonStep,
    SlotSetStep,
    SlotGetStep,
    IfStep,
    ModuleStep,
)


class AutoChains:
    """
    Auto-Chains v1:
      - принимает задачу
      - просит LLM построить структуру цепочки
      - собирает Chain v2 из шагов
      - исполняет её
    """

    def __init__(self, shell):
        self.shell = shell

    def build(self, task: str):
        """
        LLM генерирует структуру цепочки.
        Формат ответа:

        STEP:
          type: llm
          prompt: "..."
        STEP:
          type: module
          name: audio
          command: convert
          args: "{input} {output}"
        STEP:
          type: python
          code: "ctx['x']=1; return ctx"
        """

        prompt = (
            "Ты — конструктор цепочек действий в системе 01OSAI.\n"
            "Построй цепочку шагов для задачи.\n"
            "Формат ответа строго такой:\n\n"
            "STEP:\n"
            "  type: <llm|module|python|slot_set|slot_get>\n"
            "  ... параметры ...\n\n"
            f"Задача: {task}"
        )

        log("[auto-chains] requesting chain structure from LLM")
        answer = self.shell.osai.run(prompt)

        steps = self._parse_steps(answer)
        chain = self._build_chain(steps)

        return chain, answer

    def run(self, task: str):
        chain, structure = self.build(task)
        ctx = {"text": task}
        result = chain.run(ctx, self.shell)
        return result.get("text", ""), structure

    # ---------------------------------------------------------
    # INTERNAL PARSER
    # ---------------------------------------------------------

    def _parse_steps(self, text: str):
        lines = text.split("\n")
        steps = []
        current = {}

        for line in lines:
            line = line.strip()

            if line.startswith("STEP:"):
                if current:
                    steps.append(current)
                current = {}

            elif line.startswith("type:"):
                current["type"] = line.split(":", 1)[1].strip()

            elif line.startswith("prompt:"):
                current["prompt"] = line.split(":", 1)[1].strip()

            elif line.startswith("name:"):
                current["name"] = line.split(":", 1)[1].strip()

            elif line.startswith("command:"):
                current["command"] = line.split(":", 1)[1].strip()

            elif line.startswith("args:"):
                current["args"] = line.split(":", 1)[1].strip()

            elif line.startswith("code:"):
                current["code"] = line.split(":", 1)[1].strip()

            elif line.startswith("slot:"):
                current["slot"] = line.split(":", 1)[1].strip()

            elif line.startswith("value:"):
                current["value"] = line.split(":", 1)[1].strip()

            elif line.startswith("target:"):
                current["target"] = line.split(":", 1)[1].strip()

        if current:
            steps.append(current)

        return steps

    # ---------------------------------------------------------
    # INTERNAL BUILDER
    # ---------------------------------------------------------

    def _build_chain(self, steps):
        chain_steps = []

        for s in steps:
            t = s.get("type")

            if t == "llm":
                chain_steps.append(LLMStep(s["prompt"]))

            elif t == "module":
                chain_steps.append(
                    ModuleStep(
                        s["name"],
                        s["command"],
                        s["args"]
                    )
                )

            elif t == "python":
                code = s["code"]

                def make_func(code_str):
                    def _f(ctx):
                        local = {"ctx": ctx}
                        exec(code_str, {}, local)
                        return local["ctx"]
                    return _f

                chain_steps.append(PythonStep(make_func(code)))

            elif t == "slot_set":
                chain_steps.append(SlotSetStep(s["slot"], s["value"]))

            elif t == "slot_get":
                chain_steps.append(SlotGetStep(s["slot"], s["target"]))

        return Chain(chain_steps)
