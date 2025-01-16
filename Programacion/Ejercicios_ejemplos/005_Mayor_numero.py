def numero_mayor():
    
    num1 = float(input("Escribe un numero: "))
    num2 = float(input("Escribe un numero: "))
    num3 = float(input("Escribe un numero: "))
    num4 = float(input("Escribe un numero: "))
    num5 = float(input("Escribe un numero: "))
    

    mayor = num1;

    if(num2 > mayor):
        mayor = num2
    
    if(num3 > mayor):
        mayor = num3

    if(num4 > mayor):
        mayor = num4

    if(num5 > mayor):
        mayor = num5

    print(f"El numero mayor es: {mayor:.2f}")

numero_mayor()