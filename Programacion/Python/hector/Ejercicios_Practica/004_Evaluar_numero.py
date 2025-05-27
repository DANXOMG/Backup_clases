# Evaluamos sin un número es positivo, negativo o cero

def evaluar_numero():
    num = float(input("Ingresa un número: "))
    if num > 0:
        print("El número es positivo.")
    elif num < 0:
        print("El número es negativo.")
    else :
        print("El número es cero.")


evaluar_numero()