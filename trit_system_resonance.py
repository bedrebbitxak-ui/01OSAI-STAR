# 01OSAI-STAR-TRIT98 — Trit System Resonance
# Системный резонанс TRIT98: глубинное взаимодействие ядра, origin-слоя и системной волны

from trit_system_wave import TritSystemWave
from trit_origin_resonance import TritOriginResonance
from trit_system_core import TritSystemCore

class TritSystemResonance:
    def __init__(self):
        self.wave = TritSystemWave()
        self.origin_res = TritOriginResonance()
        self.core = TritSystemCore()

        self.history = []

    def measure(self):
        """
        Измерение системного резонанса:
        - резонанс ядра
        - резонанс origin-слоя
        - резонанс системной волны
        """
        core_snap = self.core.pulse()
        origin_snap = self.origin_res.measure()
        wave_snap = self.wave.propagate()

        resonance = {
            "core": core_snap,
            "origin": origin_snap,
            "wave": wave_snap
        }

        self.history.append(resonance)
        return resonance

    def snapshot(self):
        return {
            "last": self.history[-1] if self.history else None,
            "history_length": len(self.history)
        }


if __name__ == "__main__":
    tsr = TritSystemResonance()
    print("=== TRIT SYSTEM RESONANCE ===")
    print(tsr.measure())
