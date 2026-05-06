import time

def log(*args):
    """
    Простой логгер с таймстампом.
    """
    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}]", *args)
