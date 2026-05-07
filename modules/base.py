class BaseModule:
    """
    Базовый класс для всех модулей 01OSAI-STAR.
    Каждый модуль должен определить:
      - name (str)
      - commands (list[str])
      - run(command, args)
      - info()
    """

    name = "base"
    commands = []

    def run(self, command: str, args: str):
        raise NotImplementedError("Module must implement run()")

    def info(self):
        return f"Module '{self.name}' with commands: {', '.join(self.commands)}"
