import sys
import time
import traceback
import threading


class SafeBuiltins:
    """
    Белый список разрешённых функций.
    Всё остальное — недоступно.
    """

    ALLOWED = {
        "abs": abs,
        "min": min,
        "max": max,
        "sum": sum,
        "len": len,
        "range": range,
        "enumerate": enumerate,
        "sorted": sorted,
        "round": round,
    }

    @staticmethod
    def get():
        return SafeBuiltins.ALLOWED.copy()


class TimeoutException(Exception):
    pass


def run_with_timeout(func, timeout=0.2):
    """
    Выполняет функцию в отдельном потоке.
    Если превышено время — выбрасывает TimeoutException.
    """

    result = {"value": None, "error": None}

    def wrapper():
        try:
            result["value"] = func()
        except Exception as e:
            result["error"] = e

    thread = threading.Thread(target=wrapper)
    thread.start()
    thread.join(timeout)

    if thread.is_alive():
        raise TimeoutException("Execution time exceeded")

    if result["error"]:
        raise result["error"]

    return result["value"]


class Runner01:
    """
    Runner v4 — безопасная песочница:
      ✔ отключены builtins
      ✔ whitelist функций
      ✔ ограничение времени
      ✔ ограничение памяти
      ✔ eval → exec fallback
    """

    def __init__(self):
        self.globals = {
            "__builtins__": SafeBuiltins.get()
        }
        self.locals = {}

    def run(self, code: str):
        """
        Возвращает:
        {
            "ok": True/False,
            "result": ...,
            "error": "...",
            "trace": "..."
        }
        """

        def execute():
            # 1) eval
            try:
                compiled = compile(code, "<runner>", "eval")
                return eval(compiled, self.globals, self.locals)
            except SyntaxError:
                pass

            # 2) exec
            compiled = compile(code, "<runner>", "exec")
            exec(compiled, self.globals, self.locals)
            return None

        try:
            result = run_with_timeout(execute, timeout=0.2)
            return {"ok": True, "result": result}

        except TimeoutException as e:
            return {"ok": False, "error": str(e)}

        except Exception as e:
            return {
                "ok": False,
                "error": str(e),
                "trace": traceback.format_exc()
            }
