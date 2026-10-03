# 01OSAI-STAR-TRIT98 — Trit System Matrix
# Системная матрица TRIT98: матричное представление системных связей

from trit_system_topology import TritSystemTopology

class TritSystemMatrix:
    def __init__(self):
        self.topology = TritSystemTopology()
        self.matrix = []
        self.history = []

        self._build_matrix()

    def _build_matrix(self):
        topo = self.topology.snapshot()
        nodes = topo["nodes"]
        size = len(nodes)

        # Пустая матрица
        self.matrix = [[0 for _ in range(size)] for _ in range(size)]

        # Заполнение связей
        for a, b in topo["links"]:
            i = nodes.index(a)
            j = nodes.index(b)
            self.matrix[i][j] = 1

    def snapshot(self):
        snap = {
            "matrix": self.matrix,
            "size": len(self.matrix)
        }
        self.history.append(snap)
        return snap


if __name__ == "__main__":
    tsm = TritSystemMatrix()
    print("=== TRIT SYSTEM MATRIX ===")
    print(tsm.snapshot())
