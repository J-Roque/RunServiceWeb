import requests
import os
import time

def send_notification(message, target_ip, target_user):
    """
    Envía una notificación utilizando el comando `msg` a un usuario en una máquina remota.

    Args:
        message (str): El mensaje que se enviará.
        target_ip (str): La IP de destino del equipo al que se enviará el mensaje.
        target_user (str): El nombre de usuario del destinatario.
    """
    # Construye el comando para enviar un mensaje a través de `msg`
    command = f'msg {target_user} /SERVER:{target_ip} "{message}"'
    print(f'Ejecutando comando: {command}')  # Muestra el comando para depuración
    os.system(command)

def execute_bat_script():
    """
    Ejecuta un archivo BAT específico para realizar acciones automáticas cuando el sitio web esté caído.
    """
    # Ruta del archivo BAT que se ejecutará
    bat_file_path = r'C:\websuteRun.bat'  # Asegúrate de cambiar esta ruta por la correcta
    print(f'Ejecutando script BAT en {bat_file_path}')
    os.system(bat_file_path)

def check_website(url, targets):
    """
    Verifica el estado de un sitio web e interactúa según el resultado de la verificación.

    Args:
        url (str): La URL del sitio web a verificar.
        targets (list): Lista de tuplas con la IP y el nombre de usuario a los que se enviará la notificación si el sitio falla.
    """
    try:
        # Realiza una solicitud GET al sitio
        response = requests.get(url)
        if response.ok:
            print('El sitio está funcionando correctamente.')
        else:
            # Si el sitio responde pero no de manera exitosa
            error_message = f'Error {response.status_code}: Sitio en estado no funcional'
            print('El sitio está caído. Código de estado:', response.status_code)
            execute_bat_script()  # Ejecuta el script BAT en caso de falla
            for target_ip, target_user in targets:
                send_notification(error_message, target_ip, target_user)
    except requests.RequestException as e:
        # Si hay un problema al conectarse al sitio
        print('El sitio está caído. Error:', e)
        error_message = f'Caída del sitio: Error en la conexión ({e})'
        execute_bat_script()  # Ejecuta el script en caso de error
        for target_ip, target_user in targets:
            send_notification(error_message, target_ip, target_user)

# Ejemplo de uso
if __name__ == "__main__":
    # URL a verificar (cambiar según tus necesidades)
    url = "https://facebook.com"
    # Lista de tuplas (IP, nombre de usuario) para enviar notificaciones
    targets = [
        ("192.168.1.10", "usuario1"),  # Cambia la IP y el nombre de usuario según tu entorno
        ("192.168.1.11", "usuario2")
    ]
    # Bucle infinito para verificar el estado del sitio cada minuto
    while True:
        check_website(url, targets)
        # Pausa de 60 segundos antes de la próxima verificación
        time.sleep(60)
