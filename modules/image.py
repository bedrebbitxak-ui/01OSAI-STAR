from modules.base import BaseModule


class ImageModule(BaseModule):
    name = "image"
    commands = ["info", "analyze", "info"]

    def run(self, command: str, args: str):
        command = command.lower()

        if command == "info":
            return f"[image.info] file = {args}"

        if command == "analyze":
            return f"[image.analyze] analyzing {args}..."

        return f"Unknown command '{command}' for module '{self.name}'"

    def info(self):
        return f"ImageModule: commands = {', '.join(self.commands)}"
