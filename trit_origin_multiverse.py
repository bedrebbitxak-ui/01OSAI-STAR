# 01OSAI-STAR-TRIT98 — Trit Origin Multiverse
# Первичная мультивселенная TRIT98: множество origin-вселенных

from trit_origin_universe import TritOriginUniverse

class TritOriginMultiverse:
    def __init__(self):
        self.universes = []
        self.merges = []

    def spawn(self):
        """
        Создать новую origin-вселенную.
        """
        u = TritOriginUniverse()
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
        Объединить две origin-вселенные.
        """
        if idx1 >= len(self.universes) or idx2 >= len(self.universes):
            return None

        u1 = self.universes[idx1]
        u2 = self.universes[idx2]

        merged = {
            "phase": (u1["phase"], u2["phase"]),
            "energy": (u1["energy"], u2["energy"]),
            "state": (u1["state"], u2["state"])
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
    tom = TritOriginMultiverse()
    print("=== TRIT ORIGIN MULTIVERSE SPAWN ===")
    print(tom.spawn_many(3))
