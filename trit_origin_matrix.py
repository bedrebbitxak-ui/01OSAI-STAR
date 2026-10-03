# 01OSAI-STAR-TRIT98 — Trit Origin Matrix
# Матрица происхождения TRIT98: структурный корневой слой, первичная геометрия системы

from trit_origin import TritOrigin
from trit_origin_signature import TritOriginSignature
from trit_topology import TritTopology
from trit_memory import TritMemory

class TritOriginMatrix:
    def __init__(self):
        self.origin = TritOrigin()
        self.signature = TritOriginSignature()
        self.topology = TritTopology()
        self.memory = TritMemory()
        self.memory.load()

        # Матрица происхождения (корневая форма)
        self.matrix = self.build_matrix()

        # История матриц
        self.history = []

    def build_matrix(self):
        """
        Создание матрицы происхождения TRIT98.
        Формула:
        matrix[i][j] = трит-связь между узлом i и узлом j на уровне происхождения.
        -1 = корневая свернутая связь
         0 = нейтральная связь
        +1 = корневая активная связь
        """
        nodes = self.topology.nodes
        size = len(nodes)

        matrix = [[0 for _ in range(size)] for _ in range(size)]

        for node in nodes:
            for linked in node.links:
                # Корневой уровень: активная связь = +1
                matrix[node.index][linked.index] = 1

            # Если узел в NEG на уровне происхождения → свернуть связи
            if node.state == -1:
                for j in range(size):
                    matrix[node.index][j] = -1

        return matrix

    def update(self):
        """
        Обновление матрицы происхождения после изменения корневых слоёв.
        """
        self.matrix = self.build_matrix()
        self.history.append(self.matrix)
        return self.matrix

    def snapshot(self):
        """
        Снимок матрицы происхождения TRIT98.
        """
        return {
            "origin_signature": self.signature.snapshot(),
            "matrix": self.matrix,
            "size": len(self.matrix),
            "history_length": len(self.history)
        }


if __name__ == "__main__":
    tom = TritOriginMatrix()

    print("=== TRIT ORIGIN MATRIX ===")
    print(tom.snapshot())

    print("\n=== TRIT ORIGIN MATRIX UPDATE ===")
    print(tom.update())
