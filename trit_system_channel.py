# 01OSAI-STAR-TRIT98 — Trit System Channel
# Канал связи TRIT98: направленный поток сообщений

from trit_system_io import TritSystemIO

class TritSystemChannel:
    def __init__(self, name="main"):
        self.name = name
        self.io = TritSystemIO()
        self.messages = []

    def send(self, payload):
        msg = {
            "channel": self.name,
            "payload": payload
        }
        self.io.write(msg)
        self.messages.append(msg)
        return msg

    def receive(self, payload):
        return self.io.read(payload)

    def snapshot(self):
        return {
            "name": self.name,
            "messages_count": len(self.messages),
            "last_message": self.messages[-1] if self.messages else None
        }


if __name__ == "__main__":
    tsc = TritSystemChannel("system")
    tsc.send({"event": "start"})
    print("=== TRIT SYSTEM CHANNEL SNAPSHOT ===")
    print(tsc.snapshot())
