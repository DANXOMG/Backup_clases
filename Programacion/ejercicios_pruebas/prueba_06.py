lista = ["audi", "toyota", "Wolkswagen", "BMW", "Lancia"]

for coche in lista:
    print(f"Mi coche es un: {coche}")

numeros = [1, 2, 3, 4, 6, 7, 8, 9]

for num in numeros:
    print(f"Mi numero {num} x2 = {num *2}")




while True:
    contador = int(input("Dame un numero y cuento hasta él: "))
    if contador > 0:
        print("Contando hasta...")
        break
    else:
        print("El contador no es válido")


print(f"Contando hasta {contador}")

for i in range(1, contador):
    print(i)

print(contador)


