# intents/intent_semantic.py

def intent_semantic(shell, payload):
    """
    Команды:
      sem add <text>   — извлечь факт из текста и сохранить
      sem fact <text>  — сохранить факт напрямую
      sem list         — показать факты
      sem ask <q>      — ответить на вопрос на основе фактов
    """

    parts = payload.split(" ", 1)
    cmd = parts[0]

    # sem list
    if cmd == "list":
        return shell.semantic.list_facts()

    # sem add <text>
    if cmd == "add":
        if len(parts) < 2:
            return "Usage: sem add <text>"
        return shell.semantic.add_fact_from_text(parts[1])

    # sem fact <text>
    if cmd == "fact":
        if len(parts) < 2:
            return "Usage: sem fact <text>"
        return shell.semantic.add_fact(parts[1])

    # sem ask <question>
    if cmd == "ask":
        if len(parts) < 2:
            return "Usage: sem ask <question>"
        return shell.semantic.query(parts[1])

    return "Unknown semantic command"

