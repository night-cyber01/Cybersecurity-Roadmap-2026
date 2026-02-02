# caesar.py - Herramienta de Cifrado Cesar
# Uso: python3 caesar.py

def cifrar(texto, desplazamiento):
    resultado = ""
    
    # Recorremos cada letra del mensaje
    for letra in texto:
        # Solo ciframos mayusculas por ahora (Simpleza)
        if letra.isupper():
            # 1. Convertir letra a numero ASCII (A = 65)
            ascii_original = ord(letra)
            
            # 2. Normalizar a 0-25 (A=0, B=1...) para usar modulo
            indice_original = ascii_original - 65
            
            # 3. Aplicar desplazamiento y modulo 26 (El truco del reloj)
            nuevo_indice = (indice_original + desplazamiento) % 26
            
            # 4. Volver a convertir a ASCII real (+65)
            nuevo_ascii = nuevo_indice + 65
            
            # 5. Convertir numero a letra y agregar al resultado
            resultado += chr(nuevo_ascii)
        else:
            # Si no es mayuscula (espacio, numero), lo dejamos igual
            resultado += letra
            
    return resultado

# --- Bloque Principal ---
mensaje = input("Ingresa el mensaje (MAYUSCULAS): ")
clave = int(input("Ingresa la clave numerica (ej. 3): "))

mensaje_cifrado = cifrar(mensaje, clave)
print(f"Mensaje Original: {mensaje}")
print(f"Mensaje Cifrado:  {mensaje_cifrado}")
