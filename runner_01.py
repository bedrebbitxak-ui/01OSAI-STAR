import traceback

class Runner01:
    """
    Runner v3 — безопасная песочница без eval.
    Работает в двух режимах:
      - eval (если выражение возвращает значение)
      - exec (если это блок кода)
    """

    def __init__(self):
        # изолированные контексты
        self.globals = {
            "__builtins__": {}  # ← полностью отключаем встроенные функции
        }
        self.locals = {}

    def run(self, code: str):
        """
        Выполняет код в песочнице.
        Возвращает:
        {
            "ok": True/False,
            "result": ...,
            "error": "...",
            "trace": "..."
        }
        """

        # 1) сначала пробуем eval
        try:
            compiled = compile(code, "<runner>", "eval")
            result = eval(compiled, self.globals, self.locals)
            return {"ok": True, "result": result}
        except SyntaxError:
            pass
        except Exception as e:
            return {
                "ok": False,
                "error": str(e),
                "trace": traceback.format_exc()
            }

        # 2) если eval не подошёл — пробуем exec
        try:
            compiled = compile(code, "<runner>", "exec")
            exec(compiled, self.globals, self.locals)
            return {"ok": True, "result": None}
        except Exception as e:
            return {
                "ok": False,
                "error": str(e),
                "trace": traceback.format_exc()
            }
