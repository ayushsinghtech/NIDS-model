import requests

with open("E:/NIDS-model/flask-tester/test.pcap", "rb") as f:
    pcap_data = f.read()

response = requests.post(
    "http://localhost:5000/api/predict",
    data=pcap_data,
    headers={"Content-Type": "application/octet-stream"}
)

print("Status Code:", response.status_code)
print("Raw Response:")
print(response.text)

try:
    print("Parsed JSON:")
    print(response.json())
except Exception as e:
    print("⚠️ JSON parse failed:", e)
