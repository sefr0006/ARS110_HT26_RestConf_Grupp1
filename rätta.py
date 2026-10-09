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

R2_ospf_summary_correct = ["192.168.48.0 255.255.252.0"]

R2_eigrp_redistribute_correct = { "process-id": 1, "bandwidth": 10000, "delay": 100, "reliability": 255, "load": 1, "mtu": 1500 }

R2_ospf_redistribute_correct = { "as": 1 }

R2_ospf_nets_correct = ["172.16.23.0 0.0.0.255 area 0", "172.16.100.0 0.0.0.255 area 10"]

R2_ospf_p2p_correct = ["Loopback100"]

R3_ips_correct = { "Loopback0":   "172.16.3.1", "Loopback8":   "192.168.8.1", "Loopback9":   "192.168.9.1", "Loopback10":  "192.168.10.1", "Loopback11":  "192.168.11.1", "Loopback20":  "192.168.20.1", "Loopback25":  "192.168.25.1", "Loopback30":  "192.168.30.1", "Loopback35":  "192.168.35.1", "Loopback40":  "192.168.40.1", "Serial0/1/1": "172.16.23.3" }

R3_ospf_nets_correct = ["172.16.0.0 0.0.255.255 area 0", "192.168.0.0 0.0.255.255 area 0", "192.168.8.0 0.0.3.255 area 20"]

R3_ospf_range_correct = ["area 20 range 192.168.8.0 255.255.252.0"]

R3_ospf_p2p_correct = ["Loopback0", "Loopback8", "Loopback9", "Loopback10", "Loopback11", "Loopback20", "Loopback25", "Loopback30", "Loopback35", "Loopback40"]

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

def check_eigrp_redist(eigrp, redistribute_correct):
    redist_live = eigrp["Cisco-IOS-XE-eigrp:router-eigrp"]["eigrp"]["classic-mode"][0]["redistribute"]["ospf"][0]
    if redist_live["process-id"] == redistribute_correct["process-id"]:
        print(f"OK      redistribute ospf {redist_live["process-id"]} (process-id)")
    else:
        print(f"NO      redistribute ospf process-id {redist_live["process-id"]}(process-id)\n     expected {redistribute_correct["process-id"]}")
    for metric in ["bandwidth", "delay", "reliability", "load", "mtu"]:
        metric_live = redist_live["metric"][metric]
        if metric_live == redistribute_correct[metric]:
            print(f"OK      {metric} {metric_live}")
        else:
            print(f"NO      {metric} {metric_live}\n       expected {redistribute_correct[metric]}\n")

def check_ospf(ospf, nets_correct):
    nets_live = []
    for net in ospf["Cisco-IOS-XE-ospf:router-ospf"]["ospf"]["process-id"][0]["network"]:
        nets_live.append(f"{net["ip"]} {net["wildcard"]} area {net["area"]}")
    for net in nets_correct:
        if net in nets_live:
            print(f"OK    {net}")
        else:
            print(f"NO    {net}\n      missing\n")

def check_ospf_p2p(native, ospf_p2p_correct):
    ospf_p2p_live=[]
    for lo in native["Cisco-IOS-XE-native:interface"]["Loopback"]:
        if "Cisco-IOS-XE-ospf:router-ospf" in lo["ip"]:
            network = lo["ip"]["Cisco-IOS-XE-ospf:router-ospf"]["ospf"]["network"]
            if "point-to-point" in network:
                ospf_p2p_live.append(f"Loopback{lo["name"]}")
    for lo in ospf_p2p_correct:
        if lo in ospf_p2p_live:
            print(f"OK  {lo} point-to-point")
        else:
            print(f"NO  {lo} point-to-point\n       missing\n")

with open("R1_ietf-interfaces.json") as f:
    R1_ips = json.load(f)
# R1_ips = get_data("10.1.1.1", ips)
print('R1\n')
print('R1 IP CHECK\n')
check_ips(R1_ips, R1_ips_correct)

with open("R1_serials.json") as f:
    R1_serials = json.load(f)
# R1_serials = get_data("10.1.1.1", serials)
print('\nR1 SERIAL BW CR and DCE\n')
for serial in R1_serials["Cisco-IOS-XE-native:Serial"]:
    if serial["name"] == "0/1/0":
        check_serial(serial, True)

with open("R1_eigrp.json") as f:
    R1_eigrp = json.load(f)
