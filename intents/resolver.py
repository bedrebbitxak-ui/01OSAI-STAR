def resolve(text: str):
    t = text.strip()

    # MODULE
    if t.startswith("module "):
        return {
            "intent": "MODULE",
            "payload": t[len("module "):].strip()
        }

    # RUN
    if t.startswith("run "):
        return {
            "intent": "RUN",
            "payload": t[4:].strip()
        }

    # HELP
    if t == "help":
        return {"intent": "HELP"}

    # MEM
    if t == "mem":
        return {"intent": "MEMORY"}

    # PING
    if t.lower() in ("hi", "hello", "ping"):
        return {"intent": "PING"}

    # EXIT
    if t in ("exit", "quit"):
        return {"intent": "EXIT"}

    # DEFAULT → ECHO
    return {
        "intent": "ECHO",
        "payload": t
    }
