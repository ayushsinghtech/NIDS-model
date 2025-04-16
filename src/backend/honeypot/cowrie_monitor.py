import json
import time
import requests

LOG_PATH = "/home/ayush/cowrie/var/log/cowrie/cowrie.json"
FLASK_URL = "http://localhost:5000/log"

def is_malicious(cmd):
    red_flags = ["wget", "curl", "nmap", "cat /etc/passwd", "rm -rf"]
    return any(flag in cmd for flag in red_flags)

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
                    result = "malicious" if is_malicious(cmd) else "non-malicious"
                    data = {
                        "timestamp": entry.get("timestamp"),
                        "src_ip": entry.get("src_ip", "localhost"),
                        "command": cmd,
                        "label": result
                    }
                    requests.post(FLASK_URL, json=data)
                    print(f"[+] Sent log: {data}")
            except Exception as e:
                print(f"[!] Error: {e}")

if __name__ == "__main__":
    tail_log()
