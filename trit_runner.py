# 01OSAI-STAR-TRIT98 — Trit Runner
# Исполнитель тритовой логики: принимает решения на основе трит-состояний узлов

from trit_topology import TritTopology, Trit
from trit_memory import TritMemory

class TritRunner:
    def __init__(self):
        self.memory = TritMemory()
        self.memory.load()
        self.topology = self.memory.topology

    def evaluate_node(self, node):
        """
        Интерпретация трит-состояния узла:
        -1 = свернуть действие
         0 = удержать действие
        +1 = раскрыть действие
        """
        if node.state == Trit.NEG:
            return f"Node {node.index}: collapse"
        elif node.state == Trit.ZERO:
            return f"Node {node.index}: hold"
        elif node.state == Trit.POS:
            return f"Node {node.index}: expand"
        return f"Node {node.index}: unknown"

    def run(self):
        """
        Основной цикл тритового исполнителя.
        Проходит по всем 98 узлам и интерпретирует их состояние.
        """
        results = []
        for node in self.topology.nodes:
            result = self.evaluate_node(node)
            results.append(result)
        return results

    def set_node(self, index, value=None, state=Trit.ZERO):
        """
        Установка значения и состояния узла через память.
        """
        self.memory.set(index, value, state)

    def snapshot(self):
        """
        Получение полного состояния тритовой системы.
        """
        return self.memory.topology.snapshot()
