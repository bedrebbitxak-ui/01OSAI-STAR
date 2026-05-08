# chains_v2.py
# Chains v2 — LLM‑reasoning цепочки

from core.utils import log


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
# ПРИМЕР ЦЕПОЧКИ v2
# ---------------------------------------------------------

def build_reason_chain():
    return Chain([
        LLMStep("Сформулируй краткое описание задачи: {text}"),
        SlotSetStep("last_summary", "{text}"),
        LLMStep("Теперь сделай план из 3 шагов для: {text}"),
        PythonStep(lambda ctx: {**ctx, "text": ctx["text"].upper()}),
    ])
