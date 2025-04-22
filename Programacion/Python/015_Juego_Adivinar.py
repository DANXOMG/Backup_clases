#Funcion adivinar

from random import random

secreto = int(random() * 100)
intentos = 0

while True:  #bucle infinito

    numero = int(input("Intenta adivinar el numero: "))
    intentos += 1

    if numero == secreto: break #esto finaliza el programa manualmente
    elif numero > secreto:print("Demasiado alto")
    elif numero < secreto:print("Demasiado bajo")
print("Acertaste en ", intentos, "intentos")
