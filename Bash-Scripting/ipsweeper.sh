#!/bin/bash

# 1. Validación de Entrada
# Si el usuario NO me da un argumento (la IP), le enseño cómo usar el script.
if [ "$1" == "" ]
then
    echo "¡Error! Olvidaste la dirección IP."
    echo "Sintaxis: ./ipsweeper.sh 192.168.1"

else
    # 2. El Bucle (Loop)
    # Vamos a recorrer los números del 1 al 254.
    for ip in `seq 1 254`; do
        # 3. La Acción
        # Hacemos ping una sola vez (-c 1) a la IP construida ($1.$ip).
        # Usamos grep para buscar la línea que dice "64 bytes" (significa que respondió).
        # El símbolo & al final permite que se ejecuten varios pings a la vez (multithreading básico).
        ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
    done
fi
