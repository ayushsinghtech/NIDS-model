import os

# Get the base directory (one level up from this file's directory)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Paths relative to the project root
INPUT_PCAP = os.path.join(BASE_DIR, 'data', 'input.pcap')
OUTPUT_CSV = os.path.join(BASE_DIR, 'data', 'output', 'converted.csv')

MODEL_PATH = os.path.join(BASE_DIR, 'models', 'model.pkl')
SCALER_PATH = os.path.join(BASE_DIR, 'models', 'scaler.pkl')

# Prediction thresholds (adjust according to your training)
THRESHOLD_LOW = 0.4
THRESHOLD_HIGH = 0.6
