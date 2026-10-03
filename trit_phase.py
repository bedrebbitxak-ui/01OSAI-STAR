# 01OSAI-STAR-TRIT98 — Trit Phase
# Фазовая модель TRIT98: переходы, режимы, состояния системы

from trit_wave import TritWave
from trit_resonance import TritResonance
from trit_field import TritField
from trit_flow import TritFlow

class TritPhase:
    def __init__(self):
        self.wave = TritWave()
        self.resonance = TritResonance()
        self.field = TritField()
        self.flow = TritFlow()

        # Текущая фаза системы
        self.phase = "neutral"

        # История фазовых переходов
        self.history = []

    def detect_phase(self):
        """
        Определение фазы системы на основе:
        - резонанса
        - общей энергии
        - структуры потока
        """
        res = self.resonance.measure()
        wave_res = res["wave_resonance"]
        total_energy = res["total_energy"]
        flow = res["flow"]

        # Простая фазовая логика:
        if wave_res > 10 and total_energy > 40:
            self.phase = "active"
        elif wave_res < -10:
            self.phase = "collapsed"
        elif flow and len(flow["active"]) > 30:
            self.phase = "charged"
        else:
            self.phase = "neutral"

        self.history.append(self.phase)
        return self.phase

    def shift(self):
        """
        Фазовый сдвиг:
        1) пропустить волну
        2) обновить поле
        3) построить поток
        4) измерить резонанс
        5) определить фазу
        """
        self.wave.propagate()
        self.field.update()
        self.flow.build_flow()
        self.resonance.measure()

        return self.detect_phase()

    def snapshot(self):
        """
        Снимок фазовой модели.
        """
        return {
            "phase": self.phase,
            "history": self.history,
            "last_resonance": self.resonance.snapshot(),
            "last_wave": self.wave.snapshot(),
            "last_field": self.field.snapshot(),
            "last_flow": self.flow.last_flow()
        }


if __name__ == "__main__":
    tp = TritPhase()

    print("=== TRIT PHASE SHIFT ===")
    print(tp.shift())

    print("\n=== TRIT PHASE SNAPSHOT ===")
    print(tp.snapshot())
