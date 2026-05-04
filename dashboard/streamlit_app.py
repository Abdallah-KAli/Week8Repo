import streamlit as st
import requests
from datetime import datetime

API_URL = "http://127.0.0.1:5000/predict"

st.title("🛡 Network Anomaly Detection System")

timestamp = st.text_input("Timestamp", str(datetime.now()))
src_ip = st.text_input("Source IP", "192.168.1.10")
dst_ip = st.text_input("Destination IP", "10.0.0.5")
port = st.number_input("Port", 22)
protocol = st.selectbox("Protocol", ["TCP", "UDP"])
bytes_val = st.number_input("Bytes", 5000)

if st.button("Detect"):
    payload = {
        "timestamp": timestamp,
        "src_ip": src_ip,
        "dst_ip": dst_ip,
        "port": port,
        "protocol": protocol,
        "bytes": bytes_val
    }

    try:
        response = requests.post(API_URL, json=payload, timeout=5)

        if response.status_code != 200:
            st.error(f"API Error: {response.text}")
        else:
            result = response.json()

            if result["prediction"] == "anomaly":
                st.error("🚨 ANOMALY DETECTED")
            else:
                st.success("✅ NORMAL TRAFFIC")

            st.write("Score:", result["score"])

    except requests.exceptions.ConnectionError:
        st.error("❌ Cannot connect to API. Is Flask running?")
    except Exception as e:
        st.error(f"Unexpected error: {e}")