# Calculadora Modidico para comentar correctamente la subida a git, commit repetid

def suma(a,b):
    return a + b
def resta(a,b):
    return a - b
def multiplicar(a,b):
    return a * b
def dividir(a,b):
    return a / b
def potencia(a,b):
    return a ** b

def menu():
    print("\n---- Calculadora ----")
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")
    print("4.- Dividir")
    print("5.- Potencia")
    print("6.- Salir")
    
while True:
    menu()
    opcion = input("Selecciona la opción (1-6)")
    
    if opcion == "6":
        print("Saliendo de la calculadora.......... ")
        break
    
    if opcion == "5":
        num1 = float(input("Introduce el número de la base"))
        num2 = float(input("Introduce la potencia "))
        resultado = potencia(num1,num2)
        print(f"La potencia de {num1} elevado {num2} es: {resultado:.2f}")
        
    if opcion == "4":
        num1 = float(input("Introduce el primer número "))
        num2 = float(input("Introduce el segundo número "))
        if num2 != 0:
            resultado = dividir(num1,num2)
            print(f"La división de {num1} elevado {num2} es: {resultado:.2f}")
        else:
            print("Error: división por cero")
        
    if opcion == "3":
        num1 = float(input("Introduce el primer número "))
        num2 = float(input("Introduce el segundo número "))
        resultado = multiplicar(num1,num2)
        print(f"La multiplicación de {num1} elevado {num2} es: {resultado:.2f}")
        
    if opcion == "2":
        num1 = float(input("Introduce el primer número "))
        num2 = float(input("Introduce el segundo número "))
        resultado = resta(num1,num2)
        print(f"La resta de {num1} elevado {num2} es: {resultado:.2f}")
        
    if opcion == "1":
        num1 = float(input("Introduce el primer número "))
        num2 = float(input("Introduce el segundo número "))
        resultado = suma(num1,num2)
        print(f"La suma de {num1} elevado {num2} es: {resultado:.2f}")