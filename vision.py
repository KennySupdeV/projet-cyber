from scapy.all import ARP, Ether, srp
import pandas as pd

def scan_arp(ip_range):
    # Create an ARP request packet
    arp_request = ARP(pdst=ip_range)
    # Create an Ethernet frame
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    # Combine ARP request packet and Ethernet frame
    arp_request_packet = ether / arp_request

    # Send the packet and capture the response
    result = srp(arp_request_packet, timeout=2, verbose=False)[0]

    # Extract the IP and MAC addresses from the response
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

def main():
    ip_range = "192.168.1.1/24"  # Replace with your IP range
    devices = scan_arp(ip_range)

    # Display the results
    if devices:
        print("IP\t\t\tMAC Address")
        print("-----------------------------------------")
        for device in devices:
            print(f"{device['ip']}\t\t{device['mac']}")
    else:
        print("Aucun périphérique trouvé.")

    # Save the results to a CSV file
    df = pd.DataFrame(devices)
    df.to_csv("arp_scan_results.csv", index=False)

if __name__ == "__main__":
    main()
