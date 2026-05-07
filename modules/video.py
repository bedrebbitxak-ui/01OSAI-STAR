from modules.base import BaseModule


class VideoModule(BaseModule):
    name = "video"
    commands = ["info", "analyze", "play"]

    def run(self, command: str, args: str):
        command = command.lower()

        if command == "info":
            return f"[video.info] file = {args}"

        if command == "analyze":
            return f"[video.analyze] analyzing {args}..."

        if command == "play":
            return f"[video.play] playing video: {args}"

        return f"Unknown command '{command}' for module '{self.name}'"

    def info(self):
        return f"VideoModule: commands = {', '.join(self.commands)}"
