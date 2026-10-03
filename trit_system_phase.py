# 01OSAI-STAR-TRIT98 — Trit System Phase
# Системная фаза TRIT98: режим работы всей системы

from trit_system_resonance import TritSystemResonance

class TritSystemPhase:
    def __init__(self):
        self.resonance = TritSystemResonance()
        self.phase = "system-neutral"
        self.history = []

    def detect(self):
        """
        Определение системной фазы на основе:
        - резонанса ядра
        - резонанса origin-слоя
        - резонанса системной волны
        """
        res = self.resonance.measure()

        wave_energy = sum(e["energy"] for e in res["wave"])
        origin_energy = res["origin"]["total_energy"]

        if wave_energy > 10 and origin_energy > 40:
            self.phase = "system-active"
        elif wave_energy < -10:
            self.phase = "system-collapsed"
        elif origin_energy < 10:
            self.phase = "system-low"
        else:
            self.phase = "system-neutral"

        self.history.append(self.phase)
        return self.phase

    def shift(self):
        """
        Системный фазовый сдвиг.
        """
        return self.detect()

    def snapshot(self):
        return {
            "phase": self.phase,
            "history_length": len(self.history)
        }


if __name__ == "__main__":
    tsp = TritSystemPhase()
    print("=== TRIT SYSTEM PHASE SHIFT ===")
    print(tsp.shift())
