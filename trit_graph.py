# 01OSAI-STAR-TRIT98 — Trit Graph
# Графовое представление тритовой архитектуры: узлы, рёбра, веса, потоки

from trit_topology import TritTopology, Trit
from trit_memory import TritMemory

class TritGraph:
    def __init__(self):
        self.memory = TritMemory()
        self.memory.load()
        self.topology = self.memory.topology

        # Граф: список рёбер (i → j)
        self.edges = self.build_edges()

        # Веса рёбер
        self.weights = self.build_weights()

    def build_edges(self):
        """
        Построение списка рёбер:
        каждое ребро — это связь между узлом i и узлом j.
        """
        edges = []
        for node in self.topology.nodes:
            for linked in node.links:
                edges.append((node.index, linked.index))
        return edges

    def build_weights(self):
        """
        Построение весов рёбер:
        -1 = свернутая связь
         0 = нейтральная
        +1 = активная
        """
        weights = {}
        for node in self.topology.nodes:
            for linked in node.links:
                if node.state == Trit.NEG:
                    weights[(node.index, linked.index)] = -1
                elif node.state == Trit.ZERO:
                    weights[(node.index, linked.index)] = 0
                else:
                    weights[(node.index, linked.index)] = 1
        return weights

    def neighbors(self, index):
        """
        Получить всех соседей узла.
        """
        return [j for i, j in self.edges if i == index]

    def active_edges(self):
        """
        Все активные рёбра (+1).
        """
        return [edge for edge, w in self.weights.items() if w == 1]

    def collapsed_edges(self):
        """
        Все свернутые рёбра (-1).
        """
        return [edge for edge, w in self.weights.items() if w == -1]

    def neutral_edges(self):
        """
        Все нейтральные рёбра (0).
        """
        return [edge for edge, w in self.weights.items() if w == 0]

    def snapshot(self):
        """
        Полный снимок графа.
        """
        return {
            "edges": self.edges,
            "weights": self.weights,
            "active": self.active_edges(),
            "collapsed": self.collapsed_edges(),
            "neutral": self.neutral_edges()
        }


if __name__ == "__main__":
    tg = TritGraph()

    print("=== TRIT GRAPH SNAPSHOT ===")
    print(tg.snapshot())
