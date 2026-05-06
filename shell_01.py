import time
from core.runner import Runner
from intents.resolver import resolve
from intents import basic

def log(msg):
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {msg}")

class Shell01:
    def __init__(self, memory):
        self.memory = memory
        self.runner = Runner()
        print("[SHELL_01] initialized")

    def run(self):
        while True:
            raw = input(">>> ")
            log(f"01OSAI: input → {raw}")
            self.memory.add(raw)

            intent = resolve(raw)

            if intent["intent"] == "PING":
                response = basic.intent_ping()

            elif intent["intent"] == "HELP":
                response = basic.intent_help()

            elif intent["intent"] == "MEMORY":
                response = basic.intent_memory(self.memory)

            elif intent["intent"] == "RUN":
                response = basic.intent_run(self.runner, intent["payload"])

            else:
                response = basic.intent_echo(raw)

            print(response)
            self.memory.add(response)
