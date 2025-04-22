#Calculadora

def sumar(a,b):
    return a + b

def restar(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    if b !=0:
        return a / b
    else:
        return "error: división por cero"
    
    
def potencia (a,b):
    return a ** b

def menu():
    print("---- Calculadora ----")
    print("Elige una de las siguientes opciones: ")
    print("1. - Sumar")
    print("2. - Restar")
    print("3. - Multiplicar")
    print("4. - Dividir")
    print("5. - Potencia")
    print("6. - Salir")
    
    
while True:
    menu()
    opcion = input("Selecciona la opción (1-6)")
    a = float(input("Dame un numero: "))
    b = float(input("Dame otro numero: "))
    if opcion == "1":
        print(sumar(a,b))
        break
    if opcion == "2":
            print(a)
            print(b)
            print(restar(a,b))
    if opcion == "3":
        print(a)
        print(b)
        print(multiplicar(a,b))
    if opcion == "4":
        print(a)
        print(b)
        print(dividir(a,b))
    if opcion == "5":
        print(a)
        print(b)
        print(potencia(a,b))
    if opcion == "6":
        print("saliendo de la calculadora...")
        break
    else:
        print("El comando ejecutado no existe en el menu")
    


       