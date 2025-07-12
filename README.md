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
