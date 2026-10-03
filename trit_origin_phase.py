# 01OSAI-STAR-TRIT98 — Trit Origin Phase
# Первичная фаза происхождения TRIT98: корневой режим системы

from trit_origin import TritOrigin
from trit_origin_signature import TritOriginSignature
from trit_origin_matrix import TritOriginMatrix
from trit_origin_field import TritOriginField
from trit_origin_wave import TritOriginWave
from trit_origin_resonance import TritOriginResonance

class TritOriginPhase:
    def __init__(self):
        self.origin = TritOrigin()
        self.signature = TritOriginSignature()
        self.matrix = TritOriginMatrix()
        self.field = TritOriginField()
        self.wave = TritOriginWave()
        self.resonance = TritOriginResonance()

        # Текущая первичная фаза
        self.phase = "origin-neutral"

        # История фаз
        self.history = []

    def detect_phase(self):
        """
        Определение первичной фазы TRIT98 на основе:
        - первичного резонанса
        - общей корневой энергии
        - первичной волны
        - матрицы происхождения
        """
        res = self.resonance.measure()
        wave_res = res["wave_resonance"]
        total_energy = res["total_energy"]
        matrix = res["matrix"]

        # Простая корневая фазовая логика
        if wave_res > 5 and total_energy > 30:
            self.phase = "origin-active"
        elif wave_res < -5:
            self.phase = "origin-collapsed"
        elif any(-1 in row for row in matrix):
            self.phase = "origin-charged"
        else:
            self.phase = "origin-neutral"

        self.history.append(self.phase)
        return self.phase

    def shift(self):
        """
        Первичный фазовый сдвиг:
        1) пропустить первичную волну
        2) обновить первичное поле
        3) обновить матрицу происхождения
        4) измерить первичный резонанс
        5) определить фазу
        """
        self.wave.propagate()
        self.field.update()
        self.matrix.update()
        self.resonance.measure()

        return self.detect_phase()

    def snapshot(self):
        """
        Снимок первичной фазы TRIT98.
        """
        return {
            "origin_signature": self.signature.snapshot(),
            "origin_matrix": self.matrix.snapshot(),
            "origin_field": self.field.snapshot(),
            "origin_wave": self.wave.snapshot(),
            "origin_resonance": self.resonance.snapshot(),
            "phase": self.phase,
            "history_length": len(self.history)
        }


if __name__ == "__main__":
    top = TritOriginPhase()

    print("=== TRIT ORIGIN PHASE SHIFT ===")
    print(top.shift())

    print("\n=== TRIT ORIGIN PHASE SNAPSHOT ===")
    print(top.snapshot())
