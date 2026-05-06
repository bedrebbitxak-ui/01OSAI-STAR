def safe_exec(code: str):
    """
    Выполняет выражение безопасно.
    Если это выражение — используем eval.
    Если это блок кода — используем exec.
    """

    # Пустой набор доступных переменных
    safe_globals = {"__builtins__": {}}
    safe_locals = {}

    # Если это выражение (например "2+2")
    try:
        return eval(code, safe_globals, safe_locals)
    except SyntaxError:
        pass

    # Если это блок кода (например "x=2\nx+2")
    try:
        exec(code, safe_globals, safe_locals)
        # Если в блоке был результат — возвращаем его
        return safe_locals.get("_", None)
    except Exception as e:
        raise e
