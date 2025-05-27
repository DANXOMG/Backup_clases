# longitud de una cadena

saludo = "Hola alumnos de Infanta Elena"
longuitud_saludo = len(saludo)
print(" El saludo tien: ", longuitud_saludo, " de caracteres.")

# Quitar espacios

cadena_con_espacios = "            esto es una cadena de prueba...           "
print("Con espacios: ", cadena_con_espacios)

cadena_sin_espacios = cadena_con_espacios.strip()
print("Sin espacios: ", cadena_sin_espacios)

# Criptografía

mensaje_cifrado = "PEESTOPEESPEUNPEMENSAJEPECIFRADOPE"
mensaje_descifrado = mensaje_cifrado.replace("PE", " ")
print("Mensaje descifrado: ", mensaje_descifrado)

# Mayúsculas, minúculas y títulos

m_minusculas = "vamos a gritar un poco"
m_mayusculas = m_minusculas.upper()
print("El mensaje esta en mayúculas: ", m_mayusculas)

m_mayusculas = "ESTE ES UN MENSAJE MAYÚSCULA"
m_minusculas = m_mayusculas.lower()
print("El mensaje esta en minúsculas: ", m_minusculas)

# Título pone la primera letra de cada palabra en mayúsculas
titulo = m_minusculas.title()
print("El mensaje es un título; ", titulo)

# Prefijos y sufijos

url = "www.google.com"
prefijo = url.startswith("www.")
sufijo = url.endswith(".com")

print("Prefijo es: ", prefijo, " , sufijo es: ", sufijo)

# Posiciones

indice = url.find("google")
print("Indice: ", indice)

# concatenación entre cadenas

nombre = "Federico"
edad = 44 # Ojo con meter un número, lo convertiremos a srting con una función str()
cargo = "Técnico de Sistemas"

saludo22 = "Mi nombre es " + nombre + " tengo " + str(edad) + " años. Y soy " + cargo
print(saludo22)

saludof22 = f"Mi nombre es {nombre} tengo {edad} años. Y soy {cargo}"
print(saludof22)

# Cadena como array de caracteres

cadena = "Esto es una cadena"
print("En la posición 6 el caracter es: ", cadena[6])