class BaseModule:
    """
    Базовый интерфейс для всех модулей 01OSAI-STAR.
    Каждый модуль обязан определить:
      - name: имя модуля
      - commands: список доступных команд
      - run(command, args): обработка команды
      - info(): описание модуля
    """

    name = "base"
    commands = []

    def run(self, command, args):
        raise NotImplementedError("Module must implement run()")

    def info(self):
        return {
            "name": self.name,
            "commands": self.commands,
            "description": "No description provided"
        }
