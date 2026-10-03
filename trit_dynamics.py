# 01OSAI-STAR-TRIT98 — Trit Dynamics
# Динамика тритовой логики: живое движение смыслов в реальном времени

from trit_flow import TritFlow
from trit_sync import TritSync
from trit_router import TritRouter
from trit_runner import TritRunner
from trit_intents import TritIntents

class TritDynamics:
    def __init__(self):
        self.flow = TritFlow()
        self.sync = TritSync()
        self.router = TritRouter()
        self.runner = TritRunner()
        self.intents = TritIntents()

        # История динамических циклов
        self.cycles = []

    def pulse(self):
        """
        Один трит-пульс:
        1) построить поток
        2) применить потоковое намерение
        3) выполнить трит-цикл
        4) синхронизировать с бинарной системой
        """
        flow = self.flow.build_flow()
        intent = self.flow.apply_flow_intent()
        cycle = self.runner.run()
        sync = self.sync.sync_to_binary()

        result = {
            "flow": flow,
            "intent": intent,
            "cycle": cycle,
            "sync": sync
        }

        self.cycles.append(result)
        return result

    def auto_pulse(self):
        """
        Автоматический трит-пульс:
        поток → авто-цикл → синхронизация
        """
        flow = self.flow.build_flow()
        auto_cycle = self.sync.system.trit_auto_cycle()
        sync = self.sync.sync_to_binary()

        result = {
            "flow": flow,
            "auto_cycle": auto_cycle,
            "sync": sync
        }

        self.cycles.append(result)
        return result

    def snapshot(self):
        """
        Снимок всей динамики.
        """
        return {
            "cycles": self.cycles,
            "last": self.cycles[-1] if self.cycles else None,
            "flow": self.flow.last_flow(),
            "sync": self.sync.snapshot()
        }


if __name__ == "__main__":
    dyn = TritDynamics()

    print("=== TRIT PULSE ===")
    print(dyn.pulse())

    print("\n=== AUTO PULSE ===")
    print(dyn.auto_pulse())
