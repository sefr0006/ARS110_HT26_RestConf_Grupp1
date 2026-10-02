import requests
import json
from login import username, password

AUTH = (username, password)

url = "https://10.1.1.1/restconf/data/ietf-interfaces:interfaces/interface/"

payload = json.dumps({
  "ietf-interfaces:interface": [
    {
      "name": "GigabitEthernet0",
      "type": "iana-if-type:ethernetCsmacd",
      "enabled": True,
      "ietf-ip:ipv4": {
        "address": [
          {
            "ip": "10.1.1.1",
            "netmask": "255.255.255.0"
          }
        ]
      },
      "ietf-ip:ipv6": {}
    },
    {
      "name": "GigabitEthernet0/0/0",
      "type": "iana-if-type:ethernetCsmacd",
      "enabled": False,
      "ietf-ip:ipv4": {},
      "ietf-ip:ipv6": {}
    },
    {
      "name": "GigabitEthernet0/0/1",
      "type": "iana-if-type:ethernetCsmacd",
      "enabled": False,
      "ietf-ip:ipv4": {},
      "ietf-ip:ipv6": {}
    },
    {
      "name": "Loopback0",
      "type": "iana-if-type:softwareLoopback",
      "enabled": True,
      "ietf-ip:ipv4": {
        "address": [
          {
            "ip": "172.16.1.1",
            "netmask": "255.255.255.0"
          }
        ]
      },
      "ietf-ip:ipv6": {}
    },
    {
      "name": "Loopback48",
      "type": "iana-if-type:softwareLoopback",
      "enabled": True,
      "ietf-ip:ipv4": {
        "address": [
          {
            "ip": "192.168.48.1",
            "netmask": "255.255.255.0"
          }
        ]
      },
      "ietf-ip:ipv6": {}
    },
    {
      "name": "Loopback49",
      "type": "iana-if-type:softwareLoopback",
      "enabled": True,
      "ietf-ip:ipv4": {
        "address": [
          {
            "ip": "192.168.49.1",
            "netmask": "255.255.255.0"
          }
        ]
      },
      "ietf-ip:ipv6": {}
    },
    {
      "name": "Loopback50",
      "type": "iana-if-type:softwareLoopback",
      "enabled": True,
      "ietf-ip:ipv4": {
        "address": [
          {
            "ip": "192.168.50.1",
            "netmask": "255.255.255.0"
          }
        ]
      },
      "ietf-ip:ipv6": {}
    },
    {
      "name": "Loopback51",
      "type": "iana-if-type:softwareLoopback",
      "enabled": True,
      "ietf-ip:ipv4": {
        "address": [
          {
            "ip": "192.168.51.1",
            "netmask": "255.255.255.0"
          }
        ]
      },
      "ietf-ip:ipv6": {}
    },
    {
      "name": "Loopback70",
      "type": "iana-if-type:softwareLoopback",
      "enabled": True,
      "ietf-ip:ipv4": {
        "address": [
          {
            "ip": "192.168.70.1",
            "netmask": "255.255.255.0"
          }
        ]
      },
      "ietf-ip:ipv6": {}
    }
  ]
})
headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json'
}

response = requests.request("PATCH", url, auth=AUTH, headers=headers, data=payload, verify=False)

print(response.text)


url = "https://10.1.1.1/restconf/data/Cisco-IOS-XE-native:native/interface/Serial/"

payload = json.dumps({
  "Cisco-IOS-XE-native:Serial": [
    {
      "name": "0/1/0",
      "bandwidth": {
        "kilobits": 64
      },
      "ip": {
        "address": {
          "primary": {
            "address": "172.16.12.1",
            "mask": "255.255.255.0"
          }
        }
      },
      "Cisco-IOS-XE-serial:DCE-mode-config": {
        "clock": {
          "rate": "64000"
        }
      }
    },
    {
      "name": "0/1/1",
      "shutdown": [
       False 
      ]
    }
  ]
})
headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json'
}

response = requests.request("PATCH", url, auth=AUTH, headers=headers, data=payload, verify=False)

print(response.text)


url = "https://10.1.1.1/restconf/data/Cisco-IOS-XE-native:native/router/Cisco-IOS-XE-eigrp:router-eigrp/"

payload = json.dumps({
  "Cisco-IOS-XE-eigrp:router-eigrp": {
    "eigrp": {
      "classic-mode": [
        {
          "autonomous-system": 1,
          "network": {
            "address": [
              {
                "ipv4-address": "172.16.0.0"
              },
              {
                "ipv4-address": "192.168.48.0"
              },
              {
                "ipv4-address": "192.168.49.0"
              },
              {
                "ipv4-address": "192.168.50.0"
              },
              {
                "ipv4-address": "192.168.51.0"
              },
              {
                "ipv4-address": "192.168.70.0"
              }
            ]
          }
        }
      ]
    }
  }
})
headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json'
}

