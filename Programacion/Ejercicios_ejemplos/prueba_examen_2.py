#calcular el area de un triangulo
# Area de un triangulo es: area = b * a /2
import math


def area_triangulo():
    base = float(input("Introduce la base: "))
    altura = float(input("Introduce la altura: "))
    area = base * altura / 2
    print(f"El area de tu triangulo es: {area}")


area_triangulo()

# Calcular el volumen de un cilindro
# V = pi * r**2 * altura

#def volumen_circulo():
#    radio = float(input("Introduce el radio de tu cilindro: "))
#    altura = float(input("Introduce la altura de tu cilindro: "))
#    volumen = math.pi * (radio ** 2) * altura
#    if radio < 0 or altura < 0:
#        print("El radio y la altura deben tener valores mayor que cero")
#    else:
#        print(f"El  volumen de tu cilindro es: {volumen}")

#Otra manera de hacerlo
def volumen_cilindro():
    while True:
        radio = float(input("Introduce el radio de tu cilindro: "))
        altura = float(input("Introduce la altura de tu cilindro: "))
        if radio > 0 and altura > 0:
            volumen = math.pi * radio**2 * altura
            print(f"El volumen de tu cilindro es: {volumen}")
            break
        else:
            print("El radio y la altura deben ser mayores que cero. Inténtalo de nuevo.")

volumen_cilindro()



