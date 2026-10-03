# 01OSAI-STAR-TRIT98 — Trit System Universe
# Системная вселенная TRIT98: расширение системного состояния в пространство

from trit_system_state import TritSystemState

class TritSystemUniverse:
    def __init__(self):
        self.state = TritSystemState()
        self.history = []

    def expand(self):
        """
        Расширение системного состояния в системную вселенную.
        """
        snap = self.state.update()

        universe_snapshot = {
            "phase": snap["phase"],
            "wave": snap["wave"],
            "field": snap["field"],
            "resonance": snap["resonance"]
        }

        self.history.append(universe_snapshot)
        return universe_snapshot

    def snapshot(self):
        return {
            "last": self.history[-1] if self.history else None,
            "history_length": len(self.history)
        }


if __name__ == "__main__":
    tsu = TritSystemUniverse()
    print("=== TRIT SYSTEM UNIVERSE EXPAND ===")
    print(tsu.expand())