response = requests.request("PATCH", url, auth=AUTH, headers=headers, data=payload, verify=False)

print(response.text)


url = "https://10.1.1.2/restconf/data/ietf-interfaces:interfaces/interface"

payload = json.dumps({
  "ietf-interfaces:interface": [
    {
      "name": "GigabitEthernet0",
      "type": "iana-if-type:ethernetCsmacd",
      "enabled": True,
      "ietf-ip:ipv4": {
        "address": [
          {
            "ip": "10.1.1.2",
            "netmask": "255.255.255.0"
          }
        ]
      },
      "ietf-ip:ipv6": {}
    },
    {
      "name": "GigabitEthernet0/0/0",
      "type": "iana-if-type:ethernetCsmacd",
      "enabled": False,
      "ietf-ip:ipv4": {},
      "ietf-ip:ipv6": {}
    },
    {
      "name": "GigabitEthernet0/0/1",
      "type": "iana-if-type:ethernetCsmacd",
      "enabled": False,
      "ietf-ip:ipv4": {},
      "ietf-ip:ipv6": {}
    },
    {
      "name": "Loopback0",
      "type": "iana-if-type:softwareLoopback",
      "enabled": True,
      "ietf-ip:ipv4": {
        "address": [
          {
            "ip": "172.16.2.1",
            "netmask": "255.255.255.0"
          }
        ]
      },
      "ietf-ip:ipv6": {}
    },
    {
      "name": "Loopback100",
      "type": "iana-if-type:softwareLoopback",
      "enabled": True,
      "ietf-ip:ipv4": {
        "address": [
          {
            "ip": "172.16.100.1",
            "netmask": "255.255.255.0"
          }
        ]
      },
      "ietf-ip:ipv6": {}
    }
  ]
})
headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json'
}

response = requests.request("PATCH", url, auth=AUTH, headers=headers, data=payload, verify=False)

print(response.text)


url = "https://10.1.1.2/restconf/data/Cisco-IOS-XE-native:native/interface/Serial/"

payload = json.dumps({
  "Cisco-IOS-XE-native:Serial": [
    {
      "name": "0/1/0",
      "bandwidth": {
        "kilobits": 64
      },
      "ip": {
        "address": {
          "primary": {
            "address": "172.16.12.2",
            "mask": "255.255.255.0"
          }
        }
      }
    },
    {
      "name": "0/1/1",
      "bandwidth": {
        "kilobits": 64
      },
      "ip": {
        "address": {
          "primary": {
            "address": "172.16.23.2",
            "mask": "255.255.255.0"
          }
        }
      },
      "Cisco-IOS-XE-serial:DCE-mode-config": {
        "clock": {
          "rate": "64000"
        }
      }
    }
  ]
})
headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json'
}

response = requests.request("PATCH", url, auth=AUTH, headers=headers, data=payload, verify=False)

print(response.text)


url = "https://10.1.1.2/restconf/data/Cisco-IOS-XE-native:native/router/Cisco-IOS-XE-eigrp:router-eigrp"

payload = json.dumps({
  "Cisco-IOS-XE-eigrp:router-eigrp": {
    "eigrp": {
      "classic-mode": [
        {
          "autonomous-system": 1,
          "network": {
            "address": [
              {
                "ipv4-address": "172.16.0.0"
              }
            ]
          },
          "redistribute": {
            "ospf": [
              {
                "process-id": 1,
                "metric": {
                  "bandwidth": 10000,
                  "delay": 100,
                  "reliability": 255,
                  "load": 1,
                  "mtu": 1500
                }
              }
            ]
          }
        }
      ]
    }
  }
})
headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json'
}

response = requests.request("PATCH", url, auth=AUTH, headers=headers, data=payload, verify=False)

print(response.text)


url = "https://10.1.1.2/restconf/data/Cisco-IOS-XE-native:native/router/Cisco-IOS-XE-ospf:router-ospf"

payload = json.dumps({
  "Cisco-IOS-XE-ospf:router-ospf": {
    "ospf": {
      "process-id": [
        {
          "id": 1,
          "network": [
            {
              "ip": "172.16.23.0",
              "wildcard": "0.0.0.255",
              "area": 0
            },
            {
              "ip": "172.16.100.0",
              "wildcard": "0.0.0.255",
              "area": 10
            }
          ],
          "redistribute": {
            "eigrp": [
              {
                "as": 1
              }
            ]
          },
          "summary-address": [
            {
              "ip": "192.168.48.0",
              "mask": "255.255.252.0"
            }
          ]
        }
      ]
    }
  }
})
headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json'
}

response = requests.request("PATCH", url, auth=AUTH, headers=headers, data=payload, verify=False)

print(response.text)


url = "https://10.1.1.3/restconf/data/ietf-interfaces:interfaces/interface"

