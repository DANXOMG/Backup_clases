#Coversion de grados celsius a fahrenheit
## formula: F = (Celsius * 9/5) + 32


import math
grados = float(input(f"Introduce los grados que hace actualmente: "))
print(f"Calculado espere...")


def conversion_grados_a_celsius(grados):
    fahrenheit = ((grados * 9/5) +32)
    return fahrenheit

print(f"Este es el resultado de la conversion de grados C a F: ")
print(conversion_grados_a_celsius(grados))