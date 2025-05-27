# Calcular el área de un círculo (Radio * Pi²)

import math
# Importamos libreraría matemática que ya tiene definida pi
#def se usa para definir una función
def calcular_radio_circulo(radio):
    
    """
    Calcula área de un círculo dado su radio.
    Parámetros:
    radio(float): El radio del círculo.
    Retorna:
    float: El área del círculo.
    
    """

    if radio <= 0 :
        return "El radio debe de ser mayor que 0"
    
    area = radio * math.pi ** 2 #Llamamos a libreria para coger Pi, math.pi
    return area

# Ejemplo de uso de la función

radio = float(input("Introduce el radio del círculo: "))

resultado = calcular_radio_circulo(radio)
print (f"El área del círculo es: {resultado:.2f} ")# Con F o f formatea para meter la variable dentro de las comillas en vez de concatenar :.2f para indicar dos decimales