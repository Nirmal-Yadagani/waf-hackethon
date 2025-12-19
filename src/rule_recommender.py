import uuid

class RuleRecommender:
    def recommend(self, decision, z_scores, context):
        if decision != "ANOMALY":
            return None

        rules = []

        if z_scores.get("req_rate", 0) > 3:
            rules.append(self.rate_limit_rule(context, z_scores))

        if z_scores.get("error_rate", 0) > 3:
            rules.append(self.block_scanner_rule(context, z_scores))

        return rules

    def rate_limit_rule(self, ctx, z):
        return {
            "rule_id": str(uuid.uuid4()),
            "condition": {
                "metric": "req_rate",
                "operator": ">",
                "threshold": "baseline + 3σ",
                "scope": "per_ip",
                "target": ctx["ip"]
            },
            "action": "RATE_LIMIT",
            "limit": "100 req/min",
            "ttl": "10m",
            "confidence": self.confidence(z["req_rate"]),
            "explanation": f"Request rate deviated by {z['req_rate']:.2f}σ"
        }

    def block_scanner_rule(self, ctx, z):
        return {
            "rule_id": str(uuid.uuid4()),
            "condition": {
                "metric": "error_rate",
                "operator": ">",
                "threshold": "baseline + 3σ",
                "scope": "per_ip",
                "target": ctx["ip"]
            },
            "action": "TEMP_BLOCK",
            "ttl": "5m",
            "confidence": self.confidence(z["error_rate"]),
            "explanation": f"High error rate deviation: {z['error_rate']:.2f}σ"
        }

    def confidence(self, z):
        return min(0.99, abs(z) / 6)
