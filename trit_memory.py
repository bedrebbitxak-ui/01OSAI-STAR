# 01OSAI-STAR-TRIT98 — Trit Memory Module
# Тритовая память для хранения состояния 98 узлов тритовой топологии

import json
from trit_topology import TritTopology, Trit

class TritMemory:
    def __init__(self, filename="trit_memory.json"):
        self.filename = filename
        self.topology = TritTopology()
        self.data = {}

    def load(self):
        """Загрузка тритовой памяти из JSON файла."""
        try:
            with open(self.filename, "r") as f:
                self.data = json.load(f)

            # Восстановление состояния узлов
            for index, node_info in self.data.items():
                index = int(index)
                state = node_info.get("state", 0)
                value = node_info.get("value", None)

                self.topology.set_state(index, state)
                self.topology.set_value(index, value)

        except FileNotFoundError:
            self.data = {}

    def save(self):
        """Сохранение тритовой памяти в JSON файл."""
        snapshot = self.topology.snapshot()
        output = {}

        for index, state, value in snapshot:
            output[index] = {
                "state": state,
                "value": value
            }

        with open(self.filename, "w") as f:
            json.dump(output, f, indent=4)

    def set(self, index, value, state=Trit.ZERO):
        """Установка значения и состояния узла."""
        self.topology.set_value(index, value)
        self.topology.set_state(index, state)
        self.save()

    def get(self, index):
        """Получение информации об узле."""
        node = self.topology.get_node(index)
        if node:
            return {
                "index": node.index,
                "state": node.state,
                "value": node.value,
                "links": [n.index for n in node.links]
            }
        return None
