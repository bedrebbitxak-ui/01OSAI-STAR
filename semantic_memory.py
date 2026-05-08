# semantic_memory.py
# Semantic Memory v1 — простое семантическое хранилище фактов поверх OSAI-Bridge

from core.utils import log


class SemanticMemory:
    """
    v1:
      - извлекает короткие факты из текста через LLM
      - хранит их в списке
      - умеет отвечать на вопросы на основе этих фактов
    """

    def __init__(self, osai):
        self.osai = osai
        self.facts = []

    def add_fact_from_text(self, text: str) -> str:
        """
        Берёт произвольный текст, просит LLM выделить один факт
        и сохраняет его.
        """
        prompt = (
            "Извлеки один короткий, чёткий факт из текста.\n"
            "Формат: одна строка, без пояснений.\n\n"
            f"Текст: {text}"
        )
        log("[semantic] extract fact")
        fact = self.osai.run(prompt).strip()
        if fact:
            self.facts.append(fact)
            return f"[semantic] stored fact: {fact}"
        else:
            return "[semantic] no fact extracted"

    def add_fact(self, fact: str) -> str:
        """
        Прямое добавление факта.
        """
        self.facts.append(fact.strip())
        return f"[semantic] stored fact: {fact.strip()}"

    def list_facts(self) -> str:
        if not self.facts:
            return "[semantic] no facts"
        return "[semantic] facts:\n" + "\n".join(f"- {f}" for f in self.facts)

    def query(self, question: str) -> str:
        """
        Отвечает на вопрос на основе сохранённых фактов.
        """
        if not self.facts:
            return "[semantic] no facts to answer from"

        context = "\n".join(f"- {f}" for f in self.facts)
        prompt = (
            "Вот набор фактов:\n"
            f"{context}\n\n"
            "Ответь на вопрос, опираясь только на эти факты.\n"
            "Если ответа нет в фактах — скажи, что фактов недостаточно.\n\n"
            f"Вопрос: {question}"
        )
        log("[semantic] query")
        answer = self.osai.run(prompt).strip()
        return f"[semantic.answer] {answer}"
