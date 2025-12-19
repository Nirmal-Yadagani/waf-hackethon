class DecisionEngine:
    def decide(self, z_anomaly, iforest_score, if_thresh=-0.15):
        return "ANOMALY" if (z_anomaly or iforest_score < if_thresh) else "NORMAL"
