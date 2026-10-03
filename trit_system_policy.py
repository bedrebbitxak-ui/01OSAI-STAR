# 01OSAI-STAR-TRIT98 — Trit System Policy
# Правила работы TRIT98

from trit_system_guard import TritSystemGuard

class TritSystemPolicy:
    def __init__(self):
        self.guard = TritSystemGuard()
        self.rules = {
            "max_energy": 120,
            "min_energy": -20
        }
        self.history = []

    def enforce(self):
        snap = self.guard.check()
        energy = snap["scan"]["energy"]["field_energy"]

        violation = None
        if energy > self.rules["max_energy"]:
            violation = "energy-too-high"
        elif energy < self.rules["min_energy"]:
            violation = "energy-too-low"

        policy_snapshot = {
            "energy": energy,
            "violation": violation
        }

        self.history.append(policy_snapshot)
        return policy_snapshot

    def snapshot(self):
        return {
            "last": self.history[-1] if self.history else None,
            "history_length": len(self.history)
        }


if __name__ == "__main__":
    tsp = TritSystemPolicy()
    print("=== TRIT SYSTEM POLICY ENFORCE ===")
    print(tsp.enforce())
