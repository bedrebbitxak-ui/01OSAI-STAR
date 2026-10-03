# 01OSAI-STAR-TRIT98 — Trit System Runner
# Исполнитель системных циклов TRIT98: запускает обновления и циклы

from trit_system import TritSystem
from trit_system_state import TritSystemState
from trit_system_universe import TritSystemUniverse
from trit_system_multiverse import TritSystemMultiverse

class TritSystemRunner:
    def __init__(self):
        self.system = TritSystem()
        self.state = TritSystemState()
        self.universe = TritSystemUniverse()
        self.multiverse = TritSystemMultiverse()

        self.history = []

    def cycle(self):
        """
        Один системный цикл TRIT98:
        - обновление системы
        - обновление состояния
        - расширение вселенной
        - создание мультивселенной
        """
        sys = self.system.update()
        st = self.state.update()
        uni = self.universe.expand()
        multi = self.multiverse.spawn()

        cycle_snapshot = {
            "system": sys,
            "state": st,
            "universe": uni,
            "multiverse": multi
        }

        self.history.append(cycle_snapshot)
        return cycle_snapshot

    def snapshot(self):
        return {
            "last": self.history[-1] if self.history else None,
            "history_length": len(self.history)
        }


if __name__ == "__main__":
    tsrun = TritSystemRunner()
    print("=== TRIT SYSTEM RUNNER CYCLE ===")
    print(tsrun.cycle())
