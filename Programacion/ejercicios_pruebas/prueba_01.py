#cadena numerica
edad = 25
print(edad)

#cadena tipo cadena
cadena = ["Pepe, alvaro"]
print(cadena)


#variuable booleana
es_cliente= True
print(es_cliente)

#variable lista
coches = ["mclaren", "ferrari", "bmw", "audi"]
print(coches)
#nombrar por la posicion, En este caso la posicion 2 (empieza en 0)
print(coches[2])
#tupla
coordenadas = (10, 20)
print(coordenadas)
#tipo conjunto
frutas={"manzana", "pera", "limon", "aguacate"}
print(frutas)
#variable diccionario
frutas ={"nombre":"manzana", "pera":30, "limon": "lima", "aguacate": "guacamole"}
print(frutas)


#sumas restas multiplicaciones
a=10
b=5
suma= a+b
resta= a-b
dividir= a/b
multiplicar= a * b

divisionentera= a // b
resto= a % b
potencia = a ** b

print("suma: ", suma)
print("Resta: ", resta)
print("Dividir: ", dividir)
print("Multiplicar: ", multiplicar)
print("Divion(entera): ", divisionentera)
print("Resto: ", resto)
print("potencia: ", potencia, "10 ** 5 ")




#Comparaciones
a= 20
b = 10

es_mayor = a > b
es_menor = a < b
es_igual = a == b
print("a:", a, "b:", b)
print("Es mayor:", es_mayor)
print("Es menor: ", es_menor)
print("Es igual: ", es_igual)



#Operaciones AND, OR, NOT
x= True
y= False

print("Operador and")
operador_and= x and y
print(operador_and)

print("Operador or")
operador_or= x or y
print(operador_or)


print("Operador not")
operador_not= not x
print(operador_not)


#Operadores de asignacion

c= 10 
c -= 5 #le va restando 5 al numero inicial 10

print("Asignacion de acumulador: ", c)


#operadores pertenecia

lista_numeros=[1,2,3,4,5,6,7,8,9,10]
existe = 4 in lista_numeros
no_existe= 11 in lista_numeros

print("Lista de numeros: ", lista_numeros)
print("Existe 4 en la lista: ", existe)
print("No existe 11 en la lista: ", no_existe)


#operadores nivel de bits

num1 = 10
num2 = 5

bit1= num1 & num2
bit2= num1 | num2

#compara los bits 
print(bit1)
print(bit2) 


# operadores de identidad is, is not

pepe = [1, 2, 3]
juan= pepe
guillermo = [1, 2, 3]

print("pepe es juan?", pepe is juan)
print("pepe no es guillermo?", pepe is not guillermo)

#######################################################

#conversion tipos

cadena = "109"
entero = int(cadena)

print(cadena, "string")
print(entero, "numero entero int")
print("convertido a numero entero 109 + 1: " , entero + 1)

#convertir entero a cadena

numero = 100
cadena_entero = str(numero)

print(numero, "se ha convertido en string (numero + " ")")
print(numero, "naranjas")


#convertir de flotante a entero 

numero_float = 150.50
num_entero = int(numero_float)

print(numero_float, "numero flotante")
print(num_entero, "numero_float convertido a entero")


#convertir de lista a conjunto

lista = [1, 2, 3, 4, 5]
conjunto = set(lista)

print("lista", lista)
print("conjunto", conjunto)


#pasar de diccionario a lista de claves

diccionario = {"a":1, "b":2, "c":3}
lista_claves=list(diccionario.keys()) #Coge solo en la lista los str a,b,c
lista_valores=list(diccionario.values()) #Coge solo en la lista los valores 1,2,3

print(diccionario)
print(lista_claves)
print(lista_valores)


#Funciones 

# area de un triangulo b * a /2
# base(float), altura(float)
# retorna area(float)



base = float(input("Dame la base del triangulo: "))
altura = float(input("Dame la altura del triangulo: "))
area = (base * altura) / 2

def area_triangulo(base, altura):
    
    if base <= 0 or altura <= 0:
        return "La base o altura debe ser mayor que 0"
    
    return area 



print(base)
print(altura)
print("Esta es el area de tu triangulo: ", area_triangulo(base, altura))








