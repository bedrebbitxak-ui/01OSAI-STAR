# 01OSAI-STAR-TRIT98 — Trit System Sync
# Системная синхронизация TRIT98: объединение ядра, origin-слоя и системного слоя

from trit_system_core import TritSystemCore
from trit_system_state import TritSystemState
from trit_system_universe import TritSystemUniverse
from trit_system_multiverse import TritSystemMultiverse

class TritSystemSync:
    def __init__(self):
        self.core = TritSystemCore()
        self.state = TritSystemState()
        self.universe = TritSystemUniverse()
        self.multiverse = TritSystemMultiverse()

        self.history = []

    def full_sync(self):
        """
        Полная системная синхронизация TRIT98:
        1) ядро
        2) состояние
        3) вселенная
        4) мультивселенная
        """
        core_snap = self.core.pulse()
        state_snap = self.state.update()
        universe_snap = self.universe.expand()
        multiverse_snap = self.multiverse.spawn()

        sync_snapshot = {
            "core": core_snap,
            "state": state_snap,
            "universe": universe_snap,
            "multiverse": multiverse_snap
        }

        self.history.append(sync_snapshot)
        return sync_snapshot

    def snapshot(self):
        return {
            "last": self.history[-1] if self.history else None,
            "history_length": len(self.history)
        }


if __name__ == "__main__":
    tss = TritSystemSync()
    print("=== TRIT SYSTEM FULL SYNC ===")
    print(tss.full_sync())
