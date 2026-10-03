# 01OSAI-STAR-TRIT98 — Trit System Graph
# Системный граф TRIT98: визуальная структура связей между системными узлами

from trit_system_topology import TritSystemTopology

class TritSystemGraph:
    def __init__(self):
        self.topology = TritSystemTopology()
        self.graph = {}
        self.history = []

        self._build_graph()

    def _build_graph(self):
        """
        Построение графа на основе системной топологии.
        """
        topo = self.topology.snapshot()

        for node in topo["nodes"]:
            self.graph[node] = []

        for a, b in topo["links"]:
            self.graph[a].append(b)

    def snapshot(self):
        snap = {
            "graph": self.graph,
            "nodes": list(self.graph.keys()),
            "edges": sum(len(v) for v in self.graph.values())
        }
        self.history.append(snap)
        return snap


if __name__ == "__main__":
    tsg = TritSystemGraph()
    print("=== TRIT SYSTEM GRAPH ===")
    print(tsg.snapshot())
