# app/routes.py
from flask import Blueprint, request, jsonify
from .services import pcap_saver, cicflow_converter, csv_loader, model_predictor, cleaner
from .config import INPUT_PCAP, OUTPUT_CSV, THRESHOLD_LOW, THRESHOLD_HIGH

api = Blueprint("api", __name__)

@api.route("/predict", methods=["POST"])
def predict():
    try:
        # 1. Save the incoming raw packet data as a PCAP file.
        pcap_saver.save_packet(request.data, INPUT_PCAP)
        
        # 2. Convert the PCAP file to CSV using the Python cicflowmeter package.
        cicflow_converter.convert(INPUT_PCAP, OUTPUT_CSV)
        
        # 3. Load and preprocess the CSV to match your training pipeline.
        df = csv_loader.load_and_preprocess(OUTPUT_CSV)
        if df.empty:
            return jsonify({"status": "UNKNOWN", "reason": "No valid flows found"}), 400
        
        # 4. Predict using the ML model.
        prediction, proba = model_predictor.predict(df)
        
        # 5. Determine the final status.
        if proba > THRESHOLD_HIGH:
            status = "MALICIOUS"
        elif proba < THRESHOLD_LOW:
            status = "BENIGN"
        else:
            status = "UNKNOWN"
        
        # 6. Clean up temporary files.
        cleaner.cleanup([INPUT_PCAP, OUTPUT_CSV])
        
        return jsonify({"status": status, "probability": float(proba)})
    
    except Exception as e:
        return jsonify({"error": "Processing failed", "details": str(e)}), 500
