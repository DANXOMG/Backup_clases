# Solicita un número al usuario y calcula la suma de sus dígitos.
def suma():
    # Pido el número al usuario y lo almaceno en una variable
    num = input("Indica un número de al menos dos cifras: ")
    # Con map separo el número en digitos, le indico que son enteros y los almaceno en una lista
    cifras = list(map(int, num))
    # Sumo todos los valores de la lista y muestro el resultado
    print(sum(cifras))
    #print(cifras)

suma() 
