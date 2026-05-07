from modules.base import BaseModule


class TextModule(BaseModule):
    name = "text"
    commands = ["generate", "upper", "lower", "info"]

    def run(self, command: str, args: str):
        command = command.lower()

        if command == "generate":
            return f"[text.generate] {args}"

        if command == "upper":
            return args.upper()

        if command == "lower":
            return args.lower()

        if command == "info":
            return self.info()

        return f"Unknown command '{command}' for module '{self.name}'"

    def info(self):
        return f"TextModule: commands = {', '.join(self.commands)}"

