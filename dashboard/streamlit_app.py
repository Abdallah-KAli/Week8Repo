import streamlit as st
import requests
import pandas as pd
import time

API_URL = "http://127.0.0.1:5000/predict"

st.set_page_config(page_title="SOC Dashboard", layout="wide")

st.title("🛡 SOC Network Anomaly Detection Dashboard")

if "logs" not in st.session_state:
    st.session_state.logs = []

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Events", len(st.session_state.logs))

with col2:
    anomaly_count = len([l for l in st.session_state.logs if l["prediction"] == "anomaly"])
    st.metric("Anomalies", anomaly_count)

with col3:
    st.metric("Normal", len(st.session_state.logs) - anomaly_count)

st.divider()

with st.form("input_form"):
    timestamp = st.text_input("Timestamp")
    src_ip = st.text_input("Source IP")
    dst_ip = st.text_input("Destination IP")
    port = st.number_input("Port", 22)
    protocol = st.selectbox("Protocol", ["TCP", "UDP"])
    bytes_val = st.number_input("Bytes", 1000)

    submit = st.form_submit_button("Analyze")

if submit:
    payload = {
        "timestamp": timestamp,
        "src_ip": src_ip,
        "dst_ip": dst_ip,
        "port": port,
        "protocol": protocol,
        "bytes": bytes_val
    }

    try:
        res = requests.post(API_URL, json=payload, timeout=5).json()

        log = {
            "src_ip": src_ip,
            "dst_ip": dst_ip,
            "prediction": res["prediction"],
            "score": res["score"],
            "risk": res["risk"]
        }

        st.session_state.logs.append(log)

    except Exception as e:
        st.error(f"API Error: {e}")

st.divider()

st.subheader("📊 Live Traffic Log")

if st.session_state.logs:
    df = pd.DataFrame(st.session_state.logs)
    st.dataframe(df, use_container_width=True)

st.subheader("🚨 Risk Level Distribution")

if st.session_state.logs:
    st.bar_chart(pd.DataFrame(st.session_state.logs)["risk"].value_counts())