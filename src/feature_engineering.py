import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

class FeatureEngineer:
    def __init__(self):
        self.scaler = StandardScaler()

    def transform(self, df):
        df = df.copy()

        if "duration" not in df.columns:
            df["duration"] = 0

        df["log_bytes"] = np.log1p(df["bytes"])
        df["log_duration"] = np.log1p(df["duration"])

        df["protocol"] = df["protocol"].astype("category").cat.codes

        features = df[["protocol", "log_bytes", "log_duration"]]

        X = self.scaler.fit_transform(features)

        return df, X