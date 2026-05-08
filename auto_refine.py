# auto_refine.py
# Auto-Refine v1 — улучшение планов и цепочек через LLM

from core.utils import log


class AutoRefine:
    """
    Auto-Refine v1:
      - принимает план или структуру цепочки
      - принимает результаты выполнения
      - просит LLM улучшить план/цепочку
      - возвращает улучшенную версию
    """

    def __init__(self, shell):
        self.shell = shell

    def refine_plan(self, original_plan: str, execution_result: str) -> str:
        """
        Улучшает план PlannerAgent v3.
        """

        prompt = (
            "Ты — оптимизатор планов в системе 01OSAI.\n"
            "Вот исходный план:\n"
            f"{original_plan}\n\n"
            "Вот результаты выполнения:\n"
            f"{execution_result}\n\n"
            "Улучшай план:\n"
            "- убери лишние шаги\n"
            "- исправь ошибки\n"
            "- уточни входы\n"
            "- используй доступные возможности системы\n"
            "- сохрани формат PlannerAgent v3\n\n"
            "Верни только улучшенный план."
        )

        log("[auto-refine] refining plan")
        return self.shell.osai.run(prompt)

    def refine_chain(self, structure: str, execution_result: str) -> str:
        """
        Улучшает структуру цепочки Auto-Chains v1.
        """

        prompt = (
            "Ты — оптимизатор цепочек действий в системе 01OSAI.\n"
            "Вот исходная структура цепочки:\n"
            f"{structure}\n\n"
            "Вот результаты выполнения:\n"
            f"{execution_result}\n\n"
            "Улучшай цепочку:\n"
            "- убери лишние шаги\n"
            "- исправь ошибки\n"
            "- уточни параметры\n"
            "- используй доступные инструменты\n"
            "- сохрани формат Auto-Chains v1 (STEP: ...)\n\n"
            "Верни только улучшенную структуру."
        )

        log("[auto-refine] refining chain")
        return self.shell.osai.run(prompt)
