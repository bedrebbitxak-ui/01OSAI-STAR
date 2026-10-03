# 01OSAI-STAR-TRIT98 — Trit Logic Core
# Полная тритовая топология узлов 49×2 = 98 смысловых позиций

class Trit:
    NEG = -1   # свернуть
    ZERO = 0   # удержать
    POS = +1   # раскрыть


class TritNode:
    def __init__(self, index):
        self.index = index          # номер узла 0–97
        self.state = Trit.ZERO      # текущее трит-состояние
        self.value = None           # смысловое значение узла
        self.links = []             # связи с другими узлами

    def set_state(self, new_state):
        if new_state in (-1, 0, 1):
            self.state = new_state

    def connect(self, other_node):
        if other_node not in self.links:
            self.links.append(other_node)


class TritTopology:
    def __init__(self):
        self.nodes = [TritNode(i) for i in range(98)]  # 49×2 узлов

        # Верхний слой (0–48)
        self.upper = self.nodes[:49]

        # Нижний слой (49–97)
        self.lower = self.nodes[49:]

        # Автоматическая связь слоёв
        self._auto_link_layers()

    def _auto_link_layers(self):
        for i in range(49):
            upper_node = self.upper[i]
            lower_node = self.lower[i]

            # Связь верхнего и нижнего узла
            upper_node.connect(lower_node)
            lower_node.connect(upper_node)

    def set_value(self, index, value):
        if 0 <= index < 98:
            self.nodes[index].value = value

    def set_state(self, index, state):
        if 0 <= index < 98:
            self.nodes[index].set_state(state)

    def get_node(self, index):
        if 0 <= index < 98:
            return self.nodes[index]
        return None

    def snapshot(self):
        """Возвращает текущее трит-состояние всех узлов."""
        return [(node.index, node.state, node.value) for node in self.nodes]
