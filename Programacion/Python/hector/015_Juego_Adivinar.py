# Función adivinar

from random import random #Importamos para obtener números aleatorios

secreto = int(random()*100) # Multiplicamos por 100 para que nos de un valor de 0 a 100 si no entre 0 y 1
intentos = 0

while True: #Para un bucle infinito para testeo
    numero = int(input(f"\nIntenta adivinar el número: "))
    intentos += 1
    if numero == secreto:
        break
    elif numero > secreto:
        print(f"\nDemasiado alto.")
    elif numero < secreto:
        print(f"\nDemasiado bajo.")
print(f"\nAcertaste el número en ", intentos, " intentos")
