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
    PlannerAgent v3.
    Планировщик, который строит план, опираясь на Capabilities v1:
      - semantic memory
      - modules (tools)
      - agents
      - chains
      - llm
    """

    def __init__(self):
        super().__init__("planner")
        self.state["last_plan"] = None

    def step(self, text: str) -> str:
        shell = self.state.get("shell")
        if shell is None:
            return "[planner.v3] ERROR: shell not attached"

        if not hasattr(shell, "capabilities"):
            return "[planner.v3] ERROR: capabilities not available"

        caps = shell.capabilities.list()

        modules = ", ".join(caps["modules"]) if caps["modules"] else "-"
        agents = ", ".join(caps["agents"]) if caps["agents"] else "-"
        chains = ", ".join(caps["chains"]) if caps["chains"] else "-"
        facts_count = len(caps["semantic"])

        prompt = (
            "Ты — планировщик действий внутри локальной системы 01OSAI.\n"
            "У тебя есть следующие возможности:\n"
            f"- Модули (tools): {modules}\n"
            f"- Агенты: {agents}\n"
            f"- Цепочки (chains): {chains}\n"
            f"- Семантическая память: {facts_count} фактов\n"
            "- LLM (OSAI-Bridge): прямые ответы и рассуждения\n\n"
            "Сформируй план решения задачи, используя эти возможности.\n"
            "Формат плана:\n"
            "1) Краткое описание шага\n"
            "   tool: <module|agent|chain|semantic|llm>\n"
            "   name: <имя модуля/агента/цепочки или '-'>\n"
            "   input: <что подать на вход>\n\n"
            f"Задача: {text}"
        )

        log("[planner.v3] building plan via LLM")
        answer = shell.osai.run(prompt)

        self.state["last_plan"] = answer

        return "[planner.v3]\n" + answer
