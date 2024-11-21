import paramiko
import paramiko

# Configuración
SERVER = "172.12.1.1"  # Dirección del servidor (IP o hostname)
PORT = 22                 # Puerto SSH (modifica si es necesario)
USERNAME = "wiskas"       # Usuario SSH
SSH_PASSWORD = "wiskas$"  # Contraseña SSH
SUDO_PASSWORD = "wiskas$"  # Contraseña para sudo


def ssh_connect_and_execute(server, port, username, ssh_password, sudo_password):
    """
    Conéctate a un servidor SSH
    """
    try:
        # Crear cliente SSH
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Conectar al servidor
        ssh.connect(hostname=server, port=port, username=username, password=ssh_password)
        
        # Abrir una sesión interactiva
        channel = ssh.invoke_shell()

        # Vaciar el canal para ignorar cualquier mensaje inicial
        while channel.recv_ready():
            channel.recv(1024)

        # Elevar privilegios con sudo su
        channel.send("sudo su\n")
          # if sudo_password:
        #     channel.recv(1024)  # Leer solicitud de contraseña
        #     channel.send(f"{sudo_password}\n")

        # Esperar hasta que tengamos acceso root
        while True:
            output = channel.recv(1024).decode('utf-8')
            if "root@" in output:  # Verifica si ya tienes acceso root
                break

        # Vaciar el canal nuevamente antes de ejecutar comandos
        while channel.recv_ready():
            channel.recv(1024)

        # Ejecutar comandos después de 'sudo su'
        commands = ["cd ..","cd administrator/NodeJS/wiskas","clear","pm2 status","pm2 start wiskasnuwevo"]
        for cmd in commands:
            channel.send(f"{cmd}\n")
            output = ""
            while True:
                data = channel.recv(1024).decode('utf-8')
                output += data
                if data.endswith("# ") or data.endswith("$ "):  # Prompt indica comando terminado
                    break
            # Filtrar el prompt final y mostrar solo la salida del comando
            lines = output.splitlines()
            # Filtrar líneas vacías o solo espacios en blanco
            command_output = "\n".join([line for line in lines[1:-1] if line.strip() != ""])
            print(command_output)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        ssh.close()

if __name__ == "__main__":
    ssh_connect_and_execute(SERVER, PORT, USERNAME, SSH_PASSWORD, SUDO_PASSWORD)