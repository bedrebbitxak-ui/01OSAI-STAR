# runner_01.py
import traceback

class Runner01:
    def __init__(self):
        self.globals = {}
        self.locals = {}

    def run(self, code: str):
        try:
            compiled = compile(code, "<runner>", "eval")
            result = eval(compiled, self.globals, self.locals)
            return {"ok": True, "result": result}
        except SyntaxError:
            try:
                compiled = compile(code, "<runner>", "exec")
                exec(compiled, self.globals, self.locals)
                return {"ok": True, "result": None}
            except Exception as e:
                return {"ok": False, "error": str(e), "trace": traceback.format_exc()}
        except Exception as e:
            return {"ok": False, "error": str(e), "trace": traceback.format_exc()}
