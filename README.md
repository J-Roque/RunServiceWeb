Website Monitor Script
Este repositorio contiene un script que verifica el estado de un sitio web y ejecuta ciertas acciones cuando el sitio no está disponible. Si el sitio presenta algún problema, el script enviará notificaciones a usuarios específicos y ejecutará un script BAT.

Requisitos
Python 3.x
Paquete requests
Puedes instalar requests ejecutando el siguiente comando:

bash
Copiar código
pip install requests
Uso
Este script monitorea continuamente el estado de un sitio web especificado y toma medidas en caso de detectar caídas. Aquí están los pasos que sigue el script:

Verificación del Sitio Web: El script realiza solicitudes a la URL indicada.
Ejecución de Script BAT: Si el sitio no está disponible o hay un error, se ejecuta un archivo BAT ubicado en C:\websuteRun.bat. Puedes modificar la ruta según sea necesario.
Notificaciones: Envía notificaciones a usuarios específicos de máquinas remotas a través del comando msg.
Variables Importantes
url: La URL del sitio web que deseas monitorear. Actualmente, está configurada como https://facebook.com.
targets: Lista de tuplas que contienen la IP y el nombre del usuario objetivo para enviar notificaciones.
Ejecución del Script
El script ejecuta un bucle infinito para verificar continuamente el estado del sitio web. Para detener la ejecución, simplemente interrumpe el proceso (Ctrl + C).

python
Copiar código
# Configura la URL de tu sitio
url = "https://facebook.com"
# Lista de tuplas con IPs y nombres de usuario objetivo
targets = [
    ("ip", "nombre equipo"),
]

while True:
    check_website(url, targets)
    # Pausar 1 minuto (60 segundos) antes de la próxima verificación
    time.sleep(60)
Personalización
Cambia url por la URL de tu sitio web.
Modifica targets con las IPs y nombres de usuario a los que deseas enviar notificaciones.
Actualiza la ruta bat_file_path con la ubicación de tu script BAT.
Notas
Este script está diseñado para ejecutarse en entornos Windows, ya que usa el comando msg y ejecuta scripts .bat.
Es posible que se necesiten permisos administrativos para enviar mensajes a otros equipos.
Contribuciones
¡Las contribuciones son bienvenidas! Si tienes alguna idea para mejorar el script o encuentras un error, abre un "Issue" o envía un "Pull Request".

Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para obtener más detalles.
