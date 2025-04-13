# app/config.py
# Paths relative to the container's (or local) file system.
INPUT_PCAP = "/data/input.pcap"
OUTPUT_CSV = "/data/output/converted.csv"
# app/config.py
MODEL_PATH = "/app/models/model.pkl"
SCALER_PATH = "/app/models/scaler.pkl"
# Prediction thresholds (adjust according to your training)
THRESHOLD_LOW = 0.4
THRESHOLD_HIGH = 0.6
