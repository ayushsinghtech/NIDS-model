# app/services/model_predictor.py
import joblib
from app.config import MODEL_PATH

# Load the pre-trained model
model = joblib.load(MODEL_PATH)

def predict(df):
    # Assuming binary classification and that predict_proba returns the probability for class 1 at index 1.
    proba = model.predict_proba(df)[0][1]
    pred = model.predict(df)[0]
    return pred, proba
