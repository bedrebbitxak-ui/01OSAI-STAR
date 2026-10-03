# 01OSAI-STAR-TRIT98 — Trit Hub
# Центральный узел связи TRIT98 ↔ 01OSAI-STAR ↔ внешние модули

from trit_system import TritSystem

class TritHub:
    def __init__(self):
        # Тритовая система
        self.trit = TritSystem()

        # Буфер входных данных
        self.inbox = []

        # Буфер выходных данных
        self.outbox = []

    def push_input(self, data):
        """
        Добавить входные данные в тритовый буфер.
        """
        self.inbox.append(data)
        return f"Input received: {data}"

    def pull_output(self):
        """
        Получить выходные данные из тритового буфера.
        """
        if not self.outbox:
            return "Outbox empty."
        return self.outbox.pop(0)

    def process(self):
        """
        Обработка входных данных через тритовую систему.
        """
        if not self.inbox:
            return "No input."

        data = self.inbox.pop(0)

        # Простейшая логика:
        # если данные содержат слово "auto" → авто-цикл
        # иначе → обычный трит-цикл
        if "auto" in str(data).lower():
            result = self.trit.trit_auto_cycle()
        else:
            result = self.trit.trit_cycle()

        self.outbox.append(result)
        return "Processed."

    def command(self, cmd):
        """
        Выполнить трит-команду через TritSystem.
        """
        result = self.trit.trit_command(cmd)
        self.outbox.append(result)
        return f"Command executed: {cmd}"

    def export_binary(self):
        """
        Экспорт тритовой системы в бинарную карту.
        """
        binary_map = self.trit.trit_export_binary()
        self.outbox.append(binary_map)
        return "Binary map exported."

    def import_binary(self, binary_map):
        """
        Импорт бинарной карты в тритовую систему.
        """
        self.trit.trit_import_binary(binary_map)
        return "Binary map imported."

    def snapshot(self):
        """
        Полный снимок TRIT98 через хаб.
        """
        snap = self.trit.trit_snapshot()
        self.outbox.append(snap)
        return snap


if __name__ == "__main__":
    hub = TritHub()

    print("=== HUB START ===")
    print(hub.snapshot())

    hub.push_input("auto")
    hub.process()
    print(hub.pull_output())
