from core.utils import log


class BaseAgent:
    """
    Базовый агент.
    У каждого агента есть:
      - имя
      - состояние (dict)
      - метод step(input) → output
    """

    def __init__(self, name):
        self.name = name
        self.state = {}

    def step(self, text: str) -> str:
        raise NotImplementedError("Agent must implement step()")


class EchoAgent(BaseAgent):
    """
    Простейший агент.
    Просто повторяет вход.
    """

    def __init__(self):
        super().__init__("echo")

    def step(self, text: str) -> str:
        return f"[echo] {text}"


class MemoryAgent(BaseAgent):
    """
    Агент, который запоминает всё, что ему говорят.
    """

    def __init__(self):
        super().__init__("memory")
        self.state["log"] = []

    def step(self, text: str) -> str:
        self.state["log"].append(text)
        return f"[memory] stored: {text}"


class PlannerAgent(BaseAgent):
    """
    Агент-планировщик.
    Простейшая версия: разбивает задачу на шаги.
    """

    def __init__(self):
        super().__init__("planner")

    def step(self, text: str) -> str:
        steps = text.split(".")
        numbered = [f"{i+1}. {s.strip()}" for i, s in enumerate(steps) if s.strip()]
        return "[planner]\n" + "\n".join(numbered)
