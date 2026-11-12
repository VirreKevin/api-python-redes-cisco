# Entorno de virtualización Python

# Pasos de instalación en Linux:

## 1. Clonación del proyecto

Desde la terminal ejecutar:

**git clone** <URL_del_repositorio> <nombre_de_la_carpeta_de_destino>

Luego ejecutar **cd** <nombre_de_la_carpeta_de_destino>. Esta carpeta será la raíz de nuestro proyecto en Python.

## 2. Creación del entorno virtual

Supongamos que el nombre que le damos al entorno virtual es **cisco**, entonces se creará una carpeta **cisco** con todas las librerías y dependencias necesarias paea nuestro proyecto. 

La manera de realizarlo es la siguiente:

# python3 -m venv <nombre_del_entorno>
Ejemplo: python3 -m venv cisco

Para activar el entorno escribimos **source cisco/bin/activate**, en la carpeta raíz del proyecto. El nombre del entorno virtual aparecerá entre paréntesis ().

## 3. Instalación de las dependencias, en este caso las librerías requests y tabulate

En la carpeta raíz de nuestro proyecto y dentro del entorno virtual escribimos: **pip install -r requirements.txt**

## 4. Selección del intérprete Python para nuestro entorno virtual

<img width="881" height="118" alt="image" src="https://github.com/user-attachments/assets/18c41d8e-d338-48b6-953c-b2499c57319f" />

<img width="736" height="412" alt="image" src="https://github.com/user-attachments/assets/2a795fcd-2cf8-47ef-a5a6-d21e09ce967f" />

Tal como se ve en la figura seleccionamos Python 3.10.12 (cisco) que se mostrará como entorno recomendado.

## 5. Desactivación del entorno virtual

Simplemente escribimos en la línea de comandos: **deactivate**



## Cambios y scripts del Grupo 5 (TP N° 4 – Redes de Computadoras 3643, UNLaM)

Grupo 5, comisión 01-1300. Integrantes: Virreira Kevin Santiago.

Estos scripts consumen la API REST del Network Controller de Packet Tracer (puerto 58000) de la red del TP N° 4.

### Contraseñas
Ningún script lleva la contraseña escrita. Cada uno **la pide por teclado** al ejecutarse (no se ve al escribirla). El usuario del controlador es `cisco`.

### Qué hace cada script (carpeta `src/`)
| Script | Endpoint | Qué hace |
|---|---|---|
| `01_get-ticket.py` | POST /ticket | Pide el ticket de acceso y muestra el estado (201) |
| `02_get-network-device.py` | GET /network-device | Lista los equipos de red (nombre, plataforma, IP). Pide el ticket por teclado |
| `03_get-host.py` | GET /host | Lista los hosts (nombre, IP, MAC, interfaz). Pide el ticket por teclado |
| `04_tabulate.py` | POST /ticket, GET /network-device, GET /host | Muestra equipos y hosts en tablas ordenadas |
| `05_inventario_csv.py` | POST /ticket, GET /network-device, GET /host | **Script propio.** Arma el inventario de la red, lo guarda en `inventario_dispositivos.csv` e `inventario_hosts.csv`, indica a qué switch está conectado cada host y cuántos equipos están en cada estado (Managed / Wrong credential) |

El router ISP **no** está administrado por el controlador (estado *Wrong credential*): no tiene nombre ni datos en el inventario. Los scripts 02 y 04 se modificaron con `.get()` para no fallar con ese equipo.

### Cómo ejecutarlos en Windows (PowerShell)
Con Packet Tracer abierto y la API habilitada (Options > Preferences > Miscellaneous > *Enable External Access for Network Controller REST API*):
```
python -m venv cisco
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\cisco\Scripts\Activate.ps1
pip install -r requirements.txt
python src\01_get-ticket.py
python src\05_inventario_csv.py
```
Los scripts 02 y 03 piden el ticket que muestra el 01