# 01OSAI-STAR-TRIT98 — Trit System Guard
# Защитный слой TRIT98

from trit_system_monitor import TritSystemMonitor
from trit_system_log import TritSystemLog

class TritSystemGuard:
    def __init__(self):
        self.monitor = TritSystemMonitor()
        self.log = TritSystemLog()
        self.history = []

    def check(self):
        snap = self.monitor.scan()
        energy = snap["energy"]["field_energy"]

        status = "ok"
        if energy > 100:
            status = "overload"
        elif energy < -10:
            status = "unstable"

        self.log.write("guard", f"status={status}", level="WARN" if status != "ok" else "INFO")

        guard_snapshot = {
            "status": status,
            "scan": snap
        }

        self.history.append(guard_snapshot)
        return guard_snapshot

    def snapshot(self):
        return {
            "last": self.history[-1] if self.history else None,
            "history_length": len(self.history)
        }


if __name__ == "__main__":
    tsg = TritSystemGuard()
    print("=== TRIT SYSTEM GUARD CHECK ===")
    print(tsg.check())
