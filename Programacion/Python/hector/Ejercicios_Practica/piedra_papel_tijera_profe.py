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
import random 

# Opción en una sola función
def piedra_papel_tijera():
    opciones = ["piedra", "papel", "tijera"]
    computadora = random.choice(opciones)
    jugador = str(input("Elige piedra, papel o tijera: ")).lower()
    
    if jugador in opciones:
        print(f"La computadora a elegido: {computadora} ")
        if computadora == jugador:
            print("Has empatado con la máquina")
        elif (jugador == "piedra" and computadora == "tijera") or \
            (jugador == "papel" and computadora == "piedra") or \
            (jugador == "tijera" and computadora == "papel"):
                print("Ganaste la partida")
        else:
            print("Has perdido la partida")
            
    else:
        print("Opción invalida")

piedra_papel_tijera()
    
    