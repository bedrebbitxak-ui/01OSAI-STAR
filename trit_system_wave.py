# 01OSAI-STAR-TRIT98 — Trit System Wave
# Системная волна TRIT98: объединённый ритм ядра и origin-слоя

from math import sin, cos, pi

from trit_system_core import TritSystemCore
from trit_origin_wave import TritOriginWave

class TritSystemWave:
    def __init__(self):
        self.core = TritSystemCore()
        self.origin_wave = TritOriginWave()

        self.phase = 0.0
        self.history = []

    def energy(self, index):
        """
        Системная волновая энергия:
        sin(system_phase + index * 0.1) * origin_wave_energy
        """
        origin_energy = self.origin_wave.wave_energy(index)
        return sin(self.phase + index * 0.1) * origin_energy

    def propagate(self):
        """
        Пропуск системной волны:
        1) центральный пульс
        2) первичная волна
        3) системное колебание
        """
        core_snap = self.core.pulse()
        origin_snap = self.origin_wave.propagate()

        size = len(origin_snap)
        wave_map = []

        for i in range(size):
            wave_map.append({
                "index": i,
                "energy": self.energy(i)
            })

        self.phase += 0.2
        self.history.append(wave_map)

        return wave_map

    def snapshot(self):
        return {
            "phase": self.phase,
            "last_wave": self.history[-1] if self.history else None,
            "history_length": len(self.history)
        }


if __name__ == "__main__":
    tsw = TritSystemWave()
    print("=== TRIT SYSTEM WAVE PROPAGATE ===")
    print(tsw.propagate())
