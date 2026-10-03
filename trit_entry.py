# 01OSAI-STAR-TRIT98 — Trit Entry
# Главная входная точка тритовой архитектуры TRIT98

from trit_system import TritSystem

class TritEntry:
    def __init__(self):
        self.system = TritSystem()

    def start(self):
        """
        Запуск тритовой системы.
        """
        return {
            "status": "TRIT98 online",
            "snapshot": self.system.trit_snapshot()
        }

    def cycle(self):
        """
        Запуск обычного трит-цикла.
        """
        return self.system.trit_cycle()

    def auto(self):
        """
        Запуск автоматического трит-цикла.
        """
        return self.system.trit_auto_cycle()

    def command(self, cmd):
        """
        Выполнение трит-команды.
        """
        return self.system.trit_command(cmd)

    def export_binary(self):
        """
        Экспорт тритовой системы в бинарную карту.
        """
        return self.system.trit_export_binary()

    def import_binary(self, binary_map):
        """
        Импорт бинарной карты в тритовую систему.
        """
        return self.system.trit_import_binary(binary_map)


if __name__ == "__main__":
    entry = TritEntry()
    print(entry.start())
