# 01OSAI-STAR-TRIT98 — Trit Field
# Тритовое смысловое поле: распределение трит-энергии по узлам

from trit_topology import TritTopology, Trit
from trit_memory import TritMemory
from trit_graph import TritGraph

class TritField:
    def __init__(self):
        self.memory = TritMemory()
        self.memory.load()
        self.topology = self.memory.topology
        self.graph = TritGraph()

        # Поле: список из 98 энергетических значений
        self.field = self.build_field()

        # История изменений поля
        self.history = []

    def energy(self, state):
        """
        Преобразование трит-состояния в энергию:
        -1 → 0.1
         0 → 0.5
        +1 → 1.0
        """
        if state == Trit.NEG:
            return 0.1
        elif state == Trit.ZERO:
            return 0.5
        elif state == Trit.POS:
            return 1.0
        return 0.0

    def build_field(self):
        """
        Создание смыслового поля:
        energy[i] = энергия узла i
        """
        field = []
        for node in self.topology.nodes:
            field.append(self.energy(node.state))
        return field

    def update(self):
        """
        Обновление поля после изменения трит-состояний.
        """
        self.field = self.build_field()
        self.history.append(self.field.copy())
        return self.field

    def total_energy(self):
        """
        Общая энергия тритовой системы.
        """
        return sum(self.field)

    def normalized(self):
        """
        Нормализованное поле (значения от 0 до 1).
        """
        total = self.total_energy()
        if total == 0:
            return [0 for _ in self.field]
        return [v / total for v in self.field]

    def snapshot(self):
        """
        Полный снимок тритового смыслового поля.
        """
        return {
            "field": self.field,
            "normalized": self.normalized(),
            "total_energy": self.total_energy(),
            "history": self.history
        }


if __name__ == "__main__":
    tf = TritField()

    print("=== TRIT FIELD SNAPSHOT ===")
    print(tf.snapshot())
