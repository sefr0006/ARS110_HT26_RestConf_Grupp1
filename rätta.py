import requests
import json
from login import username, password

AUTH = (username, password)
HEADERS = { 'Accept': 'application/yang-data+json', 'Content-Type': 'application/yang-data+json' }

serial_bw_correct = 64
serial_clockrate_correct = "64000"

mask_24 = "255.255.255.0"

R1_ips_correct = { "Loopback0":   "172.16.1.1", "Loopback48":  "192.168.48.1", "Loopback49":  "192.168.49.1", "Loopback50":  "192.168.50.1", "Loopback51":  "192.168.51.1", "Loopback70":  "192.168.70.1", "Serial0/1/0": "172.16.12.1" }

R1_eigrp_nets_correct = ["172.16.0.0", "192.168.48.0", "192.168.49.0", "192.168.50.0", "192.168.51.0", "192.168.70.0"]

#R1_live_lo = { "Loopback0":   "172.16.1.1", "Loopback48":  "192.168.48.1", "Loopback49":  "192.168.49.1", "Loopback50":  "192.168.50.1", "Loopback51":  "192.168.51.1", "Loopback70":  "192.168.70.1", }

ips = "ietf-interfaces:interfaces/interface"
serial_010 = "Cisco-IOS-XE-native:native/interface/Serial=0%2F1%2F0"
serial_011 = "Cisco-IOS-XE-native:native/interface/Serial=0%2F1%2F1"
eigrp = "Cisco-IOS-XE-native:native/router/Cisco-IOS-XE-eigrp:router-eigrp"
ospf = "Cisco-IOS-XE-native:native/router/Cisco-IOS-XE-ospf:router-ospf"
native = "Cisco-IOS-XE-native:native/interface"

def get_data(router_addr, path):
    url = f"https://{router_addr}/restconf/data/{path}"
    response = requests.request("GET", url, auth=AUTH, headers=HEADERS,  verify=False)
    return response.json()

with open("R1_ietf-interfaces.json") as f:
    R1_ips = json.load(f)
# R1_ips = get_data("10.1.1.1", ips)
# R1_serial = get_data("10.1.1.1", serial_010)
# R1_eigrp = get_data("10.1.1.1", eigrp)
# R1_native = get_data("10.1.1.1", native)

R1_ips_live = {}
R1_masks_live = {}
print('R1\n')
for intf in R1_ips["ietf-interfaces:interface"]:
    addrs = intf.get("ietf-ip:ipv4", {})
    for addr in addrs.get("address", []):
        R1_ips_live[intf["name"]] = addr["ip"]
        R1_masks_live[intf["name"]] = addr["netmask"]

for interface in R1_ips_correct:
    live_ip = R1_ips_live.get(interface)
    correct_ip = R1_ips_correct[interface]
    live_mask = R1_masks_live.get(interface)
    if live_ip == correct_ip and live_mask == mask_24:
        print("OK   ", interface, live_ip, live_mask)
    else:
        print(f"NO    {interface} {live_ip} {live_mask}\n      expected {correct_ip} {mask_24}\n")

# serial_bw_live = R1_serial["Cisco-IOS-XE-native:Serial"][0]["bandwidth"]["kilobits"]
# if serial_bw_live == serial_bw_correct:
#     print(f"OK, bandwidth {serial_bw_live} kb/s")
# else:
#     print(f"NOT OK, bandwidth {serial_bw_live} kb/s, correct is {serial_bw_correct} kb/s ")
#
# serial_clockrate_live = R1_serial["Cisco-IOS-XE-native:Serial"][0]["Cisco-IOS-XE-serial:DCE-mode-config"]["clock"]["rate"]
# if serial_clockrate_live == serial_clockrate_correct:
#     print(f"OK, clockrate {serial_clockrate_live}")
# else:
#     print(f"NOT OK, clockrate {serial_clockrate_live}, correct is {serial_clockrate_correct}")
#
# url = "https://10.1.1.1/restconf/data/Cisco-IOS-XE-native:native/router/Cisco-IOS-XE-eigrp:router-eigrp/"
#
# response = requests.request("GET", url, auth=AUTH, headers=HEADERS,  verify=False)
#
# print(response.text)
#
#
# url = "https://10.1.1.2/restconf/data/ietf-interfaces:interfaces/interface"
#
# response = requests.request("GET", url, auth=AUTH, headers=HEADERS,  verify=False)
#
# print(response.text)
#
#
# url = "https://10.1.1.2/restconf/data/Cisco-IOS-XE-native:native/interface/Serial=0%2F1%2F0"
# response = requests.request("GET", url, auth=AUTH, headers=HEADERS,  verify=False)
#
# print(response.text)
#
#
# url = "https://10.1.1.2/restconf/data/Cisco-IOS-XE-native:native/interface/Serial=0%2F1%2F1"
#
# response = requests.request("GET", url, auth=AUTH, headers=HEADERS,  verify=False)
#
# print(response.text)
# response = requests.request("GET", url, auth=AUTH, headers=HEADERS,  verify=False)
#
# print(response.text)
#
#
# url = "https://10.1.1.2/restconf/data/Cisco-IOS-XE-native:native/router/Cisco-IOS-XE-ospf:router-ospf"
# response = requests.request("GET", url, auth=AUTH, headers=HEADERS,  verify=False)
#
# print(response.text)
#
#
# url = "https://10.1.1.2/restconf/data/Cisco-IOS-XE-native:native/interface"
#
# print(response.text)
#
#
# url = "https://10.1.1.3/restconf/data/Cisco-IOS-XE-native:native/interface"
# response = requests.request("GET", url, auth=AUTH, headers=HEADERS,  verify=False)
#
# print(response.text)
#
#
# url = "https://10.1.1.3/restconf/data/Cisco-IOS-XE-native:native/interface/Serial=0%2F1%2F1"
#
# response = requests.request("GET", url, auth=AUTH, headers=HEADERS,  verify=False)
#
# print(response.text)
#
#
# url = "https://10.1.1.3/restconf/data/Cisco-IOS-XE-native:native/router/Cisco-IOS-XE-ospf:router-ospf"
#
# response = requests.request("GET", url, auth=AUTH, headers=HEADERS,  verify=False)
#
# print(response.text)
