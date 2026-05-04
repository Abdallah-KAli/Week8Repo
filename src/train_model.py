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

    df_full["score"] = model.decision_function(X)
    df_full["prediction"] = model.predict(X)

    joblib.dump((model, fe), MODEL_PATH)

    print("Model trained successfully")
    print(df_full["prediction"].value_counts())

if __name__ == "__main__":
    train()