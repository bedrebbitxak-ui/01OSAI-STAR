# 01OSAI-STAR-TRIT98 — Trit System Dynamics
# Системная динамика TRIT98: изменение состояний во времени

from trit_system_state import TritSystemState
from trit_system_wave import TritSystemWave
from trit_system_field import TritSystemField

class TritSystemDynamics:
    def __init__(self):
        self.state = TritSystemState()
        self.wave = TritSystemWave()
        self.field = TritSystemField()

        self.history = []

    def step(self):
        """
        Один динамический шаг TRIT98:
        - обновление состояния
        - пропуск волны
        - перестройка поля
        """
        state_snap = self.state.update()
        wave_snap = self.wave.propagate()
        field_snap = self.field.build()

        dyn_snapshot = {
            "state": state_snap,
            "wave": wave_snap,
            "field": field_snap
        }

        self.history.append(dyn_snapshot)
        return dyn_snapshot

    def run(self, steps=5):
        seq = []
        for _ in range(steps):
            seq.append(self.step())
        return seq

    def snapshot(self):
        return {
            "last": self.history[-1] if self.history else None,
            "history_length": len(self.history)
        }


if __name__ == "__main__":
    tsd = TritSystemDynamics()
    print("=== TRIT SYSTEM DYNAMICS RUN ===")
    print(tsd.run(3))
