import socket
import threading
from queue import Queue

def port_scan(target, ports):
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"Unable to resolve host: {target}")
        return

    print(f"Starting scan on host: {target_ip}")

    queue = Queue()
    open_ports = []

    def worker():
        while not queue.empty():
            port = queue.get()
            result = scan_port(target_ip, port)
            if result:
                open_ports.append(port)
            queue.task_done()

    for port in ports:
        queue.put(port)

    threads = []
    for _ in range(100):
        thread = threading.Thread(target=worker)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    if open_ports:
        print(f"Open ports on {target_ip}: {open_ports}")
    else:
        print(f"No open ports found on {target_ip}.")

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        sock.close()

        if result == 0:
            print(f"Port {port}: Open")
            return True
        else:
            print(f"Port {port}: Closed or filtered (Error code: {result})")
            return False
    except socket.error as e:
        print(f"Socket error on port {port}: {e}")
        return False

if __name__ == "__main__":
    target_host = input("Enter the target host: ").strip()
    ports_to_scan = range(1, 1025)  # Scanning ports 1 to 1024

    port_scan(target_host, ports_to_scan)
