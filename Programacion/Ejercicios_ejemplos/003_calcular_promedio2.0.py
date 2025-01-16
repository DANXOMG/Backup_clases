def calcular_promedio():
    numeros = [float(input('Dame un numero: ')) for i in range(3)]
    promedio = sum(numeros) /3
    print(f"El promedio de los tres numeris es: {promedio:.2f}")

calcular_promedio()