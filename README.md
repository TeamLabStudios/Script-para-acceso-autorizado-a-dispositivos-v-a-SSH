# SSH Network Manager

Este proyecto es un script en Python diseñado para conectarse a dispositivos en una red local mediante SSH y ejecutar comandos autorizados de manera automatizada. Es ideal para la administración de servidores, diagnósticos de red o automatización de tareas.

---

## Características
- Conexión a múltiples dispositivos en la red usando SSH.
- Ejecución de comandos remotos de manera centralizada.
- Uso sencillo con una lista de dispositivos configurada en el código.

---

## Requisitos
Antes de usar este script, asegúrate de cumplir con los siguientes requisitos:

1. **Python 3.x instalado**  
   Descárgalo desde [Python.org](https://www.python.org/).

2. **Biblioteca `paramiko` instalada**  
   Instala la biblioteca ejecutando el siguiente comando:  
   ```bash
   pip install paramiko
3.Credenciales de acceso SSH
Asegúrate de tener las direcciones IP, nombres de usuario y contraseñas de los dispositivos a los que deseas conectarte.

Uso

   1. Clona este repositorio o descarga el archivo directamente:
git clone [https://github.com/TeamLabStudios/Script-para-acceso-autorizado-a-dispositivos-v-a-SSH.git]
cd ssh-network-manager

2.Edita el archivo del script para configurar los dispositivos y comandos:

devices = [
    {"host": "192.168.1.10", "port": 22, "username": "admin", "password": "admin123"},
    {"host": "192.168.1.11", "port": 22, "username": "admin", "password": "admin123"}
]
command = "uname -a"

3.Ejecuta el script:

python ssh_manager.py

Notas importantes

   - Este script está destinado para uso legítimo únicamente. Asegúrate de tener permiso para acceder a los dispositivos configurados.
   - Los datos de acceso (usuario y contraseña) deben protegerse adecuadamente para evitar comprometer la seguridad de la red.

Contribuciones

Si deseas contribuir al proyecto, realiza un fork del repositorio, haz tus cambios y envía un pull request. ¡Serán bienvenidas las mejoras!

Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

Si necesitas personalizarlo más o agregar secciones específicas, ¡dímelo! 😊


