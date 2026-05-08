from intents.resolver import resolve
from basic import intent_help, intent_echo, intent_run, intent_memory, intent_module, intent_agent, intent_chain, intent_llm
from intents.intent_semantic import intent_semantic
from core.utils import log
from agents import EchoAgent, MemoryAgent, PlannerAgent
from chains import build_test_chain
from chains_v2 import build_reason_chain, build_reason_audio_chain
from router import AutoRouter
from osai_bridge import OSAIBridge
from semantic_memory import SemanticMemory
from capabilities import Capabilities
from auto_tools import AutoTools     # ← ДОБАВЛЕНО


class Shell01:
    def __init__(self, memory, modules):
        self.memory = memory
        self.modules = modules
        self.alive = True

        # ← OSAI‑BRIDGE
        self.osai = OSAIBridge(self.memory)

        # ← SEMANTIC MEMORY v1
        self.semantic = SemanticMemory(self.osai)

        # ← АГЕНТЫ
        self.agents = {
            "echo": EchoAgent(),
            "memory": MemoryAgent(),
            "planner": PlannerAgent(),
        }
        self.active_agent = None

        # ← ЦЕПОЧКИ (v1 + v2)
        self.chains = {
            "test": build_test_chain(),
            "reason": build_reason_chain(),
            "reason_audio": build_reason_audio_chain(),
        }

        # ← CAPABILITIES v1
        self.capabilities = Capabilities(self)

        # ← AUTO‑TOOLS v1
        self.auto = AutoTools(self)     # ← ДОБАВЛЕНО

        # ← АВТО‑РОУТЕР
        self.router = AutoRouter(self)

        log("SHELL_01: initialized")

    def run(self):
        while self.alive:
            try:
                user_input = input(">>> ")

                log(f"01OSAI: input → {user_input}")

                self.memory.store(user_input)

                routed = self.router.route(user_input)
                if routed is not None:
                    intent = routed
                else:
                    intent = resolve(user_input)

                itype = intent["intent"]

                # ---------------------------------------------------------
                # INTENTS
                # ---------------------------------------------------------

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
                    self.memory.store(result)
                    continue

                elif itype == "AGENT":
                    result = intent_agent(self, intent["payload"])
                    print(result)
                    self.memory.store(result)
                    continue

                elif itype == "CHAIN":
                    result = intent_chain(self, intent["payload"])
                    print(result)
                    self.memory.store(result)
                    continue

                elif itype == "LLM":
                    result = intent_llm(self, intent["payload"])
                    print(result)
                    self.memory.store(result)
                    continue

                elif itype == "SEM":
                    result = intent_semantic(self, intent["payload"])
                    print(result)
                    self.memory.store(result)
                    continue

                # ---------------------------------------------------------

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
