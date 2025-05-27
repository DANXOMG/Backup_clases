# Calcular el área de un triángulo --> base * altura / 2

#def se usa para definir una función
def calcular_area_triangulo(base, altura):
    
    """
    Calcula el área de un triángulo dados su base y su altura.
    Parámetros:
    base(float): La base del triángulo.
    altura(float): La altura del triángulo.
    Retorna:
    float: El área del triángulo.
    
    """

    if base <= 0 or altura <= 0 :
        return "La base y la altura deben de ser mayores que 0"
    area = (base * altura)/2
    return area

# Ejemplo de uso de la función

b = float(input("Introduce la base del triángulo: "))
a = float(input("Introduce la altura del triángulo: "))

resultado = calcular_area_triangulo(b,a)
print (f"El área del triángulo es: {resultado} ")# Con F o f formatea para meter la variable dentro de las comillas en vez de concatenar