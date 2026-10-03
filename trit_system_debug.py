# 01OSAI-STAR-TRIT98 — Trit System Debug
# Отладочный слой TRIT98

from trit_system_log import TritSystemLog

class TritSystemDebug:
    def __init__(self):
        self.log = TritSystemLog()
        self.flags = {
            "trace_wave": False,
            "trace_field": False,
            "trace_resonance": False
        }

    def enable(self, flag):
        if flag in self.flags:
            self.flags[flag] = True
            self.log.write("debug", f"enabled {flag}", level="DEBUG")

    def disable(self, flag):
        if flag in self.flags:
            self.flags[flag] = False
            self.log.write("debug", f"disabled {flag}", level="DEBUG")

    def snapshot(self):
        return {
            "flags": self.flags,
            "log": self.log.snapshot()
        }


if __name__ == "__main__":
    tsd = TritSystemDebug()
    tsd.enable("trace_wave")
    print("=== TRIT SYSTEM DEBUG SNAPSHOT ===")
    print(tsd.snapshot())
