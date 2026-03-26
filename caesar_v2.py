mensaje = input("Escribe el mensaje:  ")
resultado = ""
clave = int(input("Dime la clave:  "))
for letra in mensaje:
    if letra.isupper():  
        numero_ascii = ord(letra)
        indice = numero_ascii - 65
        nuevo_indice = (indice + clave) % 26
        nuevo_ascii = nuevo_indice + 65
        nueva_letra = chr(nuevo_ascii)
        resultado = resultado + nueva_letra 
    else:
        resultado = resultado + letra
print(f"Mensaje cifrado: {resultado}")