# R1_eigrp = get_data("10.1.1.1", eigrp)
print('\nR1 EIGRP NETWORKS\n')
check_eigrp(R1_eigrp, R1_eigrp_nets_correct)

with open("R2_ietf-interfaces.json") as f:
    R2_ips = json.load(f)
# R2_ips = get_data("10.1.1.2", ips)
with open("R2_native-interface.json") as f:
    R2_native = json.load(f)
# R2_native = get_data("10.1.1.2", native)
print('\nR2\n')
print('R2 IP CHECK\n')
check_ips(R2_ips, R2_ips_correct)

with open("R2_serials.json") as f:
    R2_serials = json.load(f)
# R2_serials = get_data("10.1.1.2", serials)
print('\nR2 SERIAL BW CR and DCE\n')
for serial in R2_serials["Cisco-IOS-XE-native:Serial"]:
    if serial["name"] == "0/1/0":
        check_serial(serial, False)
    if serial["name"] == "0/1/1":
        check_serial(serial, True)

with open("R2_eigrp.json") as f:
    R2_eigrp = json.load(f)
# R2_eigrp = get_data("10.1.1.2", eigrp)
print('\nR2 EIGRP NETWORKS\n')
check_eigrp(R2_eigrp, R2_eigrp_nets_correct)
check_eigrp_redist(R2_eigrp, R2_eigrp_redistribute_correct)

with open("R2_ospf.json") as f:
    R2_ospf = json.load(f)
# R2_ospf = get_data("10.1.1.2", ospf)
print('\nR2 OSPF NETWORKS\n')
check_ospf(R2_ospf, R2_ospf_nets_correct)

print('\nR2 OSPF SUMMARY\n')
summary_live = []
for summary in R2_ospf["Cisco-IOS-XE-ospf:router-ospf"]["ospf"]["process-id"][0]["summary-address"]:
    summary_live.append(f"{summary['ip']} {summary['mask']}")
for summary in R2_ospf_summary_correct:
    if summary in summary_live:
        print(f"OK    {summary}")
    else:
        print(f"NO    {summary}\n      missing\n")

print('\nR2 OSPF REDISTRIBUTE\n')
ospf_redist_live = R2_ospf["Cisco-IOS-XE-ospf:router-ospf"]["ospf"]["process-id"][0]["redistribute"]["eigrp"][0]
if ospf_redist_live == R2_ospf_redistribute_correct:
    print(f"OK    redistribute eigrp {ospf_redist_live['as']}")
else:
    print(f"NO    redistribute eigrp {ospf_redist_live}\n      expected {R2_ospf_redistribute_correct}\n")

print('\nR2 OSPF POINT-TO-POINT\n')
check_ospf_p2p(R2_native, R2_ospf_p2p_correct)

with open("R3_ietf-interfaces.json") as f:
    R3_ips = json.load(f)
# R3_ips = get_data("10.1.1.3", ips)
with open("R3_native-interface.json") as f:
    R3_native = json.load(f)
# R3_native = get_data("10.1.1.3", native)
print('R3\n')
print('R3 IP CHECK\n')
check_ips(R3_ips, R3_ips_correct)

with open("R3_serials.json") as f:
    R3_serials = json.load(f)
# R3_serials = get_data("10.1.1.3", serials)
print('\nR3 SERIAL BW CR and DCE\n')
for serial in R3_serials["Cisco-IOS-XE-native:Serial"]:
    if serial["name"] == "0/1/1":
        check_serial(serial, False)

with open("R3_ospf.json") as f:
    R3_ospf = json.load(f)
# R3_ospf = get_data("10.1.1.3", ospf)
print('\nR3 OSPF NETWORKS\n')
check_ospf(R3_ospf, R3_ospf_nets_correct)

print('\nR3 OSPF AREA RANGE\n')
range_live = []
for area in R3_ospf["Cisco-IOS-XE-ospf:router-ospf"]["ospf"]["process-id"][0]["area"]:
    for r in area["ipv4-range"]["range"]:
        range_live.append(f"area {area['area-id']} range {r['ip']} {r['mask']}")
for r in R3_ospf_range_correct:
    if r in range_live:
        print(f"OK    {r}")
    else:
        print(f"NO    {r}\n      missing\n")

print('\nR3 OSPF POINT-TO-POINT\n')
check_ospf_p2p(R3_native, R3_ospf_p2p_correct)

