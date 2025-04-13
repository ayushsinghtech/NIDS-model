# app/services/cicflow_converter.py
import subprocess

def convert(pcap_path, csv_path):
    # Run the cicflowmeter command to convert PCAP to CSV.
    # The command usage is: cicflowmeter -f <pcap> -c <csv>
    subprocess.run(["cicflowmeter", "-f", pcap_path, "-c", csv_path], check=True)
