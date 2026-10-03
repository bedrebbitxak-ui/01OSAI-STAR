# 01OSAI-STAR-TRIT98 — Trit System Multiverse
# Системная мультивселенная TRIT98: множество системных вселенных

from trit_system_universe import TritSystemUniverse

class TritSystemMultiverse:
    def __init__(self):
        self.universes = []
        self.merges = []

    def spawn(self):
        """
        Создать новую системную вселенную.
        """
        u = TritSystemUniverse()
        snap = u.expand()
        self.universes.append(snap)
        return snap

    def spawn_many(self, count=3):
        created = []
        for _ in range(count):
            created.append(self.spawn())
        return created

    def merge(self, idx1, idx2):
        """
        Объединить две системные вселенные.
        """
        if idx1 >= len(self.universes) or idx2 >= len(self.universes):
            return None

        u1 = self.universes[idx1]
        u2 = self.universes[idx2]

        merged = {
            "phase": (u1["phase"], u2["phase"]),
            "field": (u1["field"], u2["field"]),
            "resonance": (u1["resonance"], u2["resonance"])
        }

        self.merges.append(merged)
        return merged

    def snapshot(self):
        return {
            "universes_count": len(self.universes),
            "merges_count": len(self.merges),
            "last_universe": self.universes[-1] if self.universes else None,
            "last_merge": self.merges[-1] if self.merges else None
        }


if __name__ == "__main__":
    tsm = TritSystemMultiverse()
    print("=== TRIT SYSTEM MULTIVERSE SPAWN ===")
    print(tsm.spawn_many(3))
