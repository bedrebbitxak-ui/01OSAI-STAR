# auto_pipeline.py
# Auto-Pipeline v1 — полный цикл: план → исполнение → цепочка → улучшение → память

from core.utils import log


class AutoPipeline:
    """
    Auto-Pipeline v1:
      - принимает задачу (text)
      - вызывает PlannerAgent v4 → план + исполнение + refined-план
      - строит auto-chain под задачу
      - исполняет auto-chain
      - улучшает структуру цепочки
      - сохраняет факт в Semantic Memory
      - возвращает сводный отчёт
    """

    def __init__(self, shell):
        self.shell = shell

    def run(self, task: str) -> str:
        shell = self.shell

        # 1) Планировщик v4 (через агента planner)
        planner = shell.agents.get("planner")
        if planner is None:
            return "[pipeline] ERROR: planner agent not found"

        planner.state["shell"] = shell
        log("[pipeline] step 1: planner.v4")
        plan_report = planner.step(task)

        # 2) Auto-Chains v1 — построить и выполнить цепочку под задачу
        log("[pipeline] step 2: auto-chains.v1")
        chain_result, chain_structure = shell.autochain.run(task)

        # 3) Auto-Refine v1 — улучшить структуру цепочки
        log("[pipeline] step 3: auto-refine.chain")
        refined_chain = shell.refine.refine_chain(chain_structure, chain_result)

        # 4) Semantic Memory v1 — сохранить факт из результата
        log("[pipeline] step 4: semantic.store")
        semantic_store = shell.semantic.add_fact_from_text(chain_result)

        # 5) Сводный отчёт
        report = (
            "[pipeline.v1]\n"
            "=== TASK ===\n"
            f"{task}\n\n"
            "=== PLANNER v4 REPORT ===\n"
            f"{plan_report}\n\n"
            "=== AUTO-CHAIN RESULT ===\n"
            f"{chain_result}\n\n"
            "=== AUTO-CHAIN STRUCTURE ===\n"
            f"{chain_structure}\n\n"
            "=== REFINED CHAIN STRUCTURE ===\n"
            f"{refined_chain}\n\n"
            "=== SEMANTIC MEMORY STORE ===\n"
            f"{semantic_store}\n"
        )

        return report
