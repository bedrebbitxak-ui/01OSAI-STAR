# 01OSAI-STAR-TRIT98 — Trit Router
# Маршрутизатор тритовой логики: направляет действия на основе трит-состояний узлов

from trit_topology import TritTopology, Trit
from trit_memory import TritMemory
from trit_runner import TritRunner

class TritRouter:
    def __init__(self):
        self.memory = TritMemory()
        self.memory.load()
        self.topology = self.memory.topology
        self.runner = TritRunner()

    def route(self):
        """
        Маршрутизация действий на основе трит-состояний узлов.
        Возвращает список маршрутов:
        - collapse → свернуть действие
        - hold → удержать действие
        - expand → раскрыть действие
        """
        routes = []

        for node in self.topology.nodes:
            if node.state == Trit.NEG:
                routes.append((node.index, "collapse"))
            elif node.state == Trit.ZERO:
                routes.append((node.index, "hold"))
            elif node.state == Trit.POS:
                routes.append((node.index, "expand"))
            else:
                routes.append((node.index, "unknown"))

        return routes

    def active_nodes(self):
        """
        Возвращает список узлов, которые находятся в состоянии +1 (expand).
        """
        return [node.index for node in self.topology.nodes if node.state == Trit.POS]

    def collapsed_nodes(self):
        """
        Возвращает список узлов, которые находятся в состоянии -1 (collapse).
        """
        return [node.index for node in self.topology.nodes if node.state == Trit.NEG]

    def neutral_nodes(self):
        """
        Возвращает список узлов, которые находятся в состоянии 0 (hold).
        """
        return [node.index for node in self.topology.nodes if node.state == Trit.ZERO]

    def snapshot(self):
        """
        Полный снимок маршрутизации.
        """
        return {
            "active": self.active_nodes(),
            "collapsed": self.collapsed_nodes(),
            "neutral": self.neutral_nodes(),
            "routes": self.route()
        }
