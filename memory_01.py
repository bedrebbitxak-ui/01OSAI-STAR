import json
from core.utils import log

MEMORY_FILE = "01_memory.json"

class Memory01:
    def __init__(self):
        self.data = []
        self.load()

    def load(self):
        try:
            with open(MEMORY_FILE, "r", encoding="utf-8") as f:
                self.data = json.load(f)
            log("MEMORY: loaded")
        except Exception:
            log("MEMORY: starting new memory file")
            self.data = []
            self.save()

    def save(self):
        try:
            with open(MEMORY_FILE, "w", encoding="utf-8") as f:
                json.dump(self.data, f, ensure_ascii=False, indent=2)
            log("MEMORY: saved")
        except Exception as e:
            log("MEMORY ERROR:", e)

    def store(self, item: str):
        """
        Сохраняет строку в память.
        """
        self.data.append(item)
        self.save()

    def last(self, n=1):
        """
        Возвращает последние n элементов.
        """
        return self.data[-n:]
