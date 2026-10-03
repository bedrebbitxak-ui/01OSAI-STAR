# 01OSAI-STAR-TRIT98 — Trit System Log
# Логирование системных событий TRIT98

from datetime import datetime

class TritSystemLog:
    def __init__(self):
        self.entries = []

    def write(self, source, message, level="INFO"):
        entry = {
            "time": datetime.utcnow().isoformat(),
            "source": source,
            "level": level,
            "message": message
        }
        self.entries.append(entry)
        return entry

    def snapshot(self):
        return {
            "count": len(self.entries),
            "last": self.entries[-1] if self.entries else None
        }


if __name__ == "__main__":
    tsl = TritSystemLog()
    print("=== TRIT SYSTEM LOG TEST ===")
    print(tsl.write("system", "TRIT98 log started"))
