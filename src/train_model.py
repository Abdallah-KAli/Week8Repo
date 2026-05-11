import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pandas as pd
import joblib
from sklearn.ensemble import IsolationForest
from src.feature_engineering import FeatureEngineer

DATA_PATH = "data/network_logs.csv"
MODEL_PATH = "model/isolation_forest.pkl"

def train():
    df = pd.read_csv(DATA_PATH)

    fe = FeatureEngineer()
    df_full, X = fe.transform(df)

    model = IsolationForest(
        n_estimators=200,
        contamination=0.05,
        random_state=42
    )

    model.fit(X)

    joblib.dump((model, fe), MODEL_PATH)

    print("Model saved correctly")

if __name__ == "__main__":
    train()