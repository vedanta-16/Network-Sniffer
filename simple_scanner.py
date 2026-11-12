
import os
import csv
import time
from datetime import datetime
from collections import Counter

from scapy.all import sniff, IP, IPv6, TCP, UDP, ICMP, ARP


# ==========================================
# CONFIGURATION
# ==========================================

INTERFACE = "wlan0"       # Change to your network interface
PACKET_COUNT = 50         # Maximum packets to capture
REPORT_DIR = "reports"

os.makedirs(REPORT_DIR, exist_ok=True)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

csv_file = os.path.join(
    REPORT_DIR, f"packet_scan_{timestamp}.csv"
)

txt_file = os.path.join(
    REPORT_DIR, f"packet_scan_{timestamp}.txt"
)


# ==========================================
# GLOBAL VARIABLES
# ==========================================

packets_data = []
protocol_count = Counter()
unique_ips = set()

total_traffic = 0
capture_start = None
capture_end = None


# ==========================================
# PACKET ANALYSIS
# ==========================================

def analyze_packet(packet):

    global total_traffic, capture_start, capture_end

    packet_time = time.time()

    if capture_start is None:
        capture_start = packet_time

    capture_end = packet_time

    source = "Unknown"
    destination = "Unknown"

    protocol = "Other"
    src_port = "-"
    dst_port = "-"
    flags = "-"

    # IPv4 information
    if IP in packet:
        source = packet[IP].src
        destination = packet[IP].dst

    # IPv6 information
    elif IPv6 in packet:
        source = packet[IPv6].src
        destination = packet[IPv6].dst

    # ARP information
    if ARP in packet:
        source = packet[ARP].psrc
        destination = packet[ARP].pdst
        protocol = "ARP"

    # TCP information
    if TCP in packet:
        protocol = "TCP"
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
        flags = str(packet[TCP].flags)

    # UDP information
    elif UDP in packet:
        protocol = "UDP"
        src_port = packet[UDP].sport
        dst_port = packet[UDP].dport

    # ICMP information
    elif ICMP in packet:
        protocol = "ICMP"

    # Other IP traffic
    elif IPv6 in packet and protocol == "Other":
        protocol = "IPv6"

    elif IP in packet and protocol == "Other":
        protocol = "IP"

    # Packet size
    packet_size = len(packet)

    # Update statistics
    total_traffic += packet_size
    protocol_count[protocol] += 1

    if source != "Unknown":
        unique_ips.add(source)

    if destination != "Unknown":
        unique_ips.add(destination)

    # Store packet information
    record = {
        "Time": datetime.fromtimestamp(packet_time).strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "Source": source,
        "Destination": destination,
        "Protocol": protocol,
        "Source Port": src_port,
        "Destination Port": dst_port,
        "TCP Flags": flags,
        "Packet Size": packet_size
    }

    packets_data.append(record)

    # Terminal output
    print(
        f"[{len(packets_data):03}] "
        f"{source} -> {destination} | "
        f"{protocol} | "
        f"Ports: {src_port} -> {dst_port} | "
        f"Flags: {flags} | "
        f"Size: {packet_size} bytes"
    )


# ==========================================
# GENERATE NETWORK SUMMARY
# ==========================================

def generate_summary():

    duration = 0

    if capture_start is not None and capture_end is not None:
        duration = capture_end - capture_start

    summary = []

    summary.append("")
    summary.append("=" * 50)
    summary.append("          NETWORK SCAN SUMMARY")
    summary.append("=" * 50)

    summary.append(
        f"Total packets captured : {len(packets_data)}"
    )

    summary.append(
        f"Total traffic captured : {total_traffic:,} bytes"
    )

    summary.append(
        f"Unique IP addresses    : {len(unique_ips)}"
    )

    summary.append(
        f"Capture duration       : {duration:.2f} seconds"
    )

    summary.append("")
    summary.append("PROTOCOL DISTRIBUTION")
    summary.append("-" * 35)

    if protocol_count:
        for protocol, count in sorted(protocol_count.items()):
            summary.append(
                f"{protocol:<15}: {count}"
            )
    else:
        summary.append("No protocols detected.")

    summary.append("=" * 50)

    return "\n".join(summary)


# ==========================================
# SAVE CSV REPORT
# ==========================================

def save_csv():

    if not packets_data:
        return

    with open(csv_file, "w", newline="") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=packets_data[0].keys()
        )

        writer.writeheader()
        writer.writerows(packets_data)


# ==========================================
# SAVE TXT REPORT
# ==========================================

def save_txt():

    with open(txt_file, "w") as file:

        file.write("NETWORK PACKET ANALYZER REPORT\n")
        file.write("=" * 50 + "\n")

        file.write(
            f"Report generated: {datetime.now()}\n"
        )

        file.write(
            f"Network interface: {INTERFACE}\n"
        )

        file.write(
            f"Packet limit: {PACKET_COUNT}\n"
        )

        file.write(generate_summary())

        file.write("\n\nPACKET DETAILS\n")
        file.write("-" * 50 + "\n")

        for record in packets_data:

            file.write(
                f"Time: {record['Time']} | "
                f"Source: {record['Source']} | "
                f"Destination: {record['Destination']} | "
                f"Protocol: {record['Protocol']} | "
                f"Source Port: {record['Source Port']} | "
                f"Destination Port: {record['Destination Port']} | "
                f"TCP Flags: {record['TCP Flags']} | "
                f"Size: {record['Packet Size']} bytes\n"
            )


# ==========================================
# SAVE ALL REPORTS
# ==========================================

def save_reports():

    if not packets_data:

        print("\nNo packets captured.")
        print("No reports generated.")

        return

    save_csv()
    save_txt()

    print(generate_summary())

    print("\nREPORTS GENERATED SUCCESSFULLY")
    print("-" * 50)
    print(f"CSV Report : {csv_file}")
    print(f"TXT Report : {txt_file}")


# ==========================================
# MAIN FUNCTION
# ==========================================

def main():

    print("\n")
    print("=" * 50)
    print("          NETWORK PACKET ANALYZER")
    print("=" * 50)

    print(f"Network Interface : {INTERFACE}")
    print(f"Packet Limit      : {PACKET_COUNT}")
    print("Capture Filter    : ip or ip6 or arp")

    print("\nStarting packet capture...")
    print("Press Ctrl+C to stop capture.\n")

    try:

        sniff(
            iface=INTERFACE,
            filter="ip or ip6 or arp",
            prn=analyze_packet,
            count=PACKET_COUNT,
            store=False
        )

    except KeyboardInterrupt:

        print("\n\nCapture stopped by user.")

    except Exception as error:

        print(f"\nCapture error: {error}")

    finally:

        save_reports()


# ==========================================
# PROGRAM ENTRY POINT
# ==========================================

if __name__ == "__main__":
    main()
