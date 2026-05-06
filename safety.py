from core.utils import log

FORBIDDEN = [
    "import os",
    "import sys",
    "open(",
    "exec(",
    "eval(",
    "__import__",
    "subprocess",
    "shutil",
    "socket",
]

class Safety:
    def __init__(self):
        log("SAFETY: initialized")

    def check(self, text: str) -> bool:
        """
        Простейший фильтр опасных конструкций.
        """
        lowered = text.lower()
        for bad in FORBIDDEN:
            if bad in lowered:
                log(f"SAFETY BLOCKED: {bad}")
                return False
        return True
