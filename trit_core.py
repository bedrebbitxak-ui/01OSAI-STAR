# 01OSAI-STAR-TRIT98 — Trit Core
# Центральный управляющий узел тритовой архитектуры

from trit_topology import TritTopology
from trit_memory import TritMemory
from trit_runner import TritRunner
from trit_router import TritRouter
from trit_intents import TritIntents
from trit_auto import TritAuto
from trit_bridge import TritBridge

class TritCore:
    def __init__(self):
        self.memory = TritMemory()
        self.memory.load()

        self.topology = self.memory.topology
        self.runner = TritRunner()
        self.router = TritRouter()
        self.intents = TritIntents()
        self.auto = TritAuto()
        self.bridge = TritBridge()

    def cycle(self):
        """
        Полный трит-цикл:
        1) маршрутизация
        2) исполнение
        3) снимок
        """
        routes = self.router.route()
        run_result = self.runner.run()
        snapshot = self.memory.topology.snapshot()

        return {
            "routes": routes,
            "run": run_result,
            "snapshot": snapshot
        }

    def auto_cycle(self):
        """
        Автоматический трит-цикл.
        """
        return self.auto.cycle()

    def apply_intent(self, name):
        """
        Применение намерения.
        """
        return self.intents.apply_intent(name)

    def export_binary(self):
        """
        Экспорт тритовой системы в бинарную карту.
        """
        return self.bridge.export_binary_map()

    def import_binary(self, binary_map):
        """
        Импорт бинарной карты в тритовую систему.
        """
        self.bridge.import_binary_map(binary_map)

    def snapshot(self):
        """
        Полный снимок всей тритовой архитектуры.
        """
        return {
            "topology": self.memory.topology.snapshot(),
            "intents": self.intents.list_intents(),
            "binary": self.bridge.export_binary_map()
        }
