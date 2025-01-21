def numero_mayor():
    
    numeros =[float(input('Escribe un numero: ')) for i in range(3)]
    grande = max(numeros)
    print(f'El numero mayor es: {grande:.2f}')

numero_mayor()