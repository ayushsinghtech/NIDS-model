import sys

def block_ip(ip):
    with open("malicious_ips.txt", "a") as f:
        f.write(ip + "\n")
    print(f"[+] IP {ip} logged.")

if __name__ == "__main__":
    ip = sys.argv[1]
    block_ip(ip)
