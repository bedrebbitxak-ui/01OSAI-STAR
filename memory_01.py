# memory.py
# Memory v2 — многослойная память для 01OSAI
# STM (короткая память), LTM (долгая память), Slots (контекстные переменные)

import json
from core.utils import log

MEMORY_FILE = "01_memory.json"


class MemoryV2:
    def __init__(self):
        self.stm = []          # short‑term memory (последние сообщения)
        self.ltm = {}          # long‑term memory (факты, знания)
        self.slots = {}        # контекстные переменные
        self.load()

    # ---------------------------------------------------------
    # ЗАГРУЗКА / СОХРАНЕНИЕ
    # ---------------------------------------------------------

    def load(self):
        try:
            with open(MEMORY_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)

            self.stm = data.get("stm", [])
            self.ltm = data.get("ltm", {})
            self.slots = data.get("slots", {})

            log("MEMORY v2: loaded")

        except Exception:
            log("MEMORY v2: starting new memory file")
            self.save()

    def save(self):
        try:
            data = {
                "stm": self.stm,
                "ltm": self.ltm,
                "slots": self.slots,
            }
            with open(MEMORY_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

            log("MEMORY v2: saved")

        except Exception as e:
            log(f"MEMORY v2 ERROR: {e}")

    # ---------------------------------------------------------
    # STM — короткая память
    # ---------------------------------------------------------

    def store(self, item: str):
        """Сохраняет строку в STM."""
        self.stm.append(item)
        if len(self.stm) > 50:  # ограничение размера
            self.stm = self.stm[-50:]
        self.save()

    def last(self, n=5):
        """Возвращает последние n элементов STM."""
        return self.stm[-n:]

    # ---------------------------------------------------------
    # LTM — долговременная память
    # ---------------------------------------------------------

    def remember(self, key: str, value):
        """Запомнить факт."""
        self.ltm[key] = value
        self.save()

    def recall(self, key: str):
        """Вспомнить факт."""
        return self.ltm.get(key)

    def forget(self, key: str):
        """Удалить факт."""
        if key in self.ltm:
            del self.ltm[key]
            self.save()

    # ---------------------------------------------------------
    # SLOTS — контекстные переменные
    # ---------------------------------------------------------

    def set_slot(self, key: str, value):
        """Установить контекстную переменную."""
        self.slots[key] = value
        self.save()

    def get_slot(self, key: str):
        """Получить контекстную переменную."""
        return self.slots.get(key)

    def clear_slot(self, key: str):
        """Удалить слот."""
        if key in self.slots:
            del self.slots[key]
            self.save()
