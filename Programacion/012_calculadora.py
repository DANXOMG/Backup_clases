#Calculadora

def sumar(a,b):
    return a + b

def restar(a,b):
    return a - b

def multipilcar(a,b):
    return a * b

def dividir(a,b):
    if b !=0:
        return a / b
    else:
        return "error: duvisión por cero"
    
    
def potencia (a,b):
    return a ** b

def menu():
    print("/n---- Calculadora ----")
    print("1. - Sumar")
    print("2. - Restar")
    print("3. - Multiplicar")
    print("4. - Dividir")
    print("5. - Potencia")
    print("6. - Salir")
    
    
while True:
    menu()
    opcion = input("Selecciona la opción (1-6)")
    
    if opcion == "6":
        print("saliendo de la calculadora...")
        break    