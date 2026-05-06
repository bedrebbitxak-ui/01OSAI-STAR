from modules.base import BaseModule

class ImageModule(BaseModule):
    name = "image"
    commands = ["info"]

    def run(self, command, args):
        if command == "info":
            return f"[IMAGE] info requested for: {args}"
        return f"[image] Unknown command: {command}"
