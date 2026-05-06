from core.utils import log

class Shell01:
    def __init__(self, osai):
        self.osai = osai
        log("SHELL_01: initialized")

    def process(self, text: str) -> str:
        """
        Простейший обработчик текстовых команд.
        """
        t = text.strip().lower()

        # базовые команды
        if t in ["hi", "hello", "привет"]:
            return "01OSAI-STAR online."

        if t == "help":
            return (
                "Commands:\n"
                "  hi / hello — ping\n"
                "  mem — show last memory entries\n"
                "  run <code> — execute python code in sandbox\n"
            )

        if t == "mem":
            last = self.osai.memory.last(5)
            return "Last memory:\n" + "\n".join(last)

        # выполнение кода
        if t.startswith("run "):
            code = text[4:]
            result = self.osai.execute(code)
            return str(result)

        # fallback
        return f"Echo: {text}"
