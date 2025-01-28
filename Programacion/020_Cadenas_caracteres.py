#Longitud de una cadena

saludo = "Hola alumnos de Infanta Elena"

longitud_saludo = len(saludo)

print('El saludo tiene: ', longitud_saludo, 'caracteres.')



# Quitar espacios

cadena_con_espacios = '         esto es una cadena de prueba...          '
print('Con espacios: ', cadena_con_espacios)

cadena_sin_espacios = cadena_con_espacios.strip()
print('Sin espacios: ', cadena_sin_espacios)



#Criptografia

mensaje_cifrado = 'PEESTOPEESPEUNPEMENSAJEPECIFRADO'

mensaje_descifrado = mensaje_cifrado.replace('PE', ' ')

print('Mensaje descifrado: ', mensaje_descifrado)


#Mayusculas, minusculas y titulos

minusculas = 'vamos a gritar un poco'
mayusculas = minusculas.upper()
print('El mensaje esta en mayúsculas: ', mayusculas)

mayusculas = 'ESTE ES UN MENSAJE EN MAYUSCULAS'
minusculas = mayusculas.lower()
print('El mensaje esta en minusculas: ', minusculas)


titulo = minusculas.title()
print('El mensaje es un titulo: ', titulo)

#Prefijos y sufijos

url = 'www.google.com'

prefijo = url.startswith('.www')
sufijo = url.endswith('.com')

print('Prefijo es: ', prefijo)
print('Sufijo es: ', sufijo)


#Posiciones

indice = url.find("google") #indica la posicion de la palabra google que es 4 y empieza desde el 0
print("indice: ", indice)

#Concatenacion de cadenas

nombre = 'Federico'
edad = 34
cargo = 'Tecnico de Sistemas'

saludo22 = "Mi nombre es: " + nombre + " tengo " + str(edad) + " años y soy " + cargo #necesitamos meter la edad en string para que funcione
print(saludo22)

saludof22 = f"Mi nombre es {nombre} tengo {str(edad)} y soy {cargo}"
print(saludof22)

#Cadena como array de caracteres 
cadena = "Esto es una cadena"
print('En la posicion 8 el caracter es: ', cadena[8])
