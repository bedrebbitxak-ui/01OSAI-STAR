# 01OSAI-STAR-TRIT98 — Trit System Energy
# Системная энергия TRIT98: оценка энергетического состояния системы

from trit_system_field import TritSystemField
from trit_system_wave import TritSystemWave
from trit_system_resonance import TritSystemResonance

class TritSystemEnergy:
    def __init__(self):
        self.field = TritSystemField()
        self.wave = TritSystemWave()
        self.resonance = TritSystemResonance()

        self.history = []

    def measure(self):
        """
        Измерение системной энергии:
        - энергия поля
        - энергия волны
        - резонансная энергия
        """
        field_snap = self.field.build()
        wave_snap = self.wave.propagate()
        res_snap = self.resonance.measure()

        field_energy = sum(field_snap) if field_snap else 0
        wave_energy = sum(e["energy"] for e in wave_snap) if wave_snap else 0
        res_energy = res_snap["origin"]["total_energy"] if "origin" in res_snap else 0

        energy_snapshot = {
            "field_energy": field_energy,
            "wave_energy": wave_energy,
            "resonance_energy": res_energy
        }

        self.history.append(energy_snapshot)
        return energy_snapshot

    def snapshot(self):
        return {
            "last": self.history[-1] if self.history else None,
            "history_length": len(self.history)
        }


if __name__ == "__main__":
    tse = TritSystemEnergy()
    print("=== TRIT SYSTEM ENERGY MEASURE ===")
    print(tse.measure())
