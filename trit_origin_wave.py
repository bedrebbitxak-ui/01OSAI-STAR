# 01OSAI-STAR-TRIT98 — Trit Origin Wave
# Первичная волна происхождения TRIT98: корневой ритм системы

from math import sin, cos, pi

from trit_origin import TritOrigin
from trit_origin_signature import TritOriginSignature
from trit_origin_matrix import TritOriginMatrix
from trit_origin_field import TritOriginField
from trit_topology import TritTopology

class TritOriginWave:
    def __init__(self):
        self.origin = TritOrigin()
        self.signature = TritOriginSignature()
        self.matrix = TritOriginMatrix()
        self.field = TritOriginField()
        self.topology = TritTopology()

        # Фаза первичной волны
        self.phase = 0.0

        # История волн
        self.history = []

    def wave_energy(self, index):
        """
        Первичная волновая энергия узла:
        sin(phase + index * 0.05) * origin_field_energy
        """
        base = self.field.field[index]
        return sin(self.phase + index * 0.05) * base

    def wave_state(self, index):
        """
        Первичное волновое состояние узла:
        - отрицательная волна → -1
        - слабая волна → 0
        - положительная волна → +1
        """
        e = self.wave_energy(index)
        if e > 0.25:
            return +1
        elif e < -0.25:
            return -1
        return 0

    def propagate(self):
        """
        Пропуск первичной волны через систему.
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
        self.phase += 0.15  # первичное движение волны

        return wave_map

    def resonance(self):
        """
        Первичный резонанс системы:
        сумма всех первичных волновых энергий.
        """
        return sum(self.wave_energy(i) for i in range(len(self.field.field)))

    def snapshot(self):
        """
        Снимок первичной волны TRIT98.
        """
        return {
            "origin_signature": self.signature.snapshot(),
            "origin_matrix": self.matrix.snapshot(),
            "origin_field": self.field.snapshot(),
            "phase": self.phase,
            "last_wave": self.history[-1] if self.history else None,
            "resonance": self.resonance(),
            "history_length": len(self.history)
        }


if __name__ == "__main__":
    tow = TritOriginWave()

    print("=== TRIT ORIGIN WAVE PROPAGATE ===")
    print(tow.propagate())

    print("\n=== TRIT ORIGIN WAVE SNAPSHOT ===")
    print(tow.snapshot())
