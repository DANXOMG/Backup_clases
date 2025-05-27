#Explicacion de la sentencia for

numeros = [1,2,3,4,5,6]

print("Mostrar el cuadrado de cada numero de la lista")
for num in numeros:
    cuadrado = num ** 2
    print(F"El cuadrado de {num} es {cuadrado}")


nombres = ["Ana", "Luis", "Pepe", "Maria"]
print("Saludando a cada persona")

for nombr in nombres:
    print(f"Hola, {nombr}")


#Ejemplo de rango

print("Contando del 1 al 8")
for i in range(8):
    print(i)