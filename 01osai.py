from core.runner import Runner
from core.utils import log
from module_loader import ModuleLoader
from memory_01 import Memory01
from safety import Safety
from shell_01 import Shell01

class OSAI:
    def __init__(self):
        log("01OSAI: initializing system")

        self.runner = Runner()
        self.loader = ModuleLoader()
        self.memory = Memory01()
        self.safety = Safety()
        self.shell = Shell01(self)

        log("01OSAI: loading modules")
        self.loader.load_all()

        log("01OSAI: system ready")

    def execute(self, code: str):
        """
        Выполняет код через песочницу и runner.
        """
        if not self.safety.check(code):
            return {"ok": False, "error": "Blocked by safety module"}

        return self.runner.run(code)

    def ask(self, text: str):
        """
        Основной интерфейс для текстовых запросов.
        """
        log(f"01OSAI: input → {text}")

        # память
        self.memory.store(text)

        # shell отвечает
        response = self.shell.process(text)

        # память
        self.memory.store(response)

        return response


if __name__ == "__main__":
    osai = OSAI()
    log("01OSAI: interactive shell started")

    while True:
        user = input(">>> ")
        if user.lower() in ["exit", "quit"]:
            break
        print(osai.ask(user))
