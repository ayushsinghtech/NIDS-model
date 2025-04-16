import json
import time
import requests
import subprocess

LOG_PATH = "/home/ayush/cowrie/var/log/cowrie/cowrie.json"
FLASK_URL = "http://localhost:5000/log"

def is_malicious(command):
    red_flags = ["wget", "curl", "nmap", "netcat", "rm -rf", "passwd", "adduser"]
    return any(flag in command for flag in red_flags)

def trap_ip(ip):
    print(f"[!] Trapping IP: {ip}")
    subprocess.run(["python3", "trap_ip.py", ip])

def tail_log():
    with open(LOG_PATH, "r") as f:
        f.seek(0, 2)
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.5)
                continue
            try:
                entry = json.loads(line.strip())
                if entry.get("eventid") == "cowrie.command.input":
                    cmd = entry.get("input", "")
                    src_ip = entry.get("src_ip", "")
                    label = "malicious" if is_malicious(cmd) else "non-malicious"

                    data = {
                        "timestamp": entry.get("timestamp"),
                        "src_ip": src_ip,
                        "command": cmd,
                        "label": label
                    }

                    print(f"[+] Command: {cmd} | IP: {src_ip} | Label: {label}")

                    # Send to Flask
                    requests.post(FLASK_URL, json=data)

                    # If malicious, trap the IP
                    if label == "malicious":
                        trap_ip(src_ip)

            except Exception as e:
                print(f"[!] Error: {e}")

if __name__ == "__main__":
    tail_log()
