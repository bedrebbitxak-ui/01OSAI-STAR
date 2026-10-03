# 01OSAI-STAR-TRIT98 — Trit Multiverse
# Многослойная модель TRIT98: параллельные вселенные, сравнение, объединение

from trit_universe import TritUniverse

class TritMultiverse:
    def __init__(self):
        # Список параллельных трит-вселенных
        self.universes = []

        # История объединений
        self.merges = []

    def spawn_universe(self):
        """
        Создать новую трит-вселенную.
        """
        u = TritUniverse()
        snapshot = u.expand()
        self.universes.append(snapshot)
        return snapshot

    def spawn_many(self, count=3):
        """
        Создать несколько параллельных вселенных.
        """
        created = []
        for _ in range(count):
            created.append(self.spawn_universe())
        return created

    def compare(self, idx1, idx2):
        """
        Сравнить две трит-вселенные.
        """
        if idx1 >= len(self.universes) or idx2 >= len(self.universes):
            return "Invalid universe index."

        u1 = self.universes[idx1]
        u2 = self.universes[idx2]

        return {
            "phase_1": u1["state"]["phase"],
            "phase_2": u2["state"]["phase"],
            "energy_1": u1["field"],
            "energy_2": u2["field"],
            "resonance_1": u1["resonance"],
            "resonance_2": u2["resonance"]
        }

    def merge(self, idx1, idx2):
        """
        Объединить две трит-вселенные в одну.
        """
        if idx1 >= len(self.universes) or idx2 >= len(self.universes):
            return "Invalid universe index."

        u1 = self.universes[idx1]
        u2 = self.universes[idx2]

        merged = {
            "phase": (u1["state"]["phase"], u2["state"]["phase"]),
            "field": (u1["field"], u2["field"]),
            "wave": (u1["wave"], u2["wave"]),
            "resonance": (u1["resonance"], u2["resonance"]),
            "system_maps": (u1["system_map"], u2["system_map"])
        }

        self.merges.append(merged)
        return merged

    def snapshot(self):
        """
        Снимок трит-мультивселенной.
        """
        return {
            "universes_count": len(self.universes),
            "merges_count": len(self.merges),
            "last_universe": self.universes[-1] if self.universes else None,
            "last_merge": self.merges[-1] if self.merges else None
        }


if __name__ == "__main__":
    tm = TritMultiverse()

    print("=== SPAWN MULTIVERSE ===")
    print(tm.spawn_many(3))

    print("\n=== MULTIVERSE SNAPSHOT ===")
    print(tm.snapshot())
