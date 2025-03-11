#necesitamos sumar, resta, multiplicar, dividir y potencia
#funciones sumar, restar, multiplicar, dividir y potencia
def sumar(a,b):
    return a + b

def restar(a,b):
    return a -b

def multiplicar(a,b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else: 
        print("El divisor no puede ser 0")

def potencia(a, b):
    if b != 0 or 1:
        return a ** b
    else:
        print("La potencia no puede ser 0 o 1")

    
def menu_calculadora():
    print("Pulse 1 para sumar")
    print("Pulse 2 para restar")
    print("Pulse 3 para multiplicar")
    print("Pulse 4 para dividir")
    print("Pulse 5 para elevar a la potencia")
    print("Pulse 6 para salir")
    return
    


while True:
    menu_calculadora()
    opcion_menu = int(input("Seleciona una de las opcione (1 - 6): "))
    if opcion_menu == 1:
        a = float(input("Dame un numero: "))
        b = float(input("Dame otro numero: "))
        print(sumar(a,b))
        break
      
    if opcion_menu == 2:
        a = float(input("Dame un numero: "))
        b = float(input("Dame otro numero: "))
        print(restar(a,b))
        break       
    if opcion_menu == 3:
        a = float(input("Dame un numero: "))
        b = float(input("Dame otro numero: "))
        print(multiplicar(a,b))
        break
    if opcion_menu == 4:
        a = float(input("Dame un numero: "))
        b = float(input("Dame otro numero: "))
        print(dividir(a,b))
        break
    if opcion_menu == 5:
        a = float(input("Dame un numero: "))
        b = float(input("Dame un numero por el que estara elevado: "))
        print(potencia(a,b))
        break
    if opcion_menu == 6:
        print("Apagando calculadora...")
        break
    else:
        print("El numero seleccionado no existe en el menu")




    
    
   
