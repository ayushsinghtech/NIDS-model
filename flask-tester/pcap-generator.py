from scapy.all import *

# This is where the PCAP will be saved in the mounted volume
output_path = "/output/test.pcap"

# Simulate a TCP flow
packets = []

packets.append(IP(src="10.0.0.1", dst="10.0.0.2") / TCP(sport=12345, dport=80, flags="S", seq=1000))
packets.append(IP(src="10.0.0.2", dst="10.0.0.1") / TCP(sport=80, dport=12345, flags="SA", seq=2000, ack=1001))
packets.append(IP(src="10.0.0.1", dst="10.0.0.2") / TCP(sport=12345, dport=80, flags="A", seq=1001, ack=2001))
packets.append(IP(src="10.0.0.1", dst="10.0.0.2") / TCP(sport=12345, dport=80, flags="PA", seq=1001, ack=2001) / Raw(load="GET / HTTP/1.1\r\nHost: example.com\r\n\r\n"))
packets.append(IP(src="10.0.0.2", dst="10.0.0.1") / TCP(sport=80, dport=12345, flags="PA", seq=2001, ack=1039) / Raw(load="HTTP/1.1 200 OK\r\nContent-Length: 2\r\n\r\nOK"))
packets.append(IP(src="10.0.0.1", dst="10.0.0.2") / TCP(sport=12345, dport=80, flags="A", seq=1039, ack=2026))

# Save to PCAP
wrpcap(output_path, packets)

print(f"✅ PCAP file written to {output_path}")
