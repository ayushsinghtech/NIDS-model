# app/services/cicflow_converter.py
import subprocess
import logging
import os

def convert(pcap_path, csv_path):
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    
    # Log the paths for debugging
    logging.info(f"Converting PCAP: {pcap_path} to CSV: {csv_path}")
    
    try:
        # Capture the output from the cicflowmeter command
        result = subprocess.run(
            ["cicflowmeter", "-f", pcap_path, "-c", csv_path], 
            check=True,
            capture_output=True,
            text=True
        )
        logging.info(f"CICFlowMeter output: {result.stdout}")
        
        # Check if the CSV was created and has content
        if os.path.exists(csv_path):
            file_size = os.path.getsize(csv_path)
            logging.info(f"CSV file created with size: {file_size} bytes")
            if file_size == 0:
                logging.error("CSV file is empty!")
            return file_size
        else:
            logging.error(f"CSV file was not created at {csv_path}")
            return 0
            
    except subprocess.CalledProcessError as e:
        logging.error(f"CICFlowMeter conversion failed: {e}")
        logging.error(f"STDERR: {e.stderr}")
        raise