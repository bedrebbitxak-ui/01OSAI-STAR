# 01OSAI-STAR-TRIT98 — Trit Origin Resonance
# Первичный резонанс TRIT98: глубинное взаимодействие корневых слоёв

from trit_origin import TritOrigin
from trit_origin_signature import TritOriginSignature
from trit_origin_matrix import TritOriginMatrix
from trit_origin_field import TritOriginField
from trit_origin_wave import TritOriginWave

class TritOriginResonance:
    def __init__(self):
        self.origin = TritOrigin()
        self.signature = TritOriginSignature()
        self.matrix = TritOriginMatrix()
        self.field = TritOriginField()
        self.wave = TritOriginWave()

        # История резонансных состояний
        self.history = []

    def measure(self):
        """
        Измерение первичного резонанса TRIT98:
        - волновой резонанс
        - общая корневая энергия
        - матричная структура
        """
        wave_res = self.wave.resonance()
        total_energy = self.field.total_energy()
        origin_matrix = self.matrix.matrix

        state = {
            "wave_resonance": wave_res,
            "total_energy": total_energy,
            "matrix": origin_matrix
        }

        self.history.append(state)
        return state

    def pulse(self):
        """
        Первичный резонансный пульс:
        1) пропустить первичную волну
        2) обновить первичное поле
        3) обновить матрицу происхождения
        4) измерить резонанс
        """
        self.wave.propagate()
        self.field.update()
        self.matrix.update()

        state = self.measure()
        return state

    def snapshot(self):
        """
        Снимок первичного резонанса TRIT98.
        """
        return {
            "origin_signature": self.signature.snapshot(),
            "origin_matrix": self.matrix.snapshot(),
            "origin_field": self.field.snapshot(),
            "origin_wave": self.wave.snapshot(),
            "last": self.history[-1] if self.history else None,
            "history_length": len(self.history)
        }


if __name__ == "__main__":
    tor = TritOriginResonance()

    print("=== TRIT ORIGIN RESONANCE PULSE ===")
    print(tor.pulse())

    print("\n=== TRIT ORIGIN RESONANCE SNAPSHOT ===")
    print(tor.snapshot())
