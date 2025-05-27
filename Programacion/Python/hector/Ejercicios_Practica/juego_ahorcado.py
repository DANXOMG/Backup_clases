"""
Un juego del ahorcado.

if __name__ == "__main__":
    jugar_ahorcado() indicamos funcion principal


"""
import random 

def juego_ahorcado():
    opciones = ["python"]
    jugador = []
    vacio = "_"
    pista = ["_"]
    
    while True:
        computadora = random.choice(opciones)
        secreta = list(map(str, computadora.lower()))
        tamanio = (int(len(secreta)))
        print(tamanio)
        print(secreta)
        for i in range(tamanio):            
            pista.append(pista[i])
        print("".join(pista))
        jugador = []
        jugador.append(input("Indique una letra: ").lower())
        
        pista.add(jugador)
        
        
        break
juego_ahorcado()

    