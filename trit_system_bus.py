# 01OSAI-STAR-TRIT98 — Trit System Bus
# Системная шина TRIT98: множество каналов связи

from trit_system_channel import TritSystemChannel

class TritSystemBus:
    def __init__(self):
        self.channels = {}
        self.history = []

    def get_channel(self, name):
        if name not in self.channels:
            self.channels[name] = TritSystemChannel(name)
        return self.channels[name]

    def broadcast(self, payload):
        snap = {}
        for name, ch in self.channels.items():
            snap[name] = ch.send(payload)
        self.history.append(snap)
        return snap

    def snapshot(self):
        return {
            "channels": list(self.channels.keys()),
            "history_length": len(self.history)
        }


if __name__ == "__main__":
    tsb = TritSystemBus()
    ch_sys = tsb.get_channel("system")
    ch_log = tsb.get_channel("log")
    tsb.broadcast({"event": "ping"})
    print("=== TRIT SYSTEM BUS SNAPSHOT ===")
    print(tsb.snapshot())
