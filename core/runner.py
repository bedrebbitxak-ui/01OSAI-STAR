import time
import traceback
from .sandbox import safe_exec
from .utils import log

class Runner:
    def __init__(self):
        self.alive = True

    def run(self, code: str):
        try:
            log("RUNNER: executing payload")
            result = safe_exec(code)
            return {"ok": True, "result": result}
        except Exception as e:
            log("RUNNER ERROR", traceback.format_exc())
            return {"ok": False, "error": str(e)}

    def loop(self):
        log("RUNNER: loop started")
        while self.alive:
            time.sleep(0.1)
