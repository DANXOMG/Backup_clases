# suma de elementos en una lista

   # devuelve la suma de los elementos de la lista



def suma_elementos(lista): #Necesitamos sumar cada elemento de la lista que metamos como argumento
   suma = 0 #creamos la variable "suma" donde guardaremos el resultado de la suma de cada elemento en la lista
   for element in lista: #Recorremos la lista elemnto en lista
      suma = suma + element   # suma = 0 + elemnto en la lista = "suma de todos los elementos" 
   return suma #Nos devuelve el resultado de la suma de elemntos

print(suma_elementos([1, 2, 3, 4 ,5])) #Imprimimos el resultado con la funcion metiendo como parametro la lista que queramos
      

