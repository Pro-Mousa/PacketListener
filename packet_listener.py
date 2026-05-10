import scapy.all as scapy
from scapy_http import http

# Listening for packets
def packet_listener(interface):
    scapy.sniff(iface = interface,store = False,prn = packet_analyzer)
    #prn = Callback function

#Analyze the packets
def packet_analyzer(packet):
    packet.show()


packet_listener("eth0")