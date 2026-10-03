# 01OSAI-STAR-TRIT98 — Trit System Field
# Системное поле TRIT98: объединённое энергетическое распределение системы

from trit_system_flow import TritSystemFlow
from trit_origin_field import TritOriginField

class TritSystemField:
    def __init__(self):
        self.flow = TritSystemFlow()
        self.origin_field = TritOriginField()

        self.field = []
        self.history = []

    def build(self):
        """
        Построение системного поля:
        объединение origin-поля и потокового состояния.
        """
        flow_snap = self.flow.propagate()
        origin_energy = self.origin_field.normalized()

        # Простая формула объединения:
        # системная энергия = нормализованное origin-поле + фаза ядра * 0.01
        core_phase = flow_snap["core"]["identity"]["phase"]["phase"] \
            if "phase" in flow_snap["core"]["identity"] else 0

        self.field = [
            e + core_phase * 0.01
            for e in origin_energy
        ]

        self.history.append(self.field)
        return self.field

    def snapshot(self):
        return {
            "field": self.field,
            "history_length": len(self.history)
        }


if __name__ == "__main__":
    tsf = TritSystemField()
    print("=== TRIT SYSTEM FIELD BUILD ===")
    print(tsf.build())
