
# Basic Network Sniffer

A Python-based Network Sniffer developed using **Scapy** to capture and analyze live network traffic. This project was completed as part of my **CodeAlpha Cybersecurity Internship**.

The tool captures network packets, identifies protocols, extracts packet information, displays results in the terminal, and generates CSV and TXT reports.

## Project Overview

The Basic Network Sniffer helps understand how network communication works by capturing and examining packets transmitted through a selected network interface.

It provides basic packet analysis, protocol identification, traffic statistics, and automatic report generation.

## Features

- Live network packet capture using Scapy.
- Identification of TCP and UDP protocols.
- Detection of ICMP and ARP traffic.
- IPv4 and IPv6 packet identification.
- Source and destination IP address extraction.
- Source and destination port identification.
- TCP flag inspection.
- Protocol-based packet filtering.
- Packet size analysis.
- Unique IP address counting.
- Total captured traffic calculation.
- Capture duration measurement.
- Protocol distribution summary.
- Automatic CSV and TXT report generation.
- Terminal-based packet display.

## Technologies Used

- Python
- Scapy
- Kali Linux
- Linux Terminal
- CSV and TXT Reporting
- Git and GitHub

## Project Structure

```text
NetworkPacketAnalyzer/
│
├── simple_scanner.py
├── git_push.sh
├── README.md
├── .gitignore
│
├── reports/
│   └── .gitkeep
│
└── venv/
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Basic-Network-Sniffer.git
```

### 2. Navigate to the project

```bash
cd Basic-Network-Sniffer
```

### 3. Create a virtual environment

```bash
python3 -m venv venv
```

### 4. Activate the environment

```bash
source venv/bin/activate
```

### 5. Install Scapy

```bash
pip install scapy
```

### 6. Install packet capture dependencies

On Kali Linux:

```bash
sudo apt update
sudo apt install libpcap-dev
```

## Usage

Run the packet sniffer with administrator privileges:

```bash
sudo ./venv/bin/python simple_scanner.py
```

The application starts capturing packets on the configured network interface.

Press `Ctrl+C` to stop packet capture.

**Note:** Update the INTERFACE variable in simple_scanner.py to match your available network interface.

## Generated Reports

The application automatically generates two reports inside the `reports/` directory.

### CSV Report

Contains individual packet information:

- Timestamp
- Source IP
- Destination IP
- Protocol
- Source Port
- Destination Port
- TCP Flags
- Packet Size

### TXT Report

Contains the overall network scan summary:

- Total packets captured
- Total traffic captured
- Unique IP addresses
- Capture duration
- Protocol distribution
- Individual packet details

## Network Scan Summary

Example output (illustrative):

```text
NETWORK SCAN SUMMARY
==========================================

Total packets captured : 50
Total traffic captured : 85420 bytes
Unique IP addresses    : 8
Capture duration       : 12.45 seconds

PROTOCOL DISTRIBUTION
-----------------------------------
ARP            : 5
ICMP           : 3
TCP            : 32
UDP            : 10

==========================================
```

## Learning Outcomes

Through this project, I gained practical experience in:

- Understanding network packet structures.
- Learning TCP/IP communication.
- Identifying different network protocols.
- Using Scapy for packet capture and analysis.
- Understanding source and destination ports.
- Analyzing TCP flags and packet sizes.
- Generating automated network traffic reports.
- Working with Kali Linux and Python.

## Security and Ethical Use

This tool is intended for educational purposes and authorized network analysis only.

- Capture traffic only on your own device or an explicitly authorized network.
- Do not intercept third-party traffic without permission.
- Avoid collecting sensitive information.
- HTTPS/TLS application payloads remain encrypted unless authorized decryption is configured.

## Internship

**Developed as part of the CodeAlpha Cybersecurity Internship.**

## Author

Vedanta Kashelkar

GitHub: https://github.com/YOUR_USERNAME

LinkedIn: Add your LinkedIn profile URL here

---

If you find this project useful, feel free to explore the repository!
