#Piedra papel tijera lagarto spok 
import random

reglas = {
    "piedra": {"tijera": "aplasta", "lagarto": "aplasta"},
    "papel": {"piedra": "cubre", "spok": "desacredita"}, 
    "tijera": {"papel": "corta", "lagarto": "decapita"},
    "lagarto": {"papel": "come", "spok": "envenena"},
    "spok": {"piedra": "vaporiza", "tijera": "rompe"}
}



def juego_piedra_papel_tijera_lagarto_spok():
    opciones = ['piedra', 'papel', 'tijera', 'lagarto', 'spok']
    jugador1 = input('Elige una de las opciones: piedra papel tijera lagarto spok: ').lower()
    jugador2 = random.choice(opciones)
    print(f'El jugador 2 eligio: {jugador2}')
    if jugador1 == jugador2:
        print('Empate')
    elif jugador2 in reglas[jugador1]:
        print(f'Ganaste, {jugador1} {reglas[jugador1][jugador2]} {jugador2}')
    else:
        print(f'Perdiste, {jugador2} {reglas[jugador2][jugador1]} {jugador1}')

juego_piedra_papel_tijera_lagarto_spok()

## falta poner contador 
