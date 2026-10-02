import requests
import json
from login import username, password

AUTH = (username, password)
HEADERS = { 'Accept': 'application/yang-data+json', 'Content-Type': 'application/yang-data+json' }

#R1_intfs = 
#R2_intfs = 
#R3_intfs =



url = "https://10.1.1.1/restconf/data/ietf-interfaces:interfaces/interface/"
response = requests.request("GET", url, auth=AUTH, headers=HEADERS,  verify=False)

data = response.json()

R1_correct_lo = {}
for intf in data["ietf-interfaces:interface"]:
    ipv4 = intf.get("ietf-ip:ipv4", {})
    for addr in ipv4.get("address", []):
        R1_correct_lo[intf["name"]] = addr["ip"]

R1_live_lo = { "Loopback0":   "172.16.1.1", "Loopback48":  "192.168.48.1", "Loopback49":  "192.168.49.1", "Loopback50":  "192.168.50.1", "Loopback51":  "192.168.51.1", "Loopback70":  "192.168.70.1", }

for name in R1_live_lo:
    if name not in R1_live_lo:
        print("not ok", name, "missing")
    elif R1_correct_lo[name] == R1_live_lo[name]:
        print("ok ", name, R1_correct_lo[name])
    else:
        print("not ok", name, "is", R1_correct_lo[name], "correct is", R1_live_lo[name])

#print(response.text)


url = "https://10.1.1.1/restconf/data/Cisco-IOS-XE-native:native/interface/Serial=0%2F1%2F0"
response = requests.request("GET", url, auth=AUTH, headers=HEADERS,  verify=False)

print(response.text)


url = "https://10.1.1.1/restconf/data/Cisco-IOS-XE-native:native/router/Cisco-IOS-XE-eigrp:router-eigrp/"

response = requests.request("GET", url, auth=AUTH, headers=HEADERS,  verify=False)

print(response.text)


url = "https://10.1.1.2/restconf/data/ietf-interfaces:interfaces/interface"

response = requests.request("GET", url, auth=AUTH, headers=HEADERS,  verify=False)

print(response.text)


url = "https://10.1.1.2/restconf/data/Cisco-IOS-XE-native:native/interface/Serial=0%2F1%2F0"
response = requests.request("GET", url, auth=AUTH, headers=HEADERS,  verify=False)

print(response.text)


url = "https://10.1.1.2/restconf/data/Cisco-IOS-XE-native:native/interface/Serial=0%2F1%2F1"

response = requests.request("GET", url, auth=AUTH, headers=HEADERS,  verify=False)

print(response.text)
response = requests.request("GET", url, auth=AUTH, headers=HEADERS,  verify=False)

print(response.text)


url = "https://10.1.1.2/restconf/data/Cisco-IOS-XE-native:native/router/Cisco-IOS-XE-ospf:router-ospf"
response = requests.request("GET", url, auth=AUTH, headers=HEADERS,  verify=False)

print(response.text)


url = "https://10.1.1.2/restconf/data/Cisco-IOS-XE-native:native/interface"

print(response.text)


url = "https://10.1.1.3/restconf/data/Cisco-IOS-XE-native:native/interface"
response = requests.request("GET", url, auth=AUTH, headers=HEADERS,  verify=False)

print(response.text)


url = "https://10.1.1.3/restconf/data/Cisco-IOS-XE-native:native/interface/Serial=0%2F1%2F1"

response = requests.request("GET", url, auth=AUTH, headers=HEADERS,  verify=False)

print(response.text)


url = "https://10.1.1.3/restconf/data/Cisco-IOS-XE-native:native/router/Cisco-IOS-XE-ospf:router-ospf"

response = requests.request("GET", url, auth=AUTH, headers=HEADERS,  verify=False)

print(response.text)
