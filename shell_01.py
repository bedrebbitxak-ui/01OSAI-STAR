from intents.resolver import resolve
from basic import intent_help, intent_echo, intent_run, intent_memory, intent_module

class Shell01:
    def __init__(self, memory, modules):
        self.memory = memory
        self.modules = modules
        self.alive = True

    def run(self):
        while self.alive:
            try:
                user_input = input(">>> ")
                intent = resolve(user_input)

                itype = intent["intent"]

                # EXIT
                if itype == "EXIT":
                    self.alive = False
                    print("Goodbye.")
                    continue

                # HELP
                if itype == "HELP":
                    print(intent_help())
                    continue

                # MEMORY
                if itype == "MEMORY":
                    print(intent_memory(self.memory))
                    continue

                # RUN
                if itype == "RUN":
                    print(intent_run(intent["payload"]))
                    continue

                # MODULE
                if itype == "MODULE":
                    result = intent_module(self.modules, intent["payload"])
                    print(result)
                    continue

                # ECHO (default)
                if itype == "ECHO":
                    print(intent_echo(intent["payload"]))
                    continue

                # PING
                if itype == "PING":
                    print("Pong.")
                    continue

            except KeyboardInterrupt:
                print("\nInterrupted.")
                self.alive = False
            except Exception as e:
                print(f"Shell error: {e}")
