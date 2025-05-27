# Para calcular un año bisiesto, tiene que ser divisible entre cruatro y no divisible entre 100 a menos que también sea divisible por 400

def calcular_bisiesto():
    anio = float(input("Indica el año: "))
    # Como se tiene que cumplir dos condiciones o una tercera sería (A y B) o C
    if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0: #En python % es el equivalente a mod, resto de división
        print("El año es bisiesto")
    else:
        print("El año no es bisiesto")   
    
calcular_bisiesto()