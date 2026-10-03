# 01OSAI-STAR-TRIT98 — Trit System Entry
# Точка входа TRIT98: запуск всей системы

from trit_system_shell import TritSystemShell

class TritSystemEntry:
    def __init__(self):
        self.shell = TritSystemShell()
        self.history = []

    def start(self):
        """
        Запуск TRIT98:
        1) системная синхронизация
        2) построение карты
        """
        sync_snap = self.shell.execute("sync")
        map_snap = self.shell.execute("map")

        entry_snapshot = {
            "sync": sync_snap,
            "map": map_snap
        }

        self.history.append(entry_snapshot)
        return entry_snapshot

    def snapshot(self):
        return {
            "last": self.history[-1] if self.history else None,
            "history_length": len(self.history)
        }


if __name__ == "__main__":
    tse = TritSystemEntry()
    print("=== TRIT SYSTEM ENTRY START ===")
    print(tse.start())
