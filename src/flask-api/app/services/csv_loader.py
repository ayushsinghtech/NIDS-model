# app/services/csv_loader.py
import pandas as pd
import os
import joblib
from app.config import SCALER_PATH

def load_and_preprocess(csv_path):
    if not os.path.exists(csv_path):
        return pd.DataFrame()
    
    df = pd.read_csv(csv_path)
    
    # Drop columns not used during training (adjust these names as needed)
    drop_cols = ["Flow ID", "Src IP", "Dst IP", "Timestamp", "Label"]
    df.drop(columns=drop_cols, errors="ignore", inplace=True)
    
    # Drop rows with missing values
    df.dropna(inplace=True)
    
    # (Optional) Apply scaling if a scaler is provided
    if os.path.exists(SCALER_PATH):
        scaler = joblib.load(SCALER_PATH)
        df[df.columns] = scaler.transform(df[df.columns])
    
    return df
