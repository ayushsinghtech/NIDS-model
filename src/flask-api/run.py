# # run.py
# from app import create_app

# app = create_app()

# if __name__ == "__main__":
#     # Run the Flask app on 0.0.0.0 so it's accessible from Docker (if needed)
#     app.run(debug=True, host="0.0.0.0", port=5000)

import subprocess
import os

def run_cicflowmeter(input_pcap, output_csv):
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)

    cmd = ["cicflowmeter", "-f", input_pcap, "-c", output_csv]
    print(f"Running command: {' '.join(cmd)}")

    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print("[✅ SUCCESS] CICFlowMeter completed.")
            print(result.stdout)
        else:
            print("[❌ ERROR] CICFlowMeter failed:")
            print(result.stderr)
    except FileNotFoundError:
        print("[🚫 ERROR] 'cicflowmeter' not found. Make sure it's installed and in your PATH.")

# Usage
run_cicflowmeter("test.pcap", "output_csv/output.csv")


