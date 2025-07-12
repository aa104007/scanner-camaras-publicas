#!/usr/bin/env python3


import shodan
import sys
import time
from colorama import init, Fore

init(autoreset=True)

API_KEY = "COLOCA_TU_API_KEY_AQUI"  # ← Reemplaza esto con tu clave real

# Inicializar API
api = shodan.Shodan(API_KEY)

# Lista de tecnologías/cámaras comunes en Shodan
tipos_camaras = {
    1:  "webcamxp",
    2:  "webcam 7",
    3:  "ip camera",
    4:  "NetSurveillance",
    5:  "DVR",
    6:  "RTSP",
    7:  "MJPEG",
    8:  "JPEG",
    9:  "Axis",
    10: "Hikvision",
    11: "D-Link",
    12: "TP-LINK",
    13: "AVTech",
    14: "Mobotix",
    15: "Panasonic",
    16: "Vivotek",
    17: "GeoVision",
    18: "Samsung",
    19: "Foscam",
    20: "Sony"
}


def buscar_camaras(tipo, pais_iso):
    try:
        query = f"{tipo} country:{pais_iso}"
        print(Fore.GREEN + f"\n[+] Buscando: '{query}'\n")
        resultados = api.search(query)

        print(Fore.YELLOW + f"[+] Dispositivos encontrados: {resultados['total']}\n")

        for servicio in resultados['matches']:
            ip = servicio['ip_str']
            puerto = servicio['port']
            org = servicio.get('org', 'Desconocido')
            print(Fore.RED + f"[{ip}:{puerto}] - {org}")
            time.sleep(0.1)

    except shodan.APIError as e:
        print(Fore.RED + f"[!] Error en la API: {e}")
        sys.exit(1)


def menu():
    print(Fore.CYAN + "\n=== Buscar cámaras con SHODAN ===\n")
    print(Fore.WHITE + "Tipos de cámaras disponibles:")
    for key in sorted(tipos_camaras.keys()):
        print(f"{key}) {tipos_camaras[key]}")
    try:
        opcion = int(input(Fore.YELLOW + "\nSelecciona el número del tipo de cámara: "))
        if opcion not in tipos_camaras:
            raise ValueError("Opción no válida")

        tipo = tipos_camaras[opcion]
        pais = input(Fore.YELLOW + "Ingresa el código ISO del país (ej. US): ").strip().upper()
        buscar_camaras(tipo, pais)
    except ValueError as ve:
        print(Fore.RED + f"Error: {ve}")
        sys.exit(1)


if __name__ == "__main__":
    menu()
            