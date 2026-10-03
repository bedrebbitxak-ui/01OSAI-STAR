# 01OSAI-STAR-TRIT98 — Trit Origin Field
# Первичное смысловое поле происхождения TRIT98: корневое распределение энергии

from trit_origin import TritOrigin
from trit_origin_signature import TritOriginSignature
from trit_origin_matrix import TritOriginMatrix
from trit_topology import TritTopology, Trit
from trit_memory import TritMemory

class TritOriginField:
    def __init__(self):
        self.origin = TritOrigin()
        self.signature = TritOriginSignature()
        self.matrix = TritOriginMatrix()
        self.topology = TritTopology()
        self.memory = TritMemory()
        self.memory.load()

        # Первичное поле происхождения
        self.field = self.build_field()

        # История полей
        self.history = []

    def energy(self, state):
        """
        Корневое преобразование трит-состояния в энергию:
        -1 → 0.05 (минимальная корневая энергия)
         0 → 0.33 (нейтральная корневая энергия)
        +1 → 1.00 (максимальная корневая энергия)
        """
        if state == Trit.NEG:
            return 0.05
        elif state == Trit.ZERO:
            return 0.33
        elif state == Trit.POS:
            return 1.00
        return 0.0

    def build_field(self):
        """
        Создание первичного смыслового поля TRIT98:
        energy[i] = корневая энергия узла i
        """
        field = []
        for node in self.topology.nodes:
            field.append(self.energy(node.state))
        return field

    def update(self):
        """
        Обновление корневого поля после изменений в происхождении.
        """
        self.field = self.build_field()
        self.history.append(self.field.copy())
        return self.field

    def total_energy(self):
        """
        Общая корневая энергия TRIT98.
        """
        return sum(self.field)

    def normalized(self):
        """
        Нормализованное корневое поле (значения от 0 до 1).
        """
        total = self.total_energy()
        if total == 0:
            return [0 for _ in self.field]
        return [v / total for v in self.field]

    def snapshot(self):
        """
        Снимок первичного смыслового поля TRIT98.
        """
        return {
            "origin_signature": self.signature.snapshot(),
            "origin_matrix": self.matrix.snapshot(),
            "field": self.field,
            "normalized": self.normalized(),
            "total_energy": self.total_energy(),
            "history_length": len(self.history)
        }


if __name__ == "__main__":
    tof = TritOriginField()

    print("=== TRIT ORIGIN FIELD ===")
    print(tof.snapshot())

    print("\n=== TRIT ORIGIN FIELD UPDATE ===")
    print(tof.update())
