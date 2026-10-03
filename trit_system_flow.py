# 01OSAI-STAR-TRIT98 — Trit System Flow
# Системный поток TRIT98: движение смыслов через ядро и origin-слой

from trit_system_core import TritSystemCore
from trit_origin_system import TritOriginSystem

class TritSystemFlow:
    def __init__(self):
        self.core = TritSystemCore()
        self.origin = TritOriginSystem()

        self.history = []

    def propagate(self):
        """
        Пропуск системного потока:
        1) центральный пульс
        2) обновление origin-системы
        """
        core_snap = self.core.pulse()
        origin_snap = self.origin.update()

        flow_snapshot = {
            "core": core_snap,
            "origin": origin_snap
        }

        self.history.append(flow_snapshot)
        return flow_snapshot

    def snapshot(self):
        return {
            "last": self.history[-1] if self.history else None,
            "history_length": len(self.history)
        }


if __name__ == "__main__":
    tsf = TritSystemFlow()
    print("=== TRIT SYSTEM FLOW PROPAGATE ===")
    print(tsf.propagate())
