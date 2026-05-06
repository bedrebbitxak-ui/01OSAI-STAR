def safe_exec(code: str):
    """
    Выполняет выражение безопасно.
    Сначала пытается eval.
    Если eval не подходит — выполняет exec.
    """

    # Пустые безопасные окружения
    safe_globals = {"__builtins__": {}}
    safe_locals = {}

    # Попытка eval (например: "2+2")
    try:
        return eval(code, safe_globals, safe_locals)
    except Exception:
        pass

    # Попытка exec (например: "x=10\n_ = x*2")
    try:
        exec(code, safe_globals, safe_locals)
        # Возвращаем значение переменной "_" если оно есть
        return safe_locals.get("_", None)
    except Exception as e:
        return f"SandboxError: {e}"
