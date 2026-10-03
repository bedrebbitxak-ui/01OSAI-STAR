# 01OSAI-STAR-TRIT98 — Trit Universe
# Внешний слой TRIT98: расширенная модель смыслового пространства

from trit_system_map import TritSystemMap
from trit_state import TritState
from trit_field import TritField
from trit_wave import TritWave
from trit_resonance import TritResonance

class TritUniverse:
    def __init__(self):
        self.system_map = TritSystemMap()
        self.state = TritState()
        self.field = TritField()
        self.wave = TritWave()
        self.resonance = TritResonance()

        # История вселенских снимков
        self.history = []

    def expand(self):
        """
        Расширение TRIT98 до смысловой «вселенной»:
        1) обновить состояние
        2) обновить поле
        3) пропустить волну
        4) измерить резонанс
        5) собрать карту
        """
        st = self.state.update()
        fld = self.field.update()
        wv = self.wave.propagate()
        rs = self.resonance.measure()
        sm = self.system_map.snapshot()

        universe_snapshot = {
            "state": st,
            "field": fld,
            "wave": wv,
            "resonance": rs,
            "system_map": sm
        }

        self.history.append(universe_snapshot)
        return universe_snapshot

    def snapshot(self):
        """
        Снимок трит-вселенной.
        """
        return {
            "last": self.history[-1] if self.history else None,
            "history_length": len(self.history)
        }


if __name__ == "__main__":
    tu = TritUniverse()

    print("=== TRIT UNIVERSE EXPAND ===")
    print(tu.expand())

    print("\n=== TRIT UNIVERSE SNAPSHOT ===")
    print(tu.snapshot())
