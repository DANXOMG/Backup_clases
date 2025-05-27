# Calcular el volumen de un cilindro (Altura * Pi) * radio al cuadrado

import math
# Importamos libreraría matemática que ya tiene definida pi
#def se usa para definir una función
def calcular_volumen_cilindro(radio, altura):
    
    """
    Calcula el volumen de un cilindro dado su radio y altura.
    Parámetros:
    radio(float): El radio del cilindro.
    altura(float): La altura del cilindro.
    Retorna:
    float: El volumen del cilindro.
    
    """

    if radio <= 0 or altura <= 0 :
        return "La base y la altura deben de ser mayores que 0"
    
    volumen = (altura * math.pi) * (radio ** 2) #Llamamos a libreria para coger Pi, math.pi
    return volumen

# Ejemplo de uso de la función

radio = float(input("Introduce el radio del cilindro: "))
altura = float(input("Introduce la altura del cilindro: "))

resultado = calcular_volumen_cilindro(radio,altura)
print (f"El volumen del cilindro es: {resultado:.2f} ")# Con F o f formatea para meter la variable dentro de las comillas en vez de concatenar :.2f para indicar dos decimales