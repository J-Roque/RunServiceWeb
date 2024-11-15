import requests
import os
import time

def send_notification(message, target_ip, target_user):
    # Formato del comando msg
    command = f'msg {target_user} /SERVER:{target_ip} "{message}"'
    print(f'Ejecutando comando: {command}')  # Para depuración
    os.system(command)

def execute_bat_script():
    bat_file_path = r'C:\scripconexionsshservidor.bat'  # Cambia esta ruta por la correcta
    print(f'Ejecutando script BAT en {bat_file_path}')
    os.system(bat_file_path)

def check_website(url, targets):
    try:
        response = requests.get(url)
        if response.ok:
            print('El sitio está funcionando.')
        else:
            error_message = f'Error {response.status_code}: Caída de Facebook'
            print('El sitio está caído. Código de estado:', response.status_code)
            execute_bat_script()  # Ejecuta el script cuando el sitio esté caído
            for target_ip, target_user in targets:
                send_notification(error_message, target_ip, target_user)
    except requests.RequestException as e:
        print('El sitio está caído. Error:', e)
        error_message = f'Caída de faceboo: Error en la conexión'
        execute_bat_script()  # Ejecuta el script en caso de error
        for target_ip, target_user in targets:
            send_notification(error_message, target_ip, target_user)

# Cambia la URL por la de tu página web
url = "https://facebook.com"
# Lista de tuplas con IPs y nombres de usuario
targets = [
    ("ip", "nombre equipo"),
 
]
# Bucle infinito
while True:
    check_website(url, targets)
    # Pausar 1 minuto (60 segundos) antes de la próxima verificación
    time.sleep(60)
