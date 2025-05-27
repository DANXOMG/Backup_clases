# Vamos a realizar un juego de dos jugadores, contra la máquina piedra papel tijera.
"""
###################################################################################################################
Para ello usaré la función random, para que simule la elección de la máquina.
Habrá un menú con las tres opciones disponibles, asignadas a un número del 1 al 3
Luego procederé a la comparación, empezando por el empate.
Una vez que sea funcional, añadiré el número mínimo de victorias para ganar la partida
y máximo de intentos en función de la difucultad, al mejor de uno(empezaré por ella), al mejor de 3 o al mejor de 5
####################################################################################################################
"""

# Importamos la función random, y la para usarla con la selección de la máquina.
from random import random 


# Creamos una función con el menú de opciones elegibles
def menu_juego():
    print("\n#### PIEDRA, PAPEL, TIJERA ####")
    print("1.- Piedra")
    print("2.- Papel")
    print("3.- Tijera")


# Almacenamos en variable la elección del jugador y la máquina.
while True:
    menu_juego()
    opcion = input("Selecciona una opción: ")
    #if



# Función que compare la elección del jugador con la de la máquina.


# Opción en una sola función
def piedra_papel_tijera():
    opciones = ["piedra", "papel", "tijera"]
    computadora = random.choice(opciones)