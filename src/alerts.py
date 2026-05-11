
from datetime import datetime

class AlertManager:
    def __init__(self):
        self.alerts = []

    def create_alert(self, log, prediction, score, risk):
        alert = {
            "timestamp": str(datetime.now()),
            "src_ip": log.get("src_ip"),
            "dst_ip": log.get("dst_ip"),
            "prediction": prediction,
            "score": score,
            "risk": risk,
            "message": self._generate_message(risk)
        }

        self.alerts.append(alert)
        return alert

    def _generate_message(self, risk):
        if risk == "HIGH":
            return "🚨 Critical anomaly detected - immediate investigation required"
        elif risk == "MEDIUM":
            return "⚠ Suspicious activity detected - review recommended"
        else:
            return "ℹ Low-risk event detected"

    def get_alerts(self):
        return self.alerts