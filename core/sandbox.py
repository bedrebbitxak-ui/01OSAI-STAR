import traceback

SAFE_GLOBALS = {
    "__builtins__": {
        "print": print,
        "len": len,
        "range": range,
        "str": str,
        "int": int,
        "float": float,
        "bool": bool,
        "dict": dict,
        "list": list,
        "set": set,
        "tuple": tuple,
        "Exception": Exception,
    }
}

def safe_exec(code: str):
    """
    Выполняет код в безопасной песочнице.
    Возвращает результат последнего выражения.
    """
    try:
        local_env = {}
        exec(code, SAFE_GLOBALS, local_env)
        return local_env.get("result", None)
    except Exception as e:
        return f"SandboxError: {e}\n{traceback.format_exc()}"
