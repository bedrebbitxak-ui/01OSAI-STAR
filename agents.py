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


# 🟩 PlannerAgent v2 — LLM‑планировщик
class PlannerAgent(BaseAgent):
    """
    Агент‑планировщик v2.
    Использует OSAI‑Bridge (LLM) для генерации плана.
    """

    def __init__(self):
        super().__init__("planner")
        self.state["last_plan"] = None

    def step(self, text: str) -> str:
        """
        Формирует структурированный план через LLM.
        """

        # shell передаётся в intent_agent → shell.active_agent.step(payload)
        # поэтому shell доступен через self.state["shell"]
        shell = self.state.get("shell")
        if shell is None:
            return "[planner] ERROR: shell not attached"

        # Формируем запрос к LLM
        prompt = (
            "Сформируй чёткий, структурированный план действий.\n"
            "Формат:\n"
            "1. ...\n"
            "2. ...\n"
            "3. ...\n\n"
            f"Задача: {text}"
        )

        log("[planner] sending to LLM")
        answer = shell.osai.run(prompt)

        # сохраняем план
        self.state["last_plan"] = answer

        return f"[planner]\n{answer}"
