import json
import requests
api_url = "http://localhost:58000/api/v1/host"

headers={"X-Auth-Token": input("Ticket (el que dio 01_get-ticket.py): ")}

resp = requests.get(api_url, headers=headers, verify=False)

print("Request status: ", resp.status_code)

response_json = resp.json()
print (response_json)
print()
print()
hosts = response_json["response"]

for host in hosts:
    print(host["hostName"], "\t", host["hostIp"], "\t", host["hostMac"], "\t", host["connectedInterfaceName"])