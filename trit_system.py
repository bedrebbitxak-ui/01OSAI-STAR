# 01OSAI-STAR-TRIT98 — Trit System
# Финальный сборщик: связывает TRIT98 с обычным 01OSAI-STAR

from trit_core import TritCore
from trit_shell import TritShell

class TritSystem:
    def __init__(self):
        self.core = TritCore()
        self.shell = TritShell()

    def trit_cycle(self):
        """
        Запустить полный трит-цикл (маршрутизация + исполнение + снимок).
        """
        return self.core.cycle()

    def trit_auto_cycle(self):
        """
        Запустить автоматический трит-цикл.
        """
        return self.core.auto_cycle()

    def trit_snapshot(self):
        """
        Получить полный снимок тритовой архитектуры.
        """
        return self.core.snapshot()

    def trit_export_binary(self):
        """
        Экспорт тритовой системы в бинарную карту.
        """
        return self.core.export_binary()

    def trit_import_binary(self, binary_map):
        """
        Импорт бинарной карты в тритовую систему.
        """
        self.core.import_binary(binary_map)

    def trit_command(self, command_line):
        """
        Выполнить текстовую трит-команду через TritShell.
        """
        return self.shell.execute(command_line)


if __name__ == "__main__":
    system = TritSystem()

    # Пример базового запуска
    print("=== TRIT CYCLE ===")
    print(system.trit_cycle())

    print("\n=== TRIT AUTO CYCLE ===")
    print(system.trit_auto_cycle())

    print("\n=== TRIT SNAPSHOT ===")
    print(system.trit_snapshot())
