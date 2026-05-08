# auto_tools.py
# Auto-Tools v1 — исполнитель шагов плана PlannerAgent v3

from core.utils import log


class AutoTools:
    """
    Исполняет шаги плана формата:

    1) Описание шага
       tool: <module|agent|chain|semantic|llm>
       name: <имя или '-'>
       input: <текст>

    PlannerAgent v3 генерирует такие шаги.
    AutoTools v1 — исполняет.
    """

    def __init__(self, shell):
        self.shell = shell

    def execute_plan(self, plan_text: str) -> str:
        """
        Принимает текст плана от PlannerAgent v3.
        Разбирает шаги.
        Исполняет по очереди.
        """

        steps = self._parse_steps(plan_text)
        if not steps:
            return "[auto-tools] no steps parsed"

        results = []

        for step in steps:
            tool = step.get("tool")
            name = step.get("name")
            inp = step.get("input")

            log(f"[auto-tools] executing: tool={tool}, name={name}, input={inp}")

            if tool == "module":
                result = self._run_module(name, inp)
            elif tool == "agent":
                result = self._run_agent(name, inp)
            elif tool == "chain":
                result = self._run_chain(name, inp)
            elif tool == "semantic":
                result = self._run_semantic(inp)
            elif tool == "llm":
                result = self._run_llm(inp)
            else:
                result = f"[auto-tools] unknown tool '{tool}'"

            results.append(result)

        return "\n".join(results)

    # ---------------------------------------------------------
    # INTERNAL EXECUTION
    # ---------------------------------------------------------

    def _run_module(self, name, inp):
        if name not in self.shell.modules:
            return f"[auto-tools] module '{name}' not found"
        return self.shell.modules[name].run("convert", inp)

    def _run_agent(self, name, inp):
        if name not in self.shell.agents:
            return f"[auto-tools] agent '{name}' not found"
        agent = self.shell.agents[name]
        agent.state["shell"] = self.shell
        return agent.step(inp)

    def _run_chain(self, name, inp):
        if name not in self.shell.chains:
            return f"[auto-tools] chain '{name}' not found"
        ctx = {"text": inp}
        result = self.shell.chains[name].run(ctx, self.shell)
        return result.get("text", "")

    def _run_semantic(self, inp):
        return self.shell.semantic.query(inp)

    def _run_llm(self, inp):
        return self.shell.osai.run(inp)

    # ---------------------------------------------------------
    # PARSER
    # ---------------------------------------------------------

    def _parse_steps(self, text: str):
        """
        Парсер плана PlannerAgent v3.
        Ищет блоки вида:

        1) ...
           tool: X
           name: Y
           input: Z
        """

        lines = text.split("\n")
        steps = []
        current = {}

        for line in lines:
            line = line.strip()

            if line.startswith("1)") or line.startswith("2)") or line.startswith("3)") or line.startswith("4)"):
                if current:
                    steps.append(current)
                current = {"desc": line}

            elif line.startswith("tool:"):
                current["tool"] = line.split(":", 1)[1].strip()

            elif line.startswith("name:"):
                current["name"] = line.split(":", 1)[1].strip()

            elif line.startswith("input:"):
                current["input"] = line.split(":", 1)[1].strip()

        if current:
            steps.append(current)

        return steps
