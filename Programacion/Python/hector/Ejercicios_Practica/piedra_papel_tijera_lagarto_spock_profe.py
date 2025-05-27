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
def piedra_papel_tijera_lagarto_spock():
    opciones = ["piedra", "papel", "tijera", "lagarto", "spock"]
    reglas = {
        "piedra": {"tijera": "aplasta", "lagarto": "aplasta"},
        "papel": {"piedra": "cubre", "spock": "desacredita"},
        "tijera": {"papel": "corta", "lagarto": "decapita"},
        "lagarto": {"papel": "come", "spock": "envenena"},
        "spock": {"piedra": "vaporiza", "tijera": "rompe"}
    }
    
    punctuation_jugador = 0
    punctuation_computadora = 0
    ronda = 0
    
    while True:
        computadora = random.choice(opciones)
        jugador = input("Elige piedra, papel, tijera, lagarto, spock: ").lower()
        
        print(f"{reglas[jugador],[computadora]}")
        break

piedra_papel_tijera_lagarto_spock()
    
    