payload = json.dumps({
  "ietf-interfaces:interface": [
    {
      "name": "Loopback0",
      "type": "iana-if-type:softwareLoopback",
      "enabled": True,
      "ietf-ip:ipv4": {
        "address": [
          {
            "ip": "172.16.3.1",
            "netmask": "255.255.255.0"
          }
        ]
      },
      "ietf-ip:ipv6": {}
    },
    {
      "name": "Loopback8",
      "type": "iana-if-type:softwareLoopback",
      "enabled": True,
      "ietf-ip:ipv4": {
        "address": [
          {
            "ip": "172.16.8.1",
            "netmask": "255.255.255.0"
          }
        ]
      },
      "ietf-ip:ipv6": {}
    },
    {
      "name": "Loopback9",
      "type": "iana-if-type:softwareLoopback",
      "enabled": True,
      "ietf-ip:ipv4": {
        "address": [
          {
            "ip": "172.16.9.1",
            "netmask": "255.255.255.0"
          }
        ]
      },
      "ietf-ip:ipv6": {}
    },
    {
      "name": "Loopback10",
      "type": "iana-if-type:softwareLoopback",
      "enabled": True,
      "ietf-ip:ipv4": {
        "address": [
          {
            "ip": "172.16.10.1",
            "netmask": "255.255.255.0"
          }
        ]
      },
      "ietf-ip:ipv6": {}
    },
    {
      "name": "Loopback11",
      "type": "iana-if-type:softwareLoopback",
      "enabled": True,
      "ietf-ip:ipv4": {
        "address": [
          {
            "ip": "172.16.11.1",
            "netmask": "255.255.255.0"
          }
        ]
      },
      "ietf-ip:ipv6": {}
    },
    {
      "name": "Loopback20",
      "type": "iana-if-type:softwareLoopback",
      "enabled": True,
      "ietf-ip:ipv4": {
        "address": [
          {
            "ip": "172.16.20.1",
            "netmask": "255.255.255.0"
          }
        ]
      },
      "ietf-ip:ipv6": {}
    },
    {
      "name": "Loopback25",
      "type": "iana-if-type:softwareLoopback",
      "enabled": True,
      "ietf-ip:ipv4": {
        "address": [
          {
            "ip": "172.16.25.1",
            "netmask": "255.255.255.0"
          }
        ]
      },
      "ietf-ip:ipv6": {}
    },
    {
      "name": "Loopback30",
      "type": "iana-if-type:softwareLoopback",
      "enabled": True,
      "ietf-ip:ipv4": {
        "address": [
          {
            "ip": "172.16.30.1",
            "netmask": "255.255.255.0"
          }
        ]
      },
      "ietf-ip:ipv6": {}
    },
    {
      "name": "Loopback35",
      "type": "iana-if-type:softwareLoopback",
      "enabled": True,
      "ietf-ip:ipv4": {
        "address": [
          {
            "ip": "172.16.35.1",
            "netmask": "255.255.255.0"
          }
        ]
      },
      "ietf-ip:ipv6": {}
    },
    {
      "name": "Loopback40",
      "type": "iana-if-type:softwareLoopback",
      "enabled": True,
      "ietf-ip:ipv4": {
        "address": [
          {
            "ip": "172.16.40.1",
            "netmask": "255.255.255.0"
          }
        ]
      },
      "ietf-ip:ipv6": {}
    }
  ]
})
headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json'
}

response = requests.request("PATCH", url, auth=AUTH, headers=headers, data=payload, verify=False)

print(response.text)


url = "https://10.1.1.3/restconf/data/Cisco-IOS-XE-native:native/interface/Serial/"

payload = json.dumps({
  "Cisco-IOS-XE-native:Serial": [
    {
      "name": "0/1/1",
      "bandwidth": {
        "kilobits": 64
      },
      "ip": {
        "address": {
          "primary": {
            "address": "172.16.23.3",
            "mask": "255.255.255.0"
          }
        }
      }
    },
    {
      "name": "0/1/0"
    }
  ]
})
headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json'
}

response = requests.request("PATCH", url, auth=AUTH, headers=headers, data=payload, verify=False)

print(response.text)


url = "https://10.1.1.3/restconf/data/Cisco-IOS-XE-native:native/router/Cisco-IOS-XE-ospf:router-ospf"

payload = json.dumps({
  "Cisco-IOS-XE-ospf:router-ospf": {
    "ospf": {
      "process-id": [
        {
          "id": 1,
          "network": [
            {
              "ip": "192.168.0.0",
              "wildcard": "0.0.255.255",
              "area": 0
            },
            {
              "ip": "172.16.0.0",
              "wildcard": "0.0.255.255",
              "area": 0
            },
            {
              "ip": "192.168.8.0",
              "wildcard": "0.0.3.255",
              "area": 20
            }
          ],
          "summary-address": [
            {
              "ip": "192.168.8.0",
              "mask": "255.255.252.0"
            }
          ]
        }
      ]
    }
  }
})
headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json'
}

response = requests.request("PATCH", url, auth=AUTH, headers=headers, data=payload, verify=False)

print(response.text)
