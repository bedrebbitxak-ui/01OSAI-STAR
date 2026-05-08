# intents/intent_pipeline.py

def intent_pipeline(shell, payload):
    """
    Auto-Pipeline v1:
      pipe <task>

    Пример:
      pipe конвертируй voice.wma в voice.ogg и запомни результат
    """
    task = payload.strip()
    if not task:
        return "Usage: pipe <task>"

    return shell.pipeline.run(task)
