#!/usr/bin/env python3

import socket
import sys

def scan_ports(target):
    print(f"Ah, a new target! Initiating port scan on {target}. Let's uncover their secrets, shall we?")
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: Open")
        sock.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./PortReaper.py <target>")
        sys.exit(1)
    target = sys.argv[1]
    scan_ports(target)
    print("Port scan complete. The secrets of the network are now yours to explore! Mwahaha!")
