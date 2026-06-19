# SOC Network Anomaly Detection Dashboard

A Streamlit-based Security Operations Center (SOC) dashboard for detecting suspicious network traffic using a machine learning anomaly detection model.

This project was developed during my practical training at Optimum Partners. It applies machine learning concepts to a cybersecurity-inspired use case by analyzing network event data and identifying potentially abnormal traffic patterns.

## Overview

The dashboard allows users to enter network event details such as timestamp, source IP, destination IP, port, and protocol. The system processes the input and classifies the network event as normal or anomalous using a trained Isolation Forest model.

The project includes a Streamlit dashboard, a Flask API structure, saved machine learning model files, feature engineering scripts, and sample network log data.

## Features

* Interactive SOC-style dashboard built with Streamlit
* Network traffic anomaly detection
* Isolation Forest machine learning model
* Input form for network event details
* Event counters for total events, normal traffic, and anomalies
* Saved model and scaler using Joblib
* Flask API structure for backend integration
* Organized project structure for training, prediction, and feature engineering

## Tech Stack

* Python
* Streamlit
* Flask
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Machine Learning
* Isolation Forest

## Project Structure

```text
soc-network-anomaly-detection-dashboard/
│   .gitignore
│   LICENSE
│   README.md
│   requirements.txt
│
├── api/
│   ├── app.py
│   └── __init__.py
│
├── dashboard/
│   └── streamlit_app.py
│
├── data/
│   └── network_logs.csv
│
├── model/
│   ├── isolation_forest.pkl
│   └── scaler.pkl
│
└── src/
    ├── agents.py
    ├── alerts.py
    ├── feature_engineering.py
    ├── log_generator.py
    ├── predict.py
    ├── train_model.py
    └── __init__.py
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Abdallah-KAli/soc-network-anomaly-detection-dashboard.git
cd soc-network-anomaly-detection-dashboard
```

If the repository is still named `Week8Repo`, use:

```bash
git clone https://github.com/Abdallah-KAli/Week8Repo.git
cd Week8Repo
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## How to Run

Run the Streamlit dashboard from the `dashboard` folder:

```bash
cd dashboard
streamlit run .\streamlit_app.py
```

Then open the local URL shown in the terminal:

```text
http://localhost:8501
```

## Model

The project uses an Isolation Forest model for anomaly detection. Isolation Forest is commonly used to identify unusual patterns in data, making it suitable for detecting suspicious or abnormal network behavior.

The trained model and scaler are stored in the `model/` folder:

```text
model/isolation_forest.pkl
model/scaler.pkl
```

## Dataset

The project includes a sample network logs dataset:

```text
data/network_logs.csv
```

The dataset is used to simulate network activity and support training/testing of the anomaly detection model.

## Example Use Case

A SOC analyst or cybersecurity trainee can use the dashboard to test network events and review whether the traffic appears normal or suspicious based on the trained anomaly detection model.

Example event fields include:

* Timestamp
* Source IP
* Destination IP
* Port
* Protocol
