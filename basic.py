from core.utils import log
from runner_01 import Runner01   # ← добавлено
runner = Runner01()              # ← добавлено


def intent_help():
    return (
        "Commands:\n"
        "  help — show this help\n"
        "  mem — show last memory entries\n"
        "  run <code> — execute python code in sandbox\n"
        "  module <name> <command> [args] — call module\n"
        "  exit — quit shell\n"
    )


def intent_echo(text):
    return f"Echo: {text}"


def intent_run(code):            # ← обновлено
    res = runner.run(code)
    if res["ok"]:
        return f"RUN: {res['result']}"
    else:
        return f"RUN error: {res['error']}"


def intent_memory(memory):
    last = memory.last(5)
    return "Last memory:\n" + "\n".join(last)


def intent_module(modules, payload):
    """
    payload: "text generate hello world"
    """
    parts = payload.split(" ", 2)

    if len(parts) < 2:
        return "Usage: module <name> <command> [args]"

    name = parts[0]
    command = parts[1]
    args = parts[2] if len(parts) > 2 else ""

    if name not in modules:
        return f"Module '{name}' not found"

    try:
        result = modules[name].run(command, args)
        return result
    except Exception as e:
        return f"ModuleError: {e}"
