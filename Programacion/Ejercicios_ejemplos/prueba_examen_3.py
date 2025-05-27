# Calculadora sumar, restar, multiplicar, dividir


def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
def multiplicar(a ,b):
    return a * b
def dividir(a, b):
    if b != 0:
        return a / b
    else:
        print("La division no puede ser entre cero")

def calculadora():
    print("---- Calculadora ----")
    print("Elige una de las siguientes opciones: ")
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")
    print("4.- Dividir")
    print("5.- Salir")

    while True:
        opcion = input("Selecciona una de las opciones (1-5): ") 
        if opcion == "5":
            print("Saliendo de la calculadora...")
            break
        elif opcion in ("1", "2", "3", "4"):
            a = float(input("Dame un numero: "))
            b = float(input("Dame otro numero: "))
            if opcion == "1":
                print("Has elegido sumar")
                print(f"El resultado de la suma es: {sumar(a,b)}")
           
            elif opcion == "2":
                print("Has elegido restar")
                print(f"El resultado de la resta es: {restar(a,b)}")
            
            elif opcion == "3":
                print("Has elegido multiplicar")
                print(f"El resultado de la multiplicacion es: {multiplicar(a,b)}")
            
            elif opcion == "4":
                print("Has elegido dividir")
                print(f"El resultado de la division es: {dividir(a,b)}")
        else:
            print("Opcion no valida, por favor selecciona una opcion valida (1-5)")
            continue

        

calculadora()


