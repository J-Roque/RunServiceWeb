# Website Monitor Script

Este repositorio contiene un script que verifica el estado de un sitio web y ejecuta ciertas acciones cuando el sitio no está disponible. Si el sitio presenta algún problema, el script enviará notificaciones a usuarios específicos y ejecutará un script BAT.

## Requisitos

- **Python 3.x**
- **Paquete `requests`**

Puedes instalar el paquete `requests` ejecutando:

```bash
pip install requests
```

## Descripción

El script realiza lo siguiente:

1. **Verificación del Sitio Web**: Realiza solicitudes a una URL especificada para verificar su disponibilidad.
2. **Ejecución de Script BAT**: Si el sitio no responde o hay un error, se ejecuta un archivo BAT definido.
3. **Notificaciones**: Envía mensajes a usuarios de equipos remotos utilizando el comando `msg`.

## Configuración

### Variables Principales

- `url`: La URL del sitio web que deseas monitorear. Por defecto está configurada como `https://facebook.com`.
- `targets`: Lista de tuplas con las IPs y nombres de usuario objetivo para enviar notificaciones.

### Ejecución del Script

El script ejecuta un bucle infinito para verificar continuamente el estado del sitio web. Para detener la ejecución, usa `Ctrl + C`.

```python
# Configura la URL de tu sitio
url = "https://facebook.com"
# Lista de tuplas con IPs y nombres de usuario objetivo
targets = [
    ("ip", "nombre equipo"),
]

while True:
    check_website(url, targets)
    # Pausa de 1 minuto (60 segundos) antes de la siguiente verificación
    time.sleep(60)
```

## Personalización

- Cambia `url` por la URL que deseas monitorear.
- Actualiza `targets` con las IPs y nombres de usuario de los destinatarios de las notificaciones.
- Modifica la ruta `bat_file_path` para apuntar a tu script BAT específico.

## Notas

- Este script está diseñado para ejecutarse en entornos Windows, ya que utiliza el comando `msg` y ejecuta scripts `.bat`.
- Puede ser necesario contar con permisos administrativos para enviar mensajes a otros equipos.

## Contribuciones

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar el script o encuentras algún error, abre un **Issue** o envía un **Pull Request**.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para obtener más detalles.
