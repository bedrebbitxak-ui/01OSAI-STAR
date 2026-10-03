# 01OSAI-STAR-TRIT98 — Trit Origin System
# Корневая система происхождения TRIT98: объединение всех origin-слоёв

from trit_origin import TritOrigin
from trit_origin_signature import TritOriginSignature
from trit_origin_matrix import TritOriginMatrix
from trit_origin_field import TritOriginField
from trit_origin_wave import TritOriginWave
from trit_origin_resonance import TritOriginResonance
from trit_origin_phase import TritOriginPhase
from trit_origin_state import TritOriginState

class TritOriginSystem:
    def __init__(self):
        self.origin = TritOrigin()
        self.signature = TritOriginSignature()
        self.matrix = TritOriginMatrix()
        self.field = TritOriginField()
        self.wave = TritOriginWave()
        self.resonance = TritOriginResonance()
        self.phase = TritOriginPhase()
        self.state = TritOriginState()

        # История системных снимков
        self.history = []

    def update(self):
        """
        Обновление всей корневой системы TRIT98.
        """
        snapshot = {
            "origin": self.origin.snapshot(),
            "signature": self.signature.snapshot(),
            "matrix": self.matrix.update(),
            "field": self.field.update(),
            "wave": self.wave.propagate(),
            "resonance": self.resonance.measure(),
            "phase": self.phase.shift(),
            "state": self.state.update()
        }

        self.history.append(snapshot)
        return snapshot

    def snapshot(self):
        return {
            "last": self.history[-1] if self.history else None,
            "history_length": len(self.history)
        }


if __name__ == "__main__":
    tos = TritOriginSystem()
    print("=== TRIT ORIGIN SYSTEM UPDATE ===")
    print(tos.update())
