def explain(z_scores):
    return {
        feature: f"{z:.2f}σ deviation"
        for feature, z in z_scores.items()
        if abs(z) > 2
    }
