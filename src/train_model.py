import pandas as pd
import joblib
from sklearn.ensemble import IsolationForest
from src.feature_engineering import FeatureEngineer

DATA_PATH = "data/network_logs.csv"
MODEL_PATH = "model/isolation_forest.pkl"
SCALER_PATH = "model/scaler.pkl"

def train():
    print("Loading data...")
    df = pd.read_csv(DATA_PATH)

    print("Engineering features...")
    fe = FeatureEngineer()
    df_full, X = fe.transform(df)

    print("Training Isolation Forest...")
    model = IsolationForest(
        n_estimators=150,
        contamination=0.05,
        random_state=42
    )

    model.fit(X)

    df_full["prediction"] = model.predict(X)
    df_full["prediction"] = df_full["prediction"].map({1: "normal", -1: "anomaly"})

    joblib.dump(model, MODEL_PATH)
    joblib.dump(fe.scaler, SCALER_PATH)

    print("Model trained successfully")
    print(df_full["prediction"].value_counts())

if __name__ == "__main__":
    train()