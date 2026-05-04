import pandas as pd
import random
from datetime import datetime, timedelta
import os

def generate_logs(num_records=1000):
    logs = []
    base_time = datetime.now()

    for i in range(num_records):

        log = {
            "timestamp": base_time + timedelta(seconds=i),
            "src_ip": f"192.168.1.{random.randint(1, 255)}",
            "dst_ip": f"10.0.0.{random.randint(1, 255)}",
            "port": random.choice([80, 443, 22, 21, 8080]),
            "protocol": random.choice(["TCP", "UDP"]),
            "bytes": random.randint(200, 5000),
            "label": "normal"
        }

        # inject anomalies
        if random.random() < 0.07:
            log.update({
                "port": random.choice([4444, 5555, 9999]),
                "bytes": random.randint(10000, 80000),
                "protocol": "TCP",
                "label": "suspicious"
            })

        logs.append(log)

    return pd.DataFrame(logs)


if __name__ == "__main__":

    df = generate_logs(1000)

    # safety check
    if df.empty:
        raise ValueError("Dataset generation failed")

    path = "data/network_logs.csv"
    os.makedirs("data", exist_ok=True)

    df.to_csv(path, index=False)

    print("✅ Logs generated successfully")
    print("Saved to:", path)
    print("Rows:", len(df))