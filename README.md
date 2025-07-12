# scanner-camaras-publicas
Una herramienta educativa en Python que utiliza la API de Shodan para buscar cámaras IP y dispositivos similares expuestos públicamente en internet.

> ⚠️ **Este proyecto es solo para fines educativos y de auditoría ética. El uso indebido puede ser ilegal. El autor no se hace responsable del uso que se le dé.**

---

## 🚀 Características

- Búsqueda por país usando código ISO (ej: `US`, `MX`, `ES`, etc.)
- Selección de tipo de cámara (Axis, Hikvision, MJPEG, RTSP, etc.)
- Muestra dirección IP, puerto y proveedor del dispositivo
- Compatible con cuentas gratuitas y premium de Shodan

---

## 📦 Requisitos

- Python 3.x
- Shodan API Key (gratuita o premium)
- Librerías Python:
  - `shodan`
  - `colorama`

Instálalas con:

```bash
pip install shodan colorama
```
## 🛠 Instalación
Clona este repositorio:

```bash
git clone https://github.com/tuusuario/scanner-camaras-publicas.git
cd scanner-camaras-publicas
```

Abre el archivo scanner_camaras.py y reemplaza esta línea:
``` python
API_KEY = "COLOCA_TU_API_KEY_AQUI"
```
…con tu clave real de Shodan.

Instala las dependencias si no lo has hecho:

```bash
pip install shodan colorama
```
🚀 Uso
Ejecuta el script desde la terminal:

```bash
python3 scanner_camaras.py
```
Verás un menú como este:

```r

=== Buscar cámaras con SHODAN ===

Tipos de cámaras disponibles:
1) webcamxp
2) webcam 7
3) ip camera
4) NetSurveillance
5) DVR
6) RTSP
7) MJPEG
8) JPEG
9) Axis
10) Hikvision
...

Selecciona el número del tipo de cámara: 10
Ingresa el código ISO del país (ej. US, MX, ES): SV
```
Luego mostrará los dispositivos encontrados:

```csharp

[+] Buscando: 'Hikvision country:SV'
[+] Dispositivos encontrados: 34

[192.0.2.101:554] - Proveedor ABC SV
[192.0.2.110:554] - Proveedor CACHIMBON SV
...
```
🔍 Tipos de cámaras soportadas
Este script puede detectar cámaras IP y sistemas relacionados basados en múltiples tecnologías. Algunos ejemplos:

webcamxp
webcam 7
ip camera
NetSurveillance
DVR
RTSP
MJPEG
JPEG
Axis
Hikvision
D-Link
TP-LINK
AVTech
Mobotix
Panasonic
Vivotek
GeoVision
Samsung
Foscam
Sony

🧪 Ejemplo de ejecución completa
```bash
$ python3 scanner_camaras.py

=== Buscar cámaras con SHODAN ===

Tipos de cámaras disponibles:
1) webcamxp
2) ip camera
3) RTSP
...

Selecciona el número del tipo de cámara: 3
Ingresa el código ISO del país (ej. US): SV

[+] Buscando: 'RTSP country:SV'
[+] Dispositivos encontrados: 15

[192.0.2.101:554] - Proveedor XYZ SV
[192.0.2.110:554] - Red de Cámaras Públicas
...
```

🛡️ Aviso legal
Este software está destinado exclusivamente para:

Fines educativos
Investigación académica
Auditorías de seguridad con permiso explícito
El uso sin autorización puede violar leyes locales o internacionales. El autor no se hace responsable del uso indebido del programa.

📄 Licencia
Este proyecto se publica bajo la Licencia MIT. Eres libre de usar, modificar y compartir el código, siempre que mantengas esta nota de atribución.

👨‍💻 Autor
💡 Desarrollado por: Josue Arias

🌐 GitHub: https://github.com/aa104007

📧 Contacto (opcional): josue.arias.sv@gmail.com


