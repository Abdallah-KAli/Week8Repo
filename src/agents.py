
from src.alerts import AlertManager

class DetectorAgent:
    def detect(self, result):
        return result["prediction"] == "anomaly"


class AnalyzerAgent:
    def analyze(self, result):
        score = result["score"]

        if score < -0.2:
            return "Possible intrusion pattern (high confidence anomaly)"
        elif score < 0:
            return "Suspicious behavior detected"
        else:
            return "Low severity anomaly"


class ReporterAgent:
    def report(self, log, result, analysis):
        return {
            "log": log,
            "prediction": result["prediction"],
            "risk": result["risk"],
            "score": result["score"],
            "analysis": analysis
        }


class SOCMultiAgentSystem:
    def __init__(self):
        self.detector = DetectorAgent()
        self.analyzer = AnalyzerAgent()
        self.reporter = ReporterAgent()
        self.alert_manager = AlertManager()

    def run(self, log, result):
        if self.detector.detect(result):
            analysis = self.analyzer.analyze(result)
            report = self.reporter.report(log, result, analysis)

            alert = self.alert_manager.create_alert(
                log,
                result["prediction"],
                result["score"],
                result["risk"]
            )

            report["alert"] = alert
            return report

        return {
            "log": log,
            "prediction": result["prediction"],
            "risk": result["risk"],
            "score": result["score"],
            "analysis": "Normal traffic - no action required"
        }