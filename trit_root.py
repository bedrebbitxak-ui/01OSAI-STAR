# 01OSAI-STAR-TRIT98 — Trit Root
# Абсолютный корень TRIT98: фундаментальная точка системы, базовый смысловой слой

from trit_origin import TritOrigin
from trit_system_map import TritSystemMap
from trit_state import TritState
from trit_universe import TritUniverse
from trit_multiverse import TritMultiverse

class TritRoot:
    def __init__(self):
        # Корневой источник
        self.origin = TritOrigin()

        # Карта системы
        self.system_map = TritSystemMap()

        # Состояние
        self.state = TritState()

        # Пространственные слои
        self.universe = TritUniverse()
        self.multiverse = TritMultiverse()

        # Корневой идентификатор
        self.root_id = "TRIT98-ROOT"

        # История корневых состояний
        self.history = []

    def initialize(self):
        """
        Инициализация TRIT98 из корня:
        1) сброс к первичному источнику
        2) построение карты
        3) обновление состояния
        4) расширение вселенной
        """
        origin_snapshot = self.origin.reset()
        system_map_snapshot = self.system_map.snapshot()
        state_snapshot = self.state.update()
        universe_snapshot = self.universe.expand()

        root_snapshot = {
            "root_id": self.root_id,
            "origin": origin_snapshot,
            "system_map": system_map_snapshot,
            "state": state_snapshot,
            "universe": universe_snapshot
        }

        self.history.append(root_snapshot)
        return root_snapshot

    def pulse(self):
        """
        Корневой пульс TRIT98:
        обновляет все слои системы из корня.
        """
        origin = self.origin.pulse()
        state = self.state.update()
        universe = self.universe.expand()

        root_snapshot = {
            "root_id": self.root_id,
            "origin": origin,
            "state": state,
            "universe": universe
        }

        self.history.append(root_snapshot)
        return root_snapshot

    def snapshot(self):
        """
        Снимок абсолютного корня TRIT98.
        """
        return {
            "root_id": self.root_id,
            "origin": self.origin.snapshot(),
            "system_map": self.system_map.snapshot(),
            "state": self.state.snapshot(),
            "universe": self.universe.snapshot(),
            "multiverse": self.multiverse.snapshot(),
            "history_length": len(self.history)
        }


if __name__ == "__main__":
    tr = TritRoot()

    print("=== TRIT ROOT INIT ===")
    print(tr.initialize())

    print("\n=== TRIT ROOT PULSE ===")
    print(tr.pulse())

    print("\n=== TRIT ROOT SNAPSHOT ===")
    print(tr.snapshot())
