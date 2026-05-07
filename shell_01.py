from intents.resolver import resolve
from basic import intent_help, intent_echo, intent_run, intent_memory, intent_module
from core.utils import log


class Shell01:
    def __init__(self, memory, modules):
        self.memory = memory
        self.modules = modules
        self.alive = True
        log("SHELL_01: initialized")

    def run(self):
        while self.alive:
            try:
                user_input = input(">>> ")

                # логируем вход
                log(f"01OSAI: input → {user_input}")

                # сохраняем в память
                self.memory.store(user_input)

                # определяем intent
                intent = resolve(user_input)
                itype = intent["intent"]

                # обработка intents
                if itype == "EXIT":
                    self.alive = False
                    print("Goodbye.")
                    continue

                if itype == "HELP":
                    print(intent_help())
                    continue

                if itype == "MEMORY":
                    print(intent_memory(self.memory))
                    continue

                if itype == "RUN":
                    print(intent_run(intent["payload"]))
                    continue

                if itype == "MODULE":
                    result = intent_module(self.modules, intent["payload"])
                    print(result)
                    # сохраняем ответ
                    self.memory.store(result)
                    continue

                if itype == "PING":
                    print("Pong.")
                    continue

                if itype == "ECHO":
                    result = intent_echo(intent["payload"])
                    print(result)
                    self.memory.store(result)
                    continue

            except KeyboardInterrupt:
                print("\nInterrupted.")
                self.alive = False

            except Exception as e:
                print(f"Shell error: {e}")
