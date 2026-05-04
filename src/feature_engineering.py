import pandas as pd
import numpy as np

class FeatureEngineer:
    def transform(self, df):
        df = df.copy()

        df["log_bytes"] = np.log1p(df["bytes"])

        if "duration" not in df.columns:
            df["duration"] = 0

        df["log_duration"] = np.log1p(df["duration"])

        df["protocol"] = df["protocol"].astype("category").cat.codes

        features = df[["protocol", "log_bytes", "log_duration"]]

        return df, features