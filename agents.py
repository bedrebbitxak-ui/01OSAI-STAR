# agents.py
from core.utils import log


class BaseAgent:
    def __init__(self, name):
        self.name = name
        self.state = {}

    def step(self, text: str) -> str:
        raise NotImplementedError("Agent must implement step()")


class EchoAgent(BaseAgent):
    def __init__(self):
        super().__init__("echo")

    def step(self, text: str) -> str:
        return f"[echo] {text}"


class MemoryAgent(BaseAgent):
    def __init__(self):
        super().__init__("memory")
        self.state["log"] = []

    def step(self, text: str) -> str:
        self.state["log"].append(text)
        return f"[memory] stored: {text}"


class PlannerAgent(BaseAgent):
    """
    PlannerAgent v4:
      - строит план (как v3)
      - исполняет план (Auto-Tools)
      - анализирует результат
      - улучшает план (Auto-Refine)
      - возвращает улучшенный план + результат
    """

    def __init__(self):
        super().__init__("planner")
        self.state["last_plan"] = None
        self.state["last_refined"] = None
        self.state["last_result"] = None

    def step(self, text: str) -> str:
        shell = self.state.get("shell")
        if shell is None:
            return "[planner.v4] ERROR: shell not attached"

        if not hasattr(shell, "capabilities"):
            return "[planner.v4] ERROR: capabilities not available"

        # ---------------------------------------------------------
        # 1. Построение плана (как v3)
        # ---------------------------------------------------------
        caps = shell.capabilities.list()

        modules = ", ".join(caps["modules"]) if caps["modules"] else "-"
        agents = ", ".join(caps["agents"]) if caps["agents"] else "-"
        chains = ", ".join(caps["chains"]) if caps["chains"] else "-"
        facts_count = len(caps["semantic"])

        prompt = (
            "Ты — планировщик действий внутри системы 01OSAI.\n"
            "Построй план решения задачи.\n\n"
            f"Модули: {modules}\n"
            f"Агенты: {agents}\n"
            f"Цепочки: {chains}\n"
            f"Фактов в памяти: {facts_count}\n\n"
            "Формат плана:\n"
            "1) Описание шага\n"
            "   tool: <module|agent|chain|semantic|llm>\n"
            "   name: <имя или '-'>\n"
            "   input: <данные>\n\n"
            f"Задача: {text}"
        )

        log("[planner.v4] building plan via LLM")
        plan = shell.osai.run(prompt)
        self.state["last_plan"] = plan

        # ---------------------------------------------------------
        # 2. Исполнение плана
        # ---------------------------------------------------------
        log("[planner.v4] executing plan via Auto-Tools")
        result = shell.auto.execute_plan(plan)
        self.state["last_result"] = result

        # ---------------------------------------------------------
        # 3. Улучшение плана (Auto-Refine)
        # ---------------------------------------------------------
        log("[planner.v4] refining plan via Auto-Refine")
        refined = shell.refine.refine_plan(plan, result)
        self.state["last_refined"] = refined

        # ---------------------------------------------------------
        # 4. Возврат результата
        # ---------------------------------------------------------
        return (
            "[planner.v4]\n"
            "=== ORIGINAL PLAN ===\n"
            f"{plan}\n\n"
            "=== EXECUTION RESULT ===\n"
            f"{result}\n\n"
            "=== REFINED PLAN ===\n"
            f"{refined}"
        )
