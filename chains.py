# chains.py
# Базовая система цепочек (Chains v1)
# Здесь будут жить последовательные процессы, которые выполняют шаги один за другим.

from core.utils import log


class Chain:
    """
    Базовая цепочка.
    Цепочка — это список шагов (callables), которые выполняются последовательно.
    Каждый шаг принимает (context) и возвращает обновлённый context.
    """

    def __init__(self, name):
        self.name = name
        self.steps = []

    def add(self, step):
        """Добавить шаг в цепочку."""
        self.steps.append(step)

    def run(self, context):
        """Запустить цепочку."""
        log(f"[CHAIN:{self.name}] start")

        for i, step in enumerate(self.steps):
            log(f"[CHAIN:{self.name}] step {i+1}/{len(self.steps)} → {step.__name__}")
            context = step(context)

        log(f"[CHAIN:{self.name}] done")
        return context


# Пример простой цепочки (для теста)
def step_upper(ctx):
    ctx["text"] = ctx["text"].upper()
    return ctx


def step_reverse(ctx):
    ctx["text"] = ctx["text"][::-1]
    return ctx


def build_test_chain():
    c = Chain("test")
    c.add(step_upper)
    c.add(step_reverse)
    return c
