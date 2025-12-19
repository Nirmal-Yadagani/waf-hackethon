import time
import pandas as pd

from src.traffic_ingestor import TrafficIngestor
from src.feature_extractor import FeatureExtractor
from src.statistical_baseline import StatisticalBaseline
from src.online_isolation_forest import OnlineIForest
from src.decision_engine import DecisionEngine
from src.explainability import explain
from src.rule_recommender import RuleRecommender


def main():
    # 1. Load traffic
    ingestor = TrafficIngestor()
    # df = ingestor.load_csv("data/traffic.csv")
    df = ingestor.load_csv("data/csic_database.csv")
    # df = ingestor.normalize(df)
    print("Loaded traffic data:")
    print(df.columns)
    # df_benign = df[df[" Label"] == "BENIGN"]
    # df_malicious = df[df[" Label"] != "BENIGN"]

    # # 2. Feature extraction
    # extractor = FeatureExtractor(window="10s")
    # features_df = extractor.extract(df)
    # print("Extracted features:")
    # print(features_df)

    # # 3. Initialize baseline (first N windows)
    # init_windows = 50
    # baseline = StatisticalBaseline(alpha=0.01)
    # baseline.initialize(features_df.iloc[:init_windows])

    # # 4. Initialize Isolation Forest
    # iforest = OnlineIForest(window_size=500)
    # iforest.fit_initial(features_df.iloc[:init_windows].values)

    # # 5. Decision + rule engine
    # decision_engine = DecisionEngine()
    # rule_engine = RuleRecommender()

    # print("🚀 Starting online anomaly detection...\n")

    # # 6. Online processing
    # for idx in range(init_windows, len(features_df)):
    #     current = features_df.iloc[idx]

    #     z_scores, z_anom = baseline.score(current)
    #     if_score = iforest.score(current.values)

    #     decision = decision_engine.decide(z_anom, if_score)

    #     print(f"[{features_df.index[idx]}] Decision: {decision}")

    #     if decision == "ANOMALY":
    #         explanation = explain(z_scores)
    #         context = {
    #             "ip": "unknown",
    #             "timestamp": str(features_df.index[idx])
    #         }

    #         rules = rule_engine.recommend(decision, z_scores, context)
    #         print("⚠️  Explanation:", explanation)
    #         print("📜 Recommended Rules:", rules)

    #     else:
    #         baseline.update(current)
    #         iforest.update(current.values)

    #     print("-" * 60)
    #     # time.sleep(0.2)  # demo-friendly pacing


if __name__ == "__main__":
    main()
