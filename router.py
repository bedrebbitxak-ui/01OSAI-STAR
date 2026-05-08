# router.py
# Auto‑Routing v1
# Определяет, куда направить текст пользователя:
#  - агентам
#  - модулям
#  - цепочкам
#  - или в echo

from core.utils import log


class AutoRouter:
    """
    Автоматический роутер.
    Получает текст и решает, куда его отправить.
    """

    def __init__(self, shell):
        self.shell = shell

    def route(self, text: str):
        """
        Возвращает:
        {
            "intent": "...",
            "payload": "..."
        }
        """

        t = text.strip().lower()

        # 1. Если пользователь явно указал команду — не трогаем
        if t.startswith(("agent ", "module ", "chain ", "run ", "mem", "help", "exit", "quit")):
            return None  # пусть resolver решает

        # 2. Если активен агент — отправляем туда
        if self.shell.active_agent is not None:
            log("[router] → active agent")
            return {"intent": "AGENT", "payload": text}

        # 3. Если текст похож на задачу — отправляем в planner
        if any(word in t for word in ["сделай", "нужно", "надо", "план", "задача"]):
            if "planner" in self.shell.agents:
                log("[router] → planner agent")
                return {"intent": "AGENT", "payload": f"use planner\n{text}"}

        # 4. Если текст похож на трансформацию строки — цепочка
        if any(word in t for word in ["разверни", "переверни", "uppercase", "reverse"]):
            if "test" in self.shell.chains:
                log("[router] → test chain")
                return {"intent": "CHAIN", "payload": f"run test {text}"}

        # 5. Если текст похож на генерацию — модуль text
        if any(word in t for word in ["напиши", "сгенерируй", "generate"]):
            if "text" in self.shell.modules:
                log("[router] → text module")
                return {"intent": "MODULE", "payload": f"text generate {text}"}

        # 6. По умолчанию — echo
        log("[router] → echo")
        return {"intent": "ECHO", "payload": text}
