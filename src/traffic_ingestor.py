import pandas as pd

class TrafficIngestor:
    def load_csv(self, path, timestamp_col=None):
        df = pd.read_csv(path)
        if timestamp_col:
            df[timestamp_col] = pd.to_datetime(df[timestamp_col])
        return df

    def normalize(self, df):
        return df[[
            "timestamp",
            "ip",
            "method",
            "status",
            "payload_size"
        ]]
