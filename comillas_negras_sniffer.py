from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
import datetime

def ethical_disclaimer():
    print("=====================================================")
    print("  Comillas Negras - Network Packet Analyzer")
    print("  Use this tool for ethical and educational purposes.")
    print("  Unauthorized monitoring is illegal and unethical.")
    print("=====================================================\n")

def process_packet(packet):
    print(f"\n[{datetime.datetime.now().strftime('%H:%M:%S')}] Packet captured:")

    if IP in packet:
        ip_layer = packet[IP]
        print(f"  From: {ip_layer.src}")
        print(f"  To:   {ip_layer.dst}")
        print(f"  Protocol: {ip_layer.proto}", end='')

        if TCP in packet:
            print(" (TCP)")
        elif UDP in packet:
            print(" (UDP)")
        elif ICMP in packet:
            print(" (ICMP)")
        else:
            print(" (Other)")

        if Raw in packet:
            payload = packet[Raw].load
            print(f"  Payload: {str(payload[:100])}...")  # Show only first 100 chars
    else:
        print("  Non-IP Packet")

def main():
    ethical_disclaimer()
    try:
        print("Sniffing... Press Ctrl+C to stop.\n")
        sniff(prn=process_packet, store=False)
    except KeyboardInterrupt:
        print("\nSniffing stopped.")
    except PermissionError:
        print("Permission denied: Try running as administrator/root.")

if __name__ == "__main__":
    main()
