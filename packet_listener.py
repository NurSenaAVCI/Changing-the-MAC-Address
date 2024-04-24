import scapy.all as scapy
from scapy_http import http
def listen_packet(interface):

    scapy.sniff(iface=interface, store=False, prn=analyze_packet)
    #pnr = The function where we will process the packages

def analyze_packet(packet):
    packet.show()