import time
from core.utils import log

class Watcher:
    def __init__(self, osai):
        self.osai = osai
        self.active = True
        log("WATCHER: initialized")

    def tick(self):
        """
        Один шаг наблюдения.
        """
        log("WATCHER: tick")
        # здесь можно добавить проверки состояния
        return True

    def loop(self):
        """
        Основной цикл наблюдателя.
        """
        log("WATCHER: loop started")
        while self.active:
            self.tick()
            time.sleep(1)
