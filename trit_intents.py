# 01OSAI-STAR-TRIT98 — Trit Intents
# Тритовые намерения: смысловые команды для тритовой архитектуры

from trit_topology import TritTopology, Trit
from trit_memory import TritMemory

class TritIntent:
    def __init__(self, name, target_nodes, desired_state):
        """
        name — имя намерения (строка)
        target_nodes — список узлов, на которые направлено намерение
        desired_state — желаемое трит-состояние (-1, 0, +1)
        """
        self.name = name
        self.target_nodes = target_nodes
        self.desired_state = desired_state


class TritIntents:
    def __init__(self):
        self.memory = TritMemory()
        self.memory.load()
        self.topology = self.memory.topology

        # Список всех намерений
        self.intents = []

    def add_intent(self, name, nodes, state):
        """
        Создание нового трит-намерения.
        """
        intent = TritIntent(name, nodes, state)
        self.intents.append(intent)

    def apply_intent(self, intent_name):
        """
        Применение намерения по имени.
        """
        for intent in self.intents:
            if intent.name == intent_name:
                for node_index in intent.target_nodes:
                    self.memory.set(node_index, value=f"intent:{intent_name}", state=intent.desired_state)
                return True
        return False

    def list_intents(self):
        """
        Возвращает список всех намерений.
        """
        return [
            {
                "name": intent.name,
                "nodes": intent.target_nodes,
                "state": intent.desired_state
            }
            for intent in self.intents
        ]

    def snapshot(self):
        """
        Возвращает снимок всех намерений и их влияния.
        """
        return {
            "intents": self.list_intents(),
            "memory": self.memory.topology.snapshot()
        }
