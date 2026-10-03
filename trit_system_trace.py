# 01OSAI-STAR-TRIT98 — Trit System Trace
# Трассировка системных шагов TRIT98

from trit_system_log import TritSystemLog
from trit_system_cycle import TritSystemCycle

class TritSystemTrace:
    def __init__(self):
        self.log = TritSystemLog()
        self.cycle = TritSystemCycle()
        self.traces = []

    def trace_cycle(self):
        snap = self.cycle.cycle()
        self.log.write("trace", "cycle executed", level="TRACE")
        self.traces.append(snap)
        return snap

    def run_many(self, count=3):
        seq = []
        for _ in range(count):
            seq.append(self.trace_cycle())
        return seq

    def snapshot(self):
        return {
            "count": len(self.traces),
            "last": self.traces[-1] if self.traces else None,
            "log": self.log.snapshot()
        }


if __name__ == "__main__":
    tst = TritSystemTrace()
    print("=== TRIT SYSTEM TRACE RUN MANY ===")
    print(tst.run_many(2))
