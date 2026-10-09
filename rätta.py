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

R2_ips_correct = { "Loopback0":   "172.16.2.1", "Loopback100": "172.16.100.1", "Serial0/1/0": "172.16.12.2", "Serial0/1/1": "172.16.23.2" }

R2_eigrp_nets_correct = ["172.16.0.0"]

R2_eigrp_redistribute_correct = { "process-id": 1, "bandwidth": 10000, "delay": 100, "reliability": 255, "load": 1, "mtu": 1500 }

R2_ospf_redistribute_correct = { "as": 1 }

R3_ips_correct = { "Loopback0":   "172.16.3.1", "Loopback8":   "192.168.8.1", "Loopback9":   "192.168.9.1", "Loopback10":  "192.168.10.1", "Loopback11":  "192.168.11.1", "Loopback20":  "192.168.20.1", "Loopback25":  "192.168.25.1", "Loopback30":  "192.168.30.1", "Loopback35":  "192.168.35.1", "Loopback40":  "192.168.40.1", "Serial0/1/1": "172.16.23.3" }


ips = "ietf-interfaces:interfaces/interface"
serials = "Cisco-IOS-XE-native:native/interface/Serial"
eigrp = "Cisco-IOS-XE-native:native/router/Cisco-IOS-XE-eigrp:router-eigrp"
ospf = "Cisco-IOS-XE-native:native/router/Cisco-IOS-XE-ospf:router-ospf"
native = "Cisco-IOS-XE-native:native/interface"

def get_data(router_addr, path):
    url = f"https://{router_addr}/restconf/data/{path}"
    response = requests.request("GET", url, auth=AUTH, headers=HEADERS,  verify=False)
    return response.json()

def check_ips(ips, ips_correct):
    ips_live = {}
    masks_live = {}
    for intf in ips["ietf-interfaces:interface"]:
        addrs = intf.get("ietf-ip:ipv4", {})
        for addr in addrs.get("address", []):
            ips_live[intf["name"]] = addr["ip"]
            masks_live[intf["name"]] = addr["netmask"]

    for interface in ips_correct:
        live_ip = ips_live.get(interface)
        correct_ip = ips_correct[interface]
        live_mask = masks_live.get(interface)
        if live_ip == correct_ip and live_mask == mask_24:
            print(f"OK    {interface} {live_ip} {live_mask}")
        else:
            print(f"NO    {interface} {live_ip} {live_mask}\n      expected {correct_ip} {mask_24}\n")

def check_serial(serial_live, dce):
    name = "Serial " + serial_live["name"]
    if dce:
        name = name + " (DCE)"
    print(name)
    serial_bw_live = serial_live["bandwidth"]["kilobits"]
    if serial_bw_live == serial_bw_correct:
        print(f"OK    bandwidth {serial_bw_live} kb/s")
    else:
        print(f"NO    bandwidth {serial_bw_live} kb/s\n      expected {serial_bw_correct} kb/s\n")
    if dce:
        serial_clockrate_live = serial_live["Cisco-IOS-XE-serial:DCE-mode-config"]["clock"]["rate"]
        if serial_clockrate_live == serial_clockrate_correct:
            print(f"OK    clockrate {serial_clockrate_live} b/s")
        else:
            print(f"NO    clockrate {serial_clockrate_live} b/s\n      expected {serial_clockrate_correct} b/s\n")

def check_eigrp(eigrp, nets_correct):
    nets_live = []
    for net in eigrp["Cisco-IOS-XE-eigrp:router-eigrp"]["eigrp"]["classic-mode"][0]["network"]["address"]:
        nets_live.append(net["ipv4-address"])
    for net in nets_correct:
        if net in nets_live:
            print(f"OK    {net}")
        else:
            print(f"NO    {net}\n      missing\n")

with open("R1_ietf-interfaces.json") as f:
    R1_ips = json.load(f)
# R1_ips = get_data("10.1.1.1", ips)
# R1_serials = get_data("10.1.1.1", serials)
# R1_eigrp = get_data("10.1.1.1", eigrp)
# R1_native = get_data("10.1.1.1", native)
print('R1\n')
print('R1 IP CHECK\n')
check_ips(R1_ips, R1_ips_correct)

with open("R1_serials.json") as f:
    R1_serials = json.load(f)
print('\nR1 SERIAL BW CR and DCE\n')
for serial in R1_serials["Cisco-IOS-XE-native:Serial"]:
    if serial["name"] == "0/1/0":
        check_serial(serial, True)

with open("R1_eigrp.json") as f:
    R1_eigrp = json.load(f)
print('\nR1 EIGRP NETWORKS\n')
check_eigrp(R1_eigrp, R1_eigrp_nets_correct)
# url = "https://10.1.1.2/restconf/data/ietf-interfaces:interfaces/interface"
with open("R2_ietf-interfaces.json") as f:
    R2_ips = json.load(f)
# R2_ips = get_data("10.1.1.1", ips)
# R2_serials = get_data("10.1.1.1", serials)
# R2_eigrp = get_data("10.1.1.1", eigrp)
# R2_native = get_data("10.1.1.1", native)
print('\nR2\n')
print('R2 IP CHECK\n')
check_ips(R2_ips, R2_ips_correct)

with open("R2_serials.json") as f:
    R2_serials = json.load(f)
print('\nR2 SERIAL BW CR and DCE\n')
for serial in R2_serials["Cisco-IOS-XE-native:Serial"]:
    if serial["name"] == "0/1/0":
        check_serial(serial, False)
    if serial["name"] == "0/1/1":
        check_serial(serial, True)

with open("R2_eigrp.json") as f:
    R2_eigrp = json.load(f)
print('\nR2 EIGRP NETWORKS\n')
check_eigrp(R2_eigrp, R2_eigrp_nets_correct)


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
