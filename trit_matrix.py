# 01OSAI-STAR-TRIT98 — Trit Matrix
# Матричное представление тритовой архитектуры: 98×98 трит-матрица связей

from trit_topology import TritTopology, Trit
from trit_memory import TritMemory

class TritMatrix:
    def __init__(self):
        self.memory = TritMemory()
        self.memory.load()
        self.topology = self.memory.topology

        # Матрица 98×98
        self.matrix = self.build_matrix()

    def build_matrix(self):
        """
        Создание трит-матрицы:
        matrix[i][j] = состояние связи между узлом i и узлом j
        -1 = связь свернута
         0 = нет связи
        +1 = связь активна
        """
        size = len(self.topology.nodes)
        matrix = [[0 for _ in range(size)] for _ in range(size)]

        for node in self.topology.nodes:
            for linked in node.links:
                # Активная связь = +1
                matrix[node.index][linked.index] = 1

            # Если узел свернут → все его связи -1
            if node.state == Trit.NEG:
                for j in range(size):
                    matrix[node.index][j] = -1

        return matrix

    def update(self):
        """
        Обновление матрицы после изменения трит-состояний.
        """
        self.matrix = self.build_matrix()
        return self.matrix

    def row(self, index):
        """
        Получить строку матрицы (все связи узла).
        """
        return self.matrix[index]

    def col(self, index):
        """
        Получить столбец матрицы (все входящие связи).
        """
        return [self.matrix[i][index] for i in range(len(self.matrix))]

    def snapshot(self):
        """
        Полный снимок матрицы.
        """
        return {
            "matrix": self.matrix,
            "size": len(self.matrix)
        }


if __name__ == "__main__":
    tm = TritMatrix()

    print("=== TRIT MATRIX SNAPSHOT ===")
    print(tm.snapshot())
