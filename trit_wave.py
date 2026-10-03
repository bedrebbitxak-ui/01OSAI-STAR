# 01OSAI-STAR-TRIT98 — Trit Wave
# Волновая модель тритовой архитектуры: колебания, резонанс, ритм системы

from trit_field import TritField
from trit_graph import TritGraph
from trit_topology import Trit
from math import sin, cos, pi

class TritWave:
    def __init__(self):
        self.field = TritField()
        self.graph = TritGraph()

        # История волновых состояний
        self.history = []

        # Фаза волны
        self.phase = 0.0

    def wave_energy(self, index):
        """
        Волновая энергия узла:
        sin(phase + index * 0.1) * field_energy
        """
        base = self.field.field[index]
        return sin(self.phase + index * 0.1) * base

    def wave_state(self, index):
        """
        Волновое состояние узла:
        - отрицательная волна → -1
        - слабая волна → 0
        - положительная волна → +1
        """
        e = self.wave_energy(index)
        if e > 0.33:
            return Trit.POS
        elif e < -0.33:
            return Trit.NEG
        return Trit.ZERO

    def propagate(self):
        """
        Пропуск волны через всю систему.
        """
        size = len(self.field.field)
        wave_map = []

        for i in range(size):
            energy = self.wave_energy(i)
            state = self.wave_state(i)
            wave_map.append({
                "index": i,
                "energy": energy,
                "state": state
            })

        self.history.append(wave_map)
        self.phase += 0.25  # движение волны

        return wave_map

    def resonance(self):
        """
        Резонанс системы:
        сумма всех волновых энергий.
        """
        return sum(self.wave_energy(i) for i in range(len(self.field.field)))

    def snapshot(self):
        """
        Полный снимок волновой модели.
        """
        return {
            "phase": self.phase,
            "last_wave": self.history[-1] if self.history else None,
            "resonance": self.resonance(),
            "history_length": len(self.history)
        }


if __name__ == "__main__":
    tw = TritWave()

    print("=== TRIT WAVE PROPAGATION ===")
    print(tw.propagate())

    print("\n=== TRIT WAVE SNAPSHOT ===")
    print(tw.snapshot())
