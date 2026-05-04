import joblib
import pandas as pd

MODEL_PATH = "model/isolation_forest.pkl"

model, fe = joblib.load(MODEL_PATH)

def predict_single(data: dict):
    df = pd.DataFrame([data])
    _, X = fe.transform(df)

    score = model.decision_function(X)[0]
    pred = model.predict(X)[0]

    if score < -0.05:
        risk = "HIGH"
    elif score < 0:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    return {
        "prediction": "anomaly" if pred == -1 else "normal",
        "score": float(score),
        "risk": risk
    }