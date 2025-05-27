# Determinar cuál es el número mayor de una serie.
""" 
def numero_mayor():
    num1 = float(input("Escribe un número: "))
    num2 = float(input("Escribe un número: "))
    num3 = float(input("Escribe un número: "))
    
    mayor = num1
    
    if (num2 > mayor):
        mayor = num2
        
    if (num3 > mayor):
        mayor = num3
    
    print(f"El número mayor es: {mayor:.2f}")

"""
# Ejemplo con lista de números
def numero_mayor():
    
    numeros = [float(input("Escribe un número: ")) for i in range(10)]
    mayor = max(numeros)
    print(f"El número mayor es: {mayor:.2f}")
    
numero_mayor()

