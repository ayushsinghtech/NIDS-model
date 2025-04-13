# app/services/pcap_saver.py
def save_packet(data, save_path):
    with open(save_path, "wb") as f:
        f.write(data)
