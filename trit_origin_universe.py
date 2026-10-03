# 01OSAI-STAR-TRIT98 — Trit Origin Universe
# Первичная вселенная происхождения TRIT98: расширение origin-слоя

from trit_origin_system import TritOriginSystem

class TritOriginUniverse:
    def __init__(self):
        self.system = TritOriginSystem()
        self.history = []

    def expand(self):
        """
        Расширение origin-слоя в первичную вселенную.
        """
        sys = self.system.update()

        universe_snapshot = {
            "system": sys,
            "energy": sys["field"],
            "wave": sys["wave"],
            "phase": sys["phase"],
            "state": sys["state"]
        }

        self.history.append(universe_snapshot)
        return universe_snapshot

    def snapshot(self):
        return {
            "last": self.history[-1] if self.history else None,
            "history_length": len(self.history)
        }


if __name__ == "__main__":
    tou = TritOriginUniverse()
    print("=== TRIT ORIGIN UNIVERSE EXPAND ===")
    print(tou.expand())
