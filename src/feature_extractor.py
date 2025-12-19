import pandas as pd

class FeatureExtractor:
    def __init__(self, window="30s"):
        self.window = window

    def extract(self, df):
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df = df.set_index("timestamp")

        features = df.resample(self.window).agg(
            req_rate=("ip", "count"),
            unique_ips=("ip", "nunique"),
            avg_payload=("payload_size", "mean"),
            error_rate=("status", lambda x: (x >= 400).mean()),
            get_ratio=("method", lambda x: (x == "GET").mean())
        )

        return features.dropna()

