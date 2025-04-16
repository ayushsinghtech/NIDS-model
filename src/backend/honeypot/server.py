from flask import Flask, request, jsonify
import csv

app = Flask(__name__)

@app.route('/log', methods=['POST'])
def receive_log():
    data = request.json
    print(f"[LOG] {data}")
    with open("honeypot_labeled_data.csv", "a") as f:
        f.write(f"{data['timestamp']},{data['src_ip']},{data['command']},{data['label']}\n")
    return jsonify({"status": "received"}), 200

if __name__ == "__main__":
    app.run(port=5000)
