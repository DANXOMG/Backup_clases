# pintar los caracters con emoticonos

import random

def generar_tablero(parejas):
    elementos = parejas * 2 # Duplicamos elementos
    random.shuffle(elementos) # Mezclamos posiciones
    return elementos

def mostrar_tablero(tablero, descubiertos):
    return [tablero[i] if i in descubiertos else "_" for i in range(len(tablero))]

def jugar_parejas():
    parejas = []#meter emoticonos
    tablero = generar_tablero(parejas)
    descubiertos = set()
    intentos = 0
    
    print("bienvenida")
    
    while len(descubiertos) < len(tablero):
        print("\nTablero:", mostrar_tablero(tablero, descubiertos))        
        try:
            pos1 = int(input("Elige la primera posición (0-11): "))
            pos2 = int(input("Elige la segunda posición (0-11): "))
        except ValueError:
            print("inutil")
            continue
    
        if pos1 == pos2 or pos1 not in range(len(tablero)) or pos2 not in range(len(tablero)):
            print("error")
            continue
    
        intentos += 1
    
        if tablero[pos1] == tablero[pos2]:
            print("pareja encontrada")
            descubiertos.update([pos1,pos2])
        else:
            print("no es un pareja")
            
    print("victoria")
        
if __name__ == "__main__":
    jugar_parejas()