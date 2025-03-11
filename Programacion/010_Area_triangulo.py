#Area del triangulo: b * a /2 

#def = funcion en python

def calcular_area_triangulo(base, altura):
    """
    Calcula el área de un triangulo dados su base y altura
    Parámetros:
    base(float): la base de triángulo
    altura(float): la altura del triángulo
    Retorna:
    float: El área del Triángulo
    """

    if base <= 0 or altura <= 0 : 
        return "La base y la altura deben de ser mayores que 0"
    
    area = (base * altura)/2
    return area


#Ejemplo de uso de la funcion
base = float(input("Introduce la base: "))
altura = float(input("Introduce la altura: "))
resultado = calcular_area_triangulo(base,altura)
#b = base  a = altura



print("El area del triangulo es: ", resultado)
print(f"El area del triangulo es: {resultado}")

