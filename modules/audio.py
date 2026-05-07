from modules.base import BaseModule


class AudioModule(BaseModule):
    name = "audio"
    commands = ["play", "info"]

    def run(self, command: str, args: str):
        command = command.lower()

        if command == "play":
            return f"[audio.play] playing sound: {args}"

        if command == "info":
            return self.info()

        return f"Unknown command '{command}' for module '{self.name}'"

    def info(self):
        return f"AudioModule: commands = {', '.join(self.commands)}"
