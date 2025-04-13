# app/services/pcap_saver.py
import os
import logging

def save_packet(data, save_path):
    logging.info(f"Received data of size: {len(data)} bytes")
    with open(save_path, "wb") as f:
        f.write(data)
    
    # Verify the file was created and has content
    file_size = os.path.getsize(save_path)
    logging.info(f"Saved PCAP file at {save_path} with size: {file_size} bytes")
    
    # Return file size for additional validation
    return file_size