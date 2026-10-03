# 01OSAI-STAR-TRIT98 — Trit Shell
# Текстовая командная оболочка для управления тритовой архитектурой

from trit_runner import TritRunner
from trit_router import TritRouter
from trit_intents import TritIntents
from trit_topology import Trit

class TritShell:
    def __init__(self):
        self.runner = TritRunner()
        self.router = TritRouter()
        self.intents = TritIntents()

        self.commands = {
            "help": self.cmd_help,
            "snapshot": self.cmd_snapshot,
            "run": self.cmd_run,
            "routes": self.cmd_routes,
            "intent": self.cmd_intent,
            "set": self.cmd_set,
            "active": self.cmd_active,
            "collapsed": self.cmd_collapsed,
            "neutral": self.cmd_neutral
        }

    def cmd_help(self):
        return [
            "help — список команд",
            "snapshot — полный снимок трит-системы",
            "run — выполнить трит-цикл",
            "routes — маршрутизация узлов",
            "intent <name> — применить намерение",
            "set <index> <state> — установить состояние узла",
            "active — узлы в состоянии +1",
            "collapsed — узлы в состоянии -1",
            "neutral — узлы в состоянии 0"
        ]

    def cmd_snapshot(self):
        return self.runner.snapshot()

    def cmd_run(self):
        return self.runner.run()

    def cmd_routes(self):
        return self.router.snapshot()

    def cmd_intent(self, name):
        applied = self.intents.apply_intent(name)
        if applied:
            return f"Intent '{name}' applied."
        return f"Intent '{name}' not found."

    def cmd_set(self, index, state):
        try:
            index = int(index)
            state = int(state)
            if state not in (-1, 0, 1):
                return "State must be -1, 0, or 1."
            self.runner.set_node(index, value=f"manual:{index}", state=state)
            return f"Node {index} set to state {state}."
        except:
            return "Invalid parameters."

    def cmd_active(self):
        return self.router.active_nodes()

    def cmd_collapsed(self):
        return self.router.collapsed_nodes()

    def cmd_neutral(self):
        return self.router.neutral_nodes()

    def execute(self, command_line):
        """
        Выполнение текстовой команды.
        """
        parts = command_line.split()
        if not parts:
            return "Empty command."

        cmd = parts[0]
        args = parts[1:]

        if cmd in self.commands:
            try:
                return self.commands[cmd](*args)
            except TypeError:
                return "Invalid arguments."
        else:
            return f"Unknown command: {cmd}"
