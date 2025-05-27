# IMPORTANTISIMO: si sabemos en número de veces que se va a ejecutar, se usa FOR

# Explicación de la sentencia FOR

# Con una lista de números y ejecutamos operción
numeros = [1,2,3,4,5,6]
print(f"\nMostrar el cuadrado de cada número de la lista")

for num in numeros:
    cuadrado = num ** 2
    print(f"El cuadrado de {num} es {cuadrado}")

# Con una lista de nombres
nombres = ["Ana","Pepe","Luis","María"]
print(f"\nSaludando a cada persona.")

for name in nombres:
    print(f"Hola, {name}")
    
# Ejemplo de rango
print("\nContando del 1 al 8")
for i in range(1,8):
    print(i)