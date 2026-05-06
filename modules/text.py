from modules.base import BaseModule

class TextModule(BaseModule):
    name = "text"
    commands = ["generate"]

    def run(self, command, args):
        if command == "generate":
            return f"[TEXT] {args}"
        return f"[text] Unknown command: {command}"
