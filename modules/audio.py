from modules.base import BaseModule

class AudioModule(BaseModule):
    name = "audio"
    commands = ["play"]

    def run(self, command, args):
        if command == "play":
            return f"[AUDIO] playing: {args}"
        return f"[audio] Unknown command: {command}"
