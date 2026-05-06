from modules.base import BaseModule

class VideoModule(BaseModule):
    name = "video"
    commands = ["info"]

    def run(self, command, args):
        if command == "info":
            return f"[VIDEO] info requested for: {args}"
        return f"[video] Unknown command: {command}"
