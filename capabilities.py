# capabilities.py
# Capabilities v1 — единая структура возможностей OSAI

class Capabilities:
    """
    Объединяет:
      - semantic memory
      - modules (tools)
      - agents
      - chains
      - llm (osai)
    """

    def __init__(self, shell):
        self.shell = shell

        self.semantic = shell.semantic
        self.modules = shell.modules
        self.agents = shell.agents
        self.chains = shell.chains
        self.llm = shell.osai

    def list(self):
        return {
            "semantic": list(self.semantic.facts),
            "modules": list(self.modules.keys()),
            "agents": list(self.agents.keys()),
            "chains": list(self.chains.keys()),
            "llm": "OSAI-Bridge",
        }

    def run_chain(self, name, text):
        if name not in self.chains:
            return f"[capabilities] chain '{name}' not found"
        ctx = {"text": text}
        result = self.chains[name].run(ctx, self.shell)
        return result.get("text", "")

    def run_module(self, name, command, args):
        if name not in self.modules:
            return f"[capabilities] module '{name}' not found"
        return self.modules[name].run(command, args)

    def run_agent(self, name, text):
        if name not in self.agents:
            return f"[capabilities] agent '{name}' not found"
        agent = self.agents[name]
        agent.state["shell"] = self.shell
        return agent.step(text)

    def ask(self, question):
        """
        LLM отвечает, используя semantic memory как контекст.
        """
        facts = "\n".join(f"- {f}" for f in self.semantic.facts)
        prompt = (
            "Вот факты:\n"
            f"{facts}\n\n"
            "Ответь на вопрос, опираясь только на эти факты.\n"
            "Если фактов недостаточно — скажи об этом.\n\n"
            f"Вопрос: {question}"
        )
        return self.llm.run(prompt)
