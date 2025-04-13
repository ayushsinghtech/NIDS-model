# app/routes.py
from flask import Blueprint, request, jsonify
from .services import pcap_saver, cicflow_converter, csv_loader, model_predictor, cleaner
from .config import INPUT_PCAP, OUTPUT_CSV, THRESHOLD_LOW, THRESHOLD_HIGH
import logging

api = Blueprint("api", __name__)

@api.route("/predict", methods=["POST"])
def predict():
    logging.info("Received prediction request")
    
    try:
        # Check if data was received
        if not request.data:
            logging.warning("No packet data received")
            return jsonify({"status": "UNKNOWN", "reason": "No packet data received"}), 400
            
        logging.info(f"Received data of size: {len(request.data)} bytes")
        
        # 1. Save the incoming raw packet data as a PCAP file.
        # Ensure that your pcap_saver.save_packet returns the size (or another value indicating success)
        pcap_size = pcap_saver.save_packet(request.data, INPUT_PCAP)
        if pcap_size <= 0:
            logging.error("Failed to save PCAP data")
            return jsonify({"status": "UNKNOWN", "reason": "Failed to save PCAP data"}), 400
        
        # 2. Convert the PCAP file to CSV using cicflow_converter.
        # Again, ensure that cicflow_converter.convert returns a size or success indicator.
        csv_size = cicflow_converter.convert(INPUT_PCAP, OUTPUT_CSV)
        if csv_size <= 0:
            logging.error("CICFlowMeter produced empty or no CSV")
            return jsonify({"status": "UNKNOWN", "reason": "CICFlowMeter produced empty or no CSV"}), 400
        
        # 3. Continue with your processing:
        # For example, you could load and preprocess CSV data, run predictions, etc.
        # df = csv_loader.load_and_preprocess(OUTPUT_CSV)
        # prediction, proba = model_predictor.predict(df)
        # status = "MALICIOUS" if proba > THRESHOLD_HIGH else "BENIGN" if proba < THRESHOLD_LOW else "UNKNOWN"
        
        # 4. Optionally, clean up temporary files:
        # cleaner.cleanup([INPUT_PCAP, OUTPUT_CSV])
        
        # For demonstration, returning a success message:
        return jsonify({"status": "SUCCESS", "pcap_size": pcap_size, "csv_size": csv_size})
    
    except Exception as e:
        logging.exception("Error in prediction endpoint")
        return jsonify({
            "error": "Processing failed", 
            "details": str(e),
            "type": type(e).__name__
        }), 500
