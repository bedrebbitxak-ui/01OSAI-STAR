def resolve(text: str):
    """
    Простейший резолвер интентов.
    Возвращает словарь:
    {
        "intent": "...",
        "payload": "..."
    }
    """

    t = text.strip()

    # EXIT
    if t.lower() in ["exit", "quit"]:
        return {"intent": "EXIT", "payload": ""}

    # HELP
    if t.lower() == "help":
        return {"intent": "HELP", "payload": ""}

    # MEMORY
    if t.lower() == "mem":
        return {"intent": "MEMORY", "payload": ""}

    # RUN
    if t.lower().startswith("run "):
        return {"intent": "RUN", "payload": t[4:]}

    # MODULE
    if t.lower().startswith("module "):
        return {"intent": "MODULE", "payload": t[7:].strip()}

    # PING
    if t.lower() in ["ping", "hi", "hello", "привет"]:
        return {"intent": "PING", "payload": ""}

    # AGENT  ← ДОБАВЛЕНО
    if t.lower().startswith("agent "):
        return {"intent": "AGENT", "payload": t[6:].strip()}

    # DEFAULT → ECHO
    return {"intent": "ECHO", "payload": t}
