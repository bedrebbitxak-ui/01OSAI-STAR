# 01OSAI-STAR-TRIT98 — Trit System Auto
# Автоматический системный режим TRIT98: авто-циклы и авто-синхронизация

from trit_system_hub import TritSystemHub
from trit_system_bridge import TritSystemBridge

class TritSystemAuto:
    def __init__(self):
        self.hub = TritSystemHub()
        self.bridge = TritSystemBridge()

        self.history = []

    def auto_cycle(self):
        """
        Автоматический системный цикл:
        1) системный пульс
        2) системный мост
        """
        hub_snap = self.hub.pulse()
        bridge_snap = self.bridge.link()

        auto_snapshot = {
            "hub": hub_snap,
            "bridge": bridge_snap
        }

        self.history.append(auto_snapshot)
        return auto_snapshot

    def run_many(self, count=5):
        cycles = []
        for _ in range(count):
            cycles.append(self.auto_cycle())
        return cycles

    def snapshot(self):
        return {
            "last": self.history[-1] if self.history else None,
            "history_length": len(self.history)
        }


if __name__ == "__main__":
    tsa = TritSystemAuto()
    print("=== TRIT SYSTEM AUTO RUN ===")
    print(tsa.run_many(3))
