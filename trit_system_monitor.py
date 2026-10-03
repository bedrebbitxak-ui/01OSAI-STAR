# 01OSAI-STAR-TRIT98 — Trit System Monitor
# Наблюдение за состоянием TRIT98

from trit_system_state import TritSystemState
from trit_system_energy import TritSystemEnergy

class TritSystemMonitor:
    def __init__(self):
        self.state = TritSystemState()
        self.energy = TritSystemEnergy()
        self.history = []

    def scan(self):
        state_snap = self.state.update()
        energy_snap = self.energy.measure()

        monitor_snapshot = {
            "state": state_snap,
            "energy": energy_snap
        }

        self.history.append(monitor_snapshot)
        return monitor_snapshot

    def snapshot(self):
        return {
            "last": self.history[-1] if self.history else None,
            "history_length": len(self.history)
        }


if __name__ == "__main__":
    tsm = TritSystemMonitor()
    print("=== TRIT SYSTEM MONITOR SCAN ===")
    print(tsm.scan())
