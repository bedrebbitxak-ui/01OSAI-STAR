# 01OSAI-STAR-TRIT98 — Trit System Bridge
# Системный мост TRIT98: соединение системного слоя с origin-слоем

from trit_system_hub import TritSystemHub
from trit_origin_system import TritOriginSystem
from trit_origin_universe import TritOriginUniverse
from trit_origin_multiverse import TritOriginMultiverse

class TritSystemBridge:
    def __init__(self):
        self.hub = TritSystemHub()
        self.origin_system = TritOriginSystem()
        self.origin_universe = TritOriginUniverse()
        self.origin_multiverse = TritOriginMultiverse()

        self.history = []

    def link(self):
        """
        Связь системного слоя и origin-слоя:
        объединение их состояний.
        """
        hub_snap = self.hub.pulse()
        origin_sys = self.origin_system.update()
        origin_uni = self.origin_universe.expand()
        origin_multi = self.origin_multiverse.spawn()

        bridge_snapshot = {
            "hub": hub_snap,
            "origin_system": origin_sys,
            "origin_universe": origin_uni,
            "origin_multiverse": origin_multi
        }

        self.history.append(bridge_snapshot)
        return bridge_snapshot

    def snapshot(self):
        return {
            "last": self.history[-1] if self.history else None,
            "history_length": len(self.history)
        }


if __name__ == "__main__":
    tsb = TritSystemBridge()
    print("=== TRIT SYSTEM BRIDGE LINK ===")
    print(tsb.link())
