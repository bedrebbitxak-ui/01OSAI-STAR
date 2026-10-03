# 01OSAI-STAR-TRIT98 — Trit System Shell
# Системная оболочка TRIT98: интерфейс взаимодействия всех системных слоёв

from trit_system_sync import TritSystemSync
from trit_system_router import TritSystemRouter
from trit_system_map import TritSystemMap

class TritSystemShell:
    def __init__(self):
        self.sync = TritSystemSync()
        self.router = TritSystemRouter()
        self.map = TritSystemMap()

        self.history = []

    def execute(self, command):
        """
        Выполнение системной команды:
        - sync
        - route:<target>
        - map
        """
        if command == "sync":
            result = self.sync.full_sync()
        elif command.startswith("route:"):
            target = command.split(":", 1)[1]
            result = self.router.route(target)
        elif command == "map":
            result = self.map.snapshot()
        else:
            result = {"error": "unknown command"}

        self.history.append(result)
        return result

    def snapshot(self):
        return {
            "last": self.history[-1] if self.history else None,
            "history_length": len(self.history)
        }


if __name__ == "__main__":
    tsshell = TritSystemShell()
    print("=== TRIT SYSTEM SHELL EXECUTE ===")
    print(tsshell.execute("sync"))
