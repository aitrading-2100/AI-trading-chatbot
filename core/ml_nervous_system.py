class NervousSystem:
    """
    ML/RL Nervous System: Validates & evolves replicants
    """
    def __init__(self):
        self.performance = {}

    def validate_decision(self, decision):
        return decision.get("confidence",0) >= 0.65

    def reward(self, replicant_id, profit):
        self.performance[replicant_id] = self.performance.get(replicant_id,0) + profit

    def prune_replicants(self):
        return [rid for rid,score in self.performance.items() if score < -0.1]
