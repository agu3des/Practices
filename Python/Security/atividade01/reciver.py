from scapy.all import sniff, UDP
import sys

def packet_handler(packet):
    packet.show()

def main():

    sniff(filter = "udp port 12345", prn=packet_handler)

if __name__ == "__main__":
    main()