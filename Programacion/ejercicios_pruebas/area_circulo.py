#area de un circulo
# A = pi * r^2

import math
radio = float(input("Introduce el radio del circulo:"))
print(f"Calculando...")

def area_circulo(radio):
    area = math.pi * radio ** 2
    return area

print("Calculado con exito")
print(area_circulo(radio))


