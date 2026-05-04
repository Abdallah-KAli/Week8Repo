from flask import Flask, request, jsonify
from src.predict import predict_single

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Network Anomaly Detection API Running"}

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    result = predict_single(data)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)