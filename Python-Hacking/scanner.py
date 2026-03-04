import sys
import socket
from datetime import datetime

# 1. Validacion de Objetivo
# El usuario debe poner la IP al ejecutar el script
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) # Traduce nombre a IP
else:
    print("Sintaxis Invalida")
    print("Uso: python3 scanner.py <IP>")
    sys.exit()

# 2. Banner de Inicio
print("-" * 50)
print(f"Escaneando objetivo: {target}")
print(f"Hora de inicio: {str(datetime.now())}")
print("-" * 50)

# 3. El Escaneo (Bucle)
try:
    # Vamos a escanear del puerto 1 al 85 (para que sea rapido)
    # Puedes cambiar 85 por 1000 o 65535, pero tardara mas.
    for port in range(1, 85):
        # Crear el socket (IPv4, TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Establecer timeout de 1 segundo (Si no responde en 1s, pasamos al siguiente)
        socket.setdefaulttimeout(1)
        
        # Intentar conectar (connect_ex devuelve 0 si hay exito)
        resultado = s.connect_ex((target, port))
        
        if resultado == 0:
            print(f"Puerto {port} esta ABIERTO")
        
        # Cerrar la conexion para liberar recursos
        s.close()

except KeyboardInterrupt:
    print("\nSaliendo del programa...")
    sys.exit()

except socket.gaierror:
    print("No se pudo resolver el hostname.")
    sys.exit()

except socket.error:
    print("No se pudo conectar al servidor.")
    sys.exit()
