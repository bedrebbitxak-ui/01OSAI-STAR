import time


def log(msg: str):
    """
    Стандартный логгер 01OSAI-STAR.
    Формат:
    [2026-05-07 04:12:33] MESSAGE
    """
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {msg}")
