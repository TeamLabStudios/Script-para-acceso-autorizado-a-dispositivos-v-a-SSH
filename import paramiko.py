import paramiko

def ssh_connect(host, port, username, password, command):
    try:
        # Crear un cliente SSH
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Conectar al dispositivo
        ssh.connect(host, port, username, password)
        print(f"Conectado a {host}")
        
        # Ejecutar un comando
        stdin, stdout, stderr = ssh.exec_command(command)
        print("Salida del comando:")
        print(stdout.read().decode())
        
        # Cerrar la conexión
        ssh.close()
    except Exception as e:
        print(f"Error al conectar a {host}: {e}")

# Configuración de los dispositivos
devices = [
    {"host": "192.168.1.10", "port": 22, "username": "admin", "password": "admin123"},
    {"host": "192.168.1.11", "port": 22, "username": "admin", "password": "admin123"}
]

# Comando a ejecutar
command = "uname -a"

# Conectar a cada dispositivo y ejecutar el comando
for device in devices:
    ssh_connect(
        host=device["host"],
        port=device["port"],
        username=device["username"],
        password=device["password"],
        command=command
    )
