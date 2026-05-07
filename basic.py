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
        "  agent ... — interact with agents\n"
        "  chain ... — run chains\n"
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


# 🟦 ← ДОБАВЛЕНО: intent_agent
def intent_agent(shell, payload):
    """
    Команды:
      agent list
      agent use <name>
      agent <text>  — отправить текст активному агенту
    """

    parts = payload.split(" ", 1)

    # agent list
    if parts[0] == "list":
        return "Agents:\n" + "\n".join(shell.agents.keys())

    # agent use <name>
    if parts[0] == "use":
        if len(parts) < 2:
            return "Usage: agent use <name>"
        name = parts[1]
        if name not in shell.agents:
            return f"Agent '{name}' not found"
        shell.active_agent = shell.agents[name]
        return f"Active agent: {name}"

    # agent <text> — отправить текст активному агенту
    if shell.active_agent is None:
        return "No active agent. Use: agent use <name>"

    return shell.active_agent.step(payload)


# 🟩 ← ДОБАВЛЕНО: intent_chain
def intent_chain(shell, payload):
    """
    Команды:
      chain list
      chain run <name> <text>
    """

    parts = payload.split(" ", 1)

    # chain list
    if parts[0] == "list":
        return "Chains:\n" + "\n".join(shell.chains.keys())

    # chain run <name> <text>
    if parts[0] == "run":
        if len(parts) < 2:
            return "Usage: chain run <name> <text>"

        # Разделяем: <name> <text>
        try:
            name, text = parts[1].split(" ", 1)
        except ValueError:
            return "Usage: chain run <name> <text>"

        if name not in shell.chains:
            return f"Chain '{name}' not found"

        ctx = {"text": text}
        result = shell.chains[name].run(ctx)

        return f"[chain:{name}] {result['text']}"

    return "Unknown chain command"
