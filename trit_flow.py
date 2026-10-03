# 01OSAI-STAR-TRIT98 — Trit Flow
# Потоки тритовой логики: динамическое движение смыслов в системе

from trit_topology import TritTopology, Trit
from trit_memory import TritMemory
from trit_router import TritRouter
from trit_intents import TritIntents

class TritFlow:
    def __init__(self):
        self.memory = TritMemory()
        self.memory.load()

        self.topology = self.memory.topology
        self.router = TritRouter()
        self.intents = TritIntents()

        # История потоков
        self.history = []

    def build_flow(self):
        """
        Построение потока на основе текущих трит-состояний.
        Поток — это последовательность узлов:
        сначала активные (+1), затем нейтральные (0), затем свернутые (-1).
        """
        active = self.router.active_nodes()
        neutral = self.router.neutral_nodes()
        collapsed = self.router.collapsed_nodes()

        flow = {
            "active": active,
            "neutral": neutral,
            "collapsed": collapsed
        }

        self.history.append(flow)
        return flow

    def apply_flow_intent(self, name="flow_intent"):
        """
        Создание и применение намерения на основе текущего потока:
        активные → +1
        нейтральные → 0
        свернутые → -1
        """
        flow = self.build_flow()

        nodes = flow["active"] + flow["neutral"] + flow["collapsed"]
        if not nodes:
            return "No nodes in flow."

        # Для простоты: намерение ставит +1 на все узлы потока
        self.intents.add_intent(name, nodes, Trit.POS)
        applied = self.intents.apply_intent(name)

        return {
            "intent_name": name,
            "applied": applied,
            "flow": flow
        }

    def last_flow(self):
        """
        Получить последний построенный поток.
        """
        if not self.history:
            return None
        return self.history[-1]

    def snapshot(self):
        """
        Снимок состояния потоков.
        """
        return {
            "history": self.history,
            "current_flow": self.last_flow(),
            "topology": self.memory.topology.snapshot()
        }


if __name__ == "__main__":
    flow = TritFlow()

    print("=== BUILD FLOW ===")
    print(flow.build_flow())

    print("\n=== APPLY FLOW INTENT ===")
    print(flow.apply_flow_intent())
