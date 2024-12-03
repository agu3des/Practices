from scapy.all import send, IP, UDP
import sys

def main():
    m = "Ola Mundo"    
    packet = IP(dst='192.168.1.2') / UDP(dport=12345) / m
    packet.show()
    send(packet)

if __name__ == "__main__":
    main()