from scapy.all import sniff

def packet_callback(packet):
    """Callback function to process captured packets."""
    print(packet.summary())  # Print packet details

if __name__ == "__main__":
    print("Starting Packet Sniffer...")
    sniff(prn=packet_callback, store=False)
