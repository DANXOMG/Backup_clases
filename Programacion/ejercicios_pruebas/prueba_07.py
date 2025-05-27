#uso de switch

#def elegir_coche(coche):
#    match coche:
#        case 1:
#            print("Has elegido un Audi")
#        case 2:
#            print("Has elegido un BMW")
#        case 3:
#            print("Has elegido un Ferrari")
#        case 4:
#            print("Has elegido un Mclaren")
#        case _:
#            print("Opcion no válida")


#coches = int(input("Elige un numero (1-4) para saber que coche te ha tocado: "))

#elegir_coche(coches)


# Longitud de una cadena

frase = "Fernando Alonso"
longitud_frase = len(frase)

print(f"Tiene {len(frase)} caracteres")
print(f"Fernando Alonso tiene: {longitud_frase} caracteres")

# Quitar espacios

espacios = "          frase con espacios         "
print(f"Con espacios: {espacios}")

sin_espacios = espacios.strip()
print(f"Sin espacios: {sin_espacios}")

#Mensaje cifrado

mensaje_cifrado = "00Esto00es00un00mensaje00cifrado00"
mensaje_descifrado = mensaje_cifrado.replace("00", "  ")
print("Descifrando mensaje...")
print("espera...")
print("Listo!")
print(f"El mensaje dice asi: {mensaje_descifrado}")

# Mayusculas a minusculas y viceversa

mayusculas = "MAYUSCULAS"
minusculas = "minusculas"

print(mayusculas)
print(minusculas)

print("Mayusculas a minusculas: ")
print(f"{mayusculas} -> {mayusculas.lower()}")
print("minusculas a mayusculas: ")
print(f"{minusculas} -> {minusculas.upper()}")
print(f"Titulo: {minusculas.title()}")

#prefijos y sufijos

link = "www.google.com"

prefijo = link.startswith("www.")
sufijo = link.endswith(".com")

print(link)
print(prefijo)
print(sufijo)

indice = link.find("google")
print(indice)

#Concatenacion de cadenas

coche = "Audi"
caballos = 220
precio = 20500
color = "negro"

print(f"Tengo un {coche} con {str(caballos)} CV que vale {str(precio)} de color {color}")
print("otra manera de hacerlo la concatenacion de cadenas: ")
especificaciones = f"Tengo un {coche} con {str(caballos)} CV que vale {str(precio)} de color {color}"
print(especificaciones)

#Cadena como array
cadena_caracteres = "abcdefghijklmnñopkrstuvwxyz"
print(cadena_caracteres)
print("La posicion 26 del array de caracteres es: ", cadena_caracteres[26])