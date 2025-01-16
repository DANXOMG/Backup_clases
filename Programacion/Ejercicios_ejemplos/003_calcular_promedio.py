def calcular_promedio():
    num1 = float(input('Dame un numero: '))
    num2 = float(input('Dame un numero: '))
    num3 = float(input('Dame un numero: '))

    promedio = (num1 + num2 + num3) /3
    print(f'El promedio de los tres numeros es: {promedio:.2f}')

calcular_promedio()