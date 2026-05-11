import sys
import os
from flask import Flask, request, jsonify


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.predict import predict_single
from src.agents import SOCMultiAgentSystem

app = Flask(__name__)

soc = SOCMultiAgentSystem()

@app.route("/")
def home():
    return {"message": "SOC Anomaly Detection API Running"}

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    result = predict_single(data)
    report = soc.run(data, result)

    return jsonify(report)

if __name__ == "__main__":
    app.run(debug=True)