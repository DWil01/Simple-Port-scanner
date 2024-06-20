import socket

def port_scan(target, ports):
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"Unable to resolve host: {target}")
        return

    print(f"Starting scan on host: {target_ip}")

    for port in ports:
        scan_port(target_ip, port)

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))

        if result == 0:
            print(f"Port {port}: Open")
        sock.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

if __name__ == "__main__":
    target_host = input("Enter the target host: ")
    ports_to_scan = range(1, 1025)  # Scanning ports 1 to 1024

    port_scan(target_host, ports_to_scan)
