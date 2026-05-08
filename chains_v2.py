# chains_v2.py
# Chains v2 — LLM‑reasoning цепочки

from core.utils import log
import re


# ---------------------------------------------------------
# БАЗОВЫЙ ШАГ
# ---------------------------------------------------------

class ChainStep:
    def run(self, ctx: dict, shell):
        raise NotImplementedError


# ---------------------------------------------------------
# LLM‑ШАГ
# ---------------------------------------------------------

class LLMStep(ChainStep):
    def __init__(self, prompt):
        self.prompt = prompt

    def run(self, ctx, shell):
        text = self.prompt.format(**ctx)
        log(f"[chain:LLM] → {text}")
        answer = shell.osai.run(text)
        ctx["text"] = answer
        return ctx


# ---------------------------------------------------------
# PYTHON‑ШАГ
# ---------------------------------------------------------

class PythonStep(ChainStep):
    def __init__(self, func):
        self.func = func

    def run(self, ctx, shell):
        ctx = self.func(ctx)
        return ctx


# ---------------------------------------------------------
# SLOT SET
# ---------------------------------------------------------

class SlotSetStep(ChainStep):
    def __init__(self, key, value_expr):
        self.key = key
        self.value_expr = value_expr

    def run(self, ctx, shell):
        value = self.value_expr.format(**ctx)
        shell.memory.set_slot(self.key, value)
        return ctx


# ---------------------------------------------------------
# SLOT GET
# ---------------------------------------------------------

class SlotGetStep(ChainStep):
    def __init__(self, key, target):
        self.key = key
        self.target = target

    def run(self, ctx, shell):
        ctx[self.target] = shell.memory.get_slot(self.key)
        return ctx


# ---------------------------------------------------------
# IF STEP
# ---------------------------------------------------------

class IfStep(ChainStep):
    def __init__(self, condition_key, then_steps, else_steps=None):
        self.condition_key = condition_key
        self.then_steps = then_steps
        self.else_steps = else_steps or []

    def run(self, ctx, shell):
        branch = self.then_steps if ctx.get(self.condition_key) else self.else_steps
        for step in branch:
            ctx = step.run(ctx, shell)
        return ctx


# ---------------------------------------------------------
# MODULE STEP — вызов module.<name>.run(...)
# ---------------------------------------------------------

class ModuleStep(ChainStep):
    def __init__(self, module_name: str, command: str, args_template: str):
        self.module_name = module_name
        self.command = command
        self.args_template = args_template

    def run(self, ctx, shell):
        if self.module_name not in shell.modules:
            ctx["text"] = f"[module:{self.module_name}] not found"
            return ctx

        args = self.args_template.format(**ctx)
        result = shell.modules[self.module_name].run(self.command, args)
        ctx["text"] = result
        return ctx


# ---------------------------------------------------------
# CHAIN
# ---------------------------------------------------------

class Chain:
    def __init__(self, steps):
        self.steps = steps

    def run(self, ctx, shell):
        for step in self.steps:
            ctx = step.run(ctx, shell)
        return ctx


# ---------------------------------------------------------
# ПРИМЕР ЦЕПОЧКИ v2 (reason)
# ---------------------------------------------------------

def build_reason_chain():
    return Chain([
        LLMStep("Сформулируй краткое описание задачи: {text}"),
        SlotSetStep("last_summary", "{text}",
        ),
        LLMStep("Теперь сделай план из 3 шагов для: {text}"),
        PythonStep(lambda ctx: {**ctx, "text": ctx["text"].upper()}),
    ])


# ---------------------------------------------------------
# reason_audio_chain — LLM → парсинг → AudioModule.convert
# ---------------------------------------------------------

def _parse_input_output(ctx: dict) -> dict:
    """
    Ожидает в ctx["text"] ответ вида:
      INPUT=<имя_входного_файла>
      OUTPUT=<имя_выходного_файла>
    и кладёт:
      ctx["input_file"], ctx["output_file"]
    """
    text = ctx.get("text", "")
    input_file = None
    output_file = None

    m_in = re.search(r"INPUT\s*=\s*(.+)", text)
    m_out = re.search(r"OUTPUT\s*=\s*(.+)", text)

    if m_in:
        input_file = m_in.group(1).strip()
    if m_out:
        output_file = m_out.group(1).strip()

    ctx["input_file"] = input_file
    ctx["output_file"] = output_file

    if not input_file or not output_file:
        ctx["text"] = "[reason_audio] parse error: expected INPUT=... and OUTPUT=..."
    else:
        ctx["text"] = f"[reason_audio] parsed: {input_file} → {output_file}"

    return ctx


def build_reason_audio_chain():
    """
    Пример:
      chain run reason_audio "конвертируй voice.wma в voice.ogg"
    """
    return Chain([
        LLMStep(
            "Из запроса определи имена входного и выходного файлов для аудио-конвертации.\n"
            "Ответь строго в формате:\n"
            "INPUT=<имя_входного_файла>\n"
            "OUTPUT=<имя_выходного_файла>\n\n"
            "Запрос: {text}"
        ),
        PythonStep(_parse_input_output),
        ModuleStep("audio", "convert", "{input_file} {output_file}"),
    ])
