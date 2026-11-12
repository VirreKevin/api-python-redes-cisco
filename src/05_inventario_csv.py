# Script propio - Grupo 5 - TP4
# Arma un inventario de la red a partir de la API del Network Controller
# y lo guarda en dos archivos CSV (dispositivos y hosts).
import csv
import getpass
from collections import Counter

import requests
from tabulate import tabulate

BASE = "http://localhost:58000/api/v1"

# 1) Pedir el ticket (la contraseña se pregunta, no está escrita en el código)
clave = getpass.getpass("Contraseña del controlador: ")
resp = requests.post(BASE + "/ticket", json={"username": "cisco", "password": clave})
ticket = resp.json()["response"]["serviceTicket"]
headers = {"X-Auth-Token": ticket}
print("Ticket obtenido:", ticket)

# 2) Dispositivos de red -> inventario_dispositivos.csv
dispositivos = requests.get(BASE + "/network-device", headers=headers).json()["response"]
filas_disp = []
for d in dispositivos:
    filas_disp.append([
        d.get("hostname", "(sin nombre)"),
        d.get("type", "-"),
        d.get("managementIpAddress", "-"),
        d.get("platformId", "-"),
        d.get("softwareVersion", "-"),
        d.get("collectionStatus", "-"),
    ])
cab_disp = ["Hostname", "Tipo", "IP de gestion", "Plataforma", "Version", "Estado"]

with open("inventario_dispositivos.csv", "w", newline="", encoding="utf-8") as f:
    escritor = csv.writer(f)
    escritor.writerow(cab_disp)
    escritor.writerows(filas_disp)

# 3) Hosts -> inventario_hosts.csv
hosts = requests.get(BASE + "/host", headers=headers).json()["response"]
filas_host = []
for h in hosts:
    filas_host.append([
        h.get("hostName", "-"),
        h.get("hostType", "-"),
        h.get("hostIp", "-"),
        h.get("hostMac", "-"),
        h.get("connectedNetworkDeviceName", "-"),
        h.get("connectedInterfaceName", "-"),
        h.get("pingStatus", "-"),
    ])
cab_host = ["Hostname", "Tipo", "IP", "MAC", "Conectado a", "Interfaz", "Ping"]

with open("inventario_hosts.csv", "w", newline="", encoding="utf-8") as f:
    escritor = csv.writer(f)
    escritor.writerow(cab_host)
    escritor.writerows(filas_host)

# 4) Resumen por pantalla
print("\nDispositivos de red:")
print(tabulate(filas_disp, headers=cab_disp, tablefmt="rst"))
print("\nHosts:")
print(tabulate(filas_host, headers=cab_host, tablefmt="rst"))

estados = Counter(fila[5] for fila in filas_disp)
print("\nEquipos por estado:")
for estado, cantidad in estados.items():
    print(" -", estado, ":", cantidad)

print("\nArchivos generados: inventario_dispositivos.csv ({} filas) e inventario_hosts.csv ({} filas)".format(len(filas_disp), len(filas_host)))