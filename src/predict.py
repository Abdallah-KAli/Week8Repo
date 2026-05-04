import joblib
import pandas as pd
import numpy as np

MODEL_PATH = "model/isolation_forest.pkl"
SCALER_PATH = "model/scaler.pkl"

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

def predict_single(data):
    df = pd.DataFrame([data])

    if "duration" not in df.columns:
        df["duration"] = 0

    df["log_bytes"] = np.log1p(df["bytes"])
    df["log_duration"] = np.log1p(df["duration"])
    df["protocol"] = pd.Categorical(df["protocol"]).codes

    X = df[["protocol", "log_bytes", "log_duration"]]
    X = scaler.transform(X)

    score = model.decision_function(X)[0]
    pred = model.predict(X)[0]

    return {
        "prediction": "anomaly" if pred == -1 else "normal",
        "score": float(score)
    }