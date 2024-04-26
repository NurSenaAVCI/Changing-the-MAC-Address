import scapy.all as scapy
from scapy_http import http
def listen_packet(interface):

    scapy.sniff(iface=interface, store=False, prn=analyze_packet)
    #pnr = The function where we will process the packages

def analyze_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            print(packet[scapy.Raw].load)

listen_packet("interface")