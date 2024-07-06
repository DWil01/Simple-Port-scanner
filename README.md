# Simple Port Scanner

Welcome to the Simple Port Scanner project! This tool is designed to perform a basic scan of a range of ports on a specified target host, whether it's an IP address or a domain name. 

## Overview

The Simple Port Scanner is a Python-based utility that leverages threading to efficiently scan multiple ports on a given target. It attempts to connect to each port in the specified range and reports whether the port is open or closed. This tool can be useful for network administrators, security professionals, and anyone interested in learning more about network security and port scanning techniques.

## Features

- **Target Resolution:** Converts domain names to IP addresses for scanning.
- **Threading for Efficiency:** Utilizes multiple threads to perform port scans concurrently, significantly speeding up the process.
- **Port Status Reporting:** Indicates whether each port is open, closed, or filtered, including any socket errors encountered during the scan.

## How It Works

1. **Input Handling:** The user is prompted to enter the target host (IP address or domain name).
2. **Target Resolution:** The tool resolves the target host to its corresponding IP address.
3. **Port Scanning:** 
    - A range of ports (1 to 1024) is queued for scanning.
    - Multiple threads are spawned to handle the port scanning concurrently.
    - Each thread attempts to connect to a port and reports its status (open, closed, or filtered).
4. **Results Display:** After all ports have been scanned, the results are displayed to the user.

## Usage

To use the Simple Port Scanner, follow these steps:

1. **Ensure Python is installed:** This tool requires Python 3 to run. You can download and install Python from [python.org](https://www.python.org/).

2. **Install Required Modules:** The tool uses the `socket`, `threading`, and `queue` modules, which are part of the Python standard library. No additional installations are needed.

3. **Run the Script:** Execute the script from the command line.

```bash
python3 simple_port_scanner.py
```

4. **Enter Target Host:** When prompted, enter the IP address or domain name of the target host.

```bash
Enter the target host: scanme.nmap.org
```

5. **View Results:** The script will display the status of each port (open or closed) and any socket errors encountered.

## Example Output

```plaintext
Enter the target host: scanme.nmap.org
Starting scan on host: 45.33.32.156
Port 22: Closed or filtered (Error code: 111)
Port 80: Open
Port 443: Open
...
Open ports on 45.33.32.156: [80, 443]
```

## Note

- This tool requires administrative or root privileges to run effectively, especially when scanning lower-numbered ports.
- Ensure you have permission to scan the target host to avoid legal or ethical issues.

## Contributing

We welcome contributions! If you have suggestions for improvements or additional features, please feel free to open an issue or submit a pull request.
