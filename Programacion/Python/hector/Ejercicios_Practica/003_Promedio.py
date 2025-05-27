# Promedio de tres números

"""
def calcular_promedio():
    num1 = float(input("Indica un número: "))
    num2 = float(input("Indica un número: "))
    num3 = float(input("Indica un número: "))
    
    promedio = (num1 + num2 + num3) / 3
    
    print(f"El promedio de los tres números es: {promedio:.2f}")
    
calcular_promedio()

"""

# Otra forma de hacerlo con una lista de números. Más correcta y adaptable

def calcular_promedio():
    numeros = [float(input('Dame un número: ')) for i in range(10)]
    promedio = sum(numeros) / 10
    print(f"El promedio de los tres números es: {promedio:.2f}")
    
calcular_promedio()