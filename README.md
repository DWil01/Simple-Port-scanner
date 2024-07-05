Sure! Here's a professional write-up you can add to your GitHub project:

---

# Simple Port Scanner

Welcome to the Simple Port Scanner project! This tool is designed to provide a straightforward and effective way to identify open ports on a given IP address or URL. Developed with both functionality and user experience in mind, this scanner combines the robustness of Scapy with the creativity and personality of the character "Cipher Phantom."

## Features

- **Stealth Scanning**: Utilizes SYN packets to probe ports, aiming to be less detectable by firewalls and intrusion detection systems.
- **Common Ports**: Scans a comprehensive list of commonly used ports, covering essential services and potential vulnerabilities.
- **Randomized Responses**: Injects a touch of unpredictability and wit through randomized responses from Cipher Phantom, making each scan unique and engaging.
- **Error Handling**: Provides clear and descriptive error messages to guide the user through any issues encountered during the scan.

## Usage

To use the Simple Port Scanner, follow these steps:

1. **Clone the Repository**: 
   ```
   git clone https://github.com/DWil01/Simple-Port-scanner.git
   ```

2. **Navigate to the Project Directory**:
   ```
   cd Simple-Port-scanner
   ```

3. **Run the Script**:
   ```
   sudo python3 port_scanner.py
   ```

4. **Enter the Target**: When prompted, enter the IP address or URL you wish to scan.

### Example

```
$ sudo python3 port_scanner.py
Cipher Phantom: Ah, seeker of secrets! Feed me the coordinates—be it a cryptic IP or a labyrinthine URL. Let the dance with shadows begin!
Enter the target IP or URL address: scanme.nmap.org
Cipher Phantom: Commencing scan on scanme.nmap.org... Let's uncover some secrets!
...
Cipher Phantom: The following ports are open on scanme.nmap.org: [22, 80]
Cipher Phantom: Scan complete. Another victory for the shadows! Muahahaha!
```

## How It Works

The Simple Port Scanner uses the Scapy library to send SYN packets to the specified target. If a SYN-ACK response is received, it indicates that the port is open. The scanner then sends a RST packet to close the connection. This method helps in avoiding detection by security systems while providing accurate results.

### Key Components

- **IP and URL Resolution**: The script can resolve URLs to their corresponding IP addresses, ensuring versatility in scanning various targets.
- **User Input Scrubbing**: The input is validated to ensure only valid IP addresses or URLs are accepted, enhancing the reliability of the scan.
- **Randomized Output**: Responses from Cipher Phantom are randomized to maintain engagement and provide a dynamic user experience.

## Conclusion

This Simple Port Scanner is more than just a tool—it's an experience. By combining technical efficacy with creative flair, it aims to offer users an engaging and insightful look into network security. Potential employers will appreciate the balance of technical acumen and innovative presentation.

Feel free to explore, use, and contribute to this project. Let's uncover the secrets that lie hidden in the shadows of the network!

---

This write-up emphasizes both the technical capabilities and the creative aspects of your port scanner, making it appealing to potential employers who are looking for both technical skills and innovative thinking.
