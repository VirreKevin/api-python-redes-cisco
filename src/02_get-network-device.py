import json
import requests
api_url = "http://localhost:58000/api/v1/network-device"

headers={"X-Auth-Token": input("Ticket (el que dio 01_get-ticket.py): ")}

resp = requests.get(api_url, headers=headers)

print("Request status: ", resp.status_code)

response_json = resp.json()
print()
print()
print (response_json)
print()
print()
networkDevices = response_json["response"]

for networkDevice in networkDevices:
    print(networkDevice.get("hostname", "(sin nombre)"), "\t", networkDevice.get("platformId", "-"), "\t", networkDevice.get("managementIpAddress", "-"))

