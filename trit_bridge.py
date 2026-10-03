# 01OSAI-STAR-TRIT98 — Trit Bridge
# Мост между тритовой логикой (-1, 0, +1) и бинарной логикой (0, 1)

from trit_topology import TritTopology, Trit
from trit_memory import TritMemory

class TritBridge:
    def __init__(self):
        self.memory = TritMemory()
        self.memory.load()
        self.topology = self.memory.topology

    def trit_to_binary(self, trit_state):
        """
        Преобразование трит-состояния в бинарное:
        -1 → 0
         0 → 0
        +1 → 1
        """
        if trit_state == Trit.POS:
            return 1
        return 0

    def binary_to_trit(self, binary_state):
        """
        Преобразование бинарного состояния в трит:
        0 → 0
        1 → +1
        """
        if binary_state == 1:
            return Trit.POS
        return Trit.ZERO

    def export_binary_map(self):
        """
        Экспорт тритовой системы в бинарную карту.
        Возвращает список из 98 бинарных значений.
        """
        binary_map = []
        for node in self.topology.nodes:
            binary_map.append(self.trit_to_binary(node.state))
        return binary_map

    def import_binary_map(self, binary_map):
        """
        Импорт бинарной карты в тритовую систему.
        """
        for index, binary_state in enumerate(binary_map):
            trit_state = self.binary_to_trit(binary_state)
            self.memory.set(index, value=f"binary_import:{binary_state}", state=trit_state)

    def snapshot(self):
        """
        Возвращает бинарную и тритовую карты одновременно.
        """
        return {
            "trit": self.memory.topology.snapshot(),
            "binary": self.export_binary_map()
        }
