import socket
from concurrent.futures import ThreadPoolExecutor

TARGET = "scanme.nmap.org"
START_PORT = 1
END_PORT = 100
TIMEOUT = 0.5

print(f"\n[+] Scanning {TARGET} for open TCP ports...\n")

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(TIMEOUT)
        if s.connect_ex((TARGET, port)) == 0:
            print(f"[OPEN] Port {port}")
        s.close()
    except:
        pass

with ThreadPoolExecutor(max_workers=50) as executor:
    executor.map(scan_port, range(START_PORT, END_PORT + 1))

print("\n[✓] Scan completed.")