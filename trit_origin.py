# 01OSAI-STAR-TRIT98 — Trit Origin
# Первичный источник TRIT98: корневой смысловой слой, нулевая точка системы

from trit_topology import TritTopology
from trit_memory import TritMemory
from trit_field import TritField
from trit_wave import TritWave
from trit_resonance import TritResonance
from trit_phase import TritPhase
from trit_state import TritState
from trit_universe import TritUniverse
from trit_multiverse import TritMultiverse

class TritOrigin:
    def __init__(self):
        # Корневые слои
        self.topology = TritTopology()
        self.memory = TritMemory()

        # Смысловые слои
        self.field = TritField()
        self.wave = TritWave()
        self.resonance = TritResonance()
        self.phase = TritPhase()
        self.state = TritState()

        # Пространственные слои
        self.universe = TritUniverse()
        self.multiverse = TritMultiverse()

        # История корневых снимков
        self.history = []

    def reset(self):
        """
        Полный сброс TRIT98 к первичному источнику.
        """
        self.topology = TritTopology()
        self.memory = TritMemory()
        self.memory.load()

        self.field = TritField()
        self.wave = TritWave()
        self.resonance = TritResonance()
        self.phase = TritPhase()
        self.state = TritState()
        self.universe = TritUniverse()
        self.multiverse = TritMultiverse()

        origin_snapshot = self.snapshot()
        self.history.append(origin_snapshot)
        return origin_snapshot

    def pulse(self):
        """
        Корневой пульс:
        1) обновить состояние
        2) обновить поле
        3) пропустить волну
        4) измерить резонанс
        5) фазовый сдвиг
        6) расширить вселенную
        """
        st = self.state.update()
        fld = self.field.update()
        wv = self.wave.propagate()
        rs = self.resonance.measure()
        ph = self.phase.shift()
        un = self.universe.expand()

        origin_snapshot = {
            "state": st,
            "field": fld,
            "wave": wv,
            "resonance": rs,
            "phase": ph,
            "universe": un
        }

        self.history.append(origin_snapshot)
        return origin_snapshot

    def snapshot(self):
        """
        Снимок первичного источника TRIT98.
        """
        return {
            "topology": self.topology.snapshot(),
            "memory": self.memory.topology.snapshot(),
            "field": self.field.snapshot(),
            "wave": self.wave.snapshot(),
            "resonance": self.resonance.snapshot(),
            "phase": self.phase.snapshot(),
            "state": self.state.snapshot(),
            "universe": self.universe.snapshot(),
            "multiverse": self.multiverse.snapshot(),
            "history_length": len(self.history)
        }


if __name__ == "__main__":
    to = TritOrigin()

    print("=== TRIT ORIGIN RESET ===")
    print(to.reset())

    print("\n=== TRIT ORIGIN PULSE ===")
    print(to.pulse())

    print("\n=== TRIT ORIGIN SNAPSHOT ===")
    print(to.snapshot())
