import scapy.all as scapy
from scapy_http import http

# Listening for packets
def packet_listener(interface):
    scapy.sniff(iface = interface,store = False,prn = packet_analyzer)
    #prn = Callback function

#Analyze the packets
def packet_analyzer(packet):
    #packet.show()

    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            print(packet[scapy.Raw].load)

packet_listener("eth0")