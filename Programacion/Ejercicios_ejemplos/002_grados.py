def calcular_grados():
    celsius = float(input('ingresa los grados celsius: '))
    farhenheit = (celsius * 9/5) +32
    print(f'La temperatura en farhenheit es: {farhenheit:.2f}')

calcular_grados()