# osai_bridge.py
# OSAI‑Bridge v1 — мост между 01OSAI и LLM

from core.utils import log


class OSAIBridge:
    """
    Мост между 01OSAI и внешним LLM.
    Формирует контекст, отправляет запрос, получает ответ.
    """

    def __init__(self, memory):
        self.memory = memory

    def build_context(self, user_text: str):
        """
        Формирует полный контекст:
        - последние сообщения (STM)
        - факты (LTM)
        - слоты (контекстные переменные)
        """
        return {
            "input": user_text,
            "stm": self.memory.last(10),
            "ltm": self.memory.ltm,
            "slots": self.memory.slots,
        }

    def call_llm(self, context: dict):
        """
        Здесь будет реальный вызов LLM.
        Пока — заглушка, чтобы система работала.
        """
        text = context["input"]
        log(f"[OSAI‑Bridge] LLM request: {text}")

        # Заглушка: просто отвечает "LLM: <text>"
        return f"LLM: {text}"

    def run(self, user_text: str):
        """
        Полный цикл:
        1. собрать контекст
        2. вызвать LLM
        3. вернуть ответ
        """
        ctx = self.build_context(user_text)
        answer = self.call_llm(ctx)
        return answer
