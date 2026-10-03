# 01OSAI-STAR-TRIT98 — Trit Resonance
# Глубинный резонанс TRIT98: взаимодействие волн, полей и потоков

from trit_wave import TritWave
from trit_field import TritField
from trit_flow import TritFlow
from trit_dynamics import TritDynamics

class TritResonance:
    def __init__(self):
        self.wave = TritWave()
        self.field = TritField()
        self.flow = TritFlow()
        self.dynamics = TritDynamics()

        # История резонансных состояний
        self.history = []

    def measure(self):
        """
        Измерение резонанса системы:
        - волновой резонанс
        - общая энергия поля
        - структура потока
        """
        wave_res = self.wave.resonance()
        total_energy = self.field.total_energy()
        current_flow = self.flow.last_flow()

        state = {
            "wave_resonance": wave_res,
            "total_energy": total_energy,
            "flow": current_flow
        }

        self.history.append(state)
        return state

    def pulse_resonance(self):
        """
        Резонансный пульс:
        1) пропустить волну
        2) обновить поле
        3) построить поток
        4) измерить резонанс
        """
        self.wave.propagate()
        self.field.update()
        self.flow.build_flow()
        dyn = self.dynamics.pulse()

        state = self.measure()
        state["dynamics"] = dyn

        return state

    def snapshot(self):
        """
        Снимок резонансного состояния.
        """
        return {
            "last": self.history[-1] if self.history else None,
            "history_length": len(self.history)
        }


if __name__ == "__main__":
    tr = TritResonance()

    print("=== TRIT RESONANCE PULSE ===")
    print(tr.pulse_resonance())

    print("\n=== TRIT RESONANCE SNAPSHOT ===")
    print(tr.snapshot())
