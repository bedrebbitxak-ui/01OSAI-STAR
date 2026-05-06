def resolve(text: str):
    t = text.strip().lower()

    if t in ("hi", "hello"):
        return {"intent": "PING"}

    if t == "help":
        return {"intent": "HELP"}

    if t == "mem":
        return {"intent": "MEMORY"}

    if t.startswith("run "):
        return {"intent": "RUN", "payload": text[4:]}

    return {"intent": "ECHO", "payload": text}
