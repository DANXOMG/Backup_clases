import os

##directorio actual
def eje1():
    print("Ej1: Mostrar el directorio actual")
    directorio_actual = os.getcwd()
    print(" El directorio actual: ", directorio_actual)
    print("-"*50)
   
def eje2():
    print("Ej2: Listar archivos y directorios")
    elementos = os.listdir(os.getcwd())
    
    print(" Elementos del directorio actual: ")
    for elemento in elementos:
        print("-", elemento)
    print("-"*50)
    
def eje3():
    print("Ej3: Crear un directorio")
    nombre_d = "mi_nuevo_directorio6"
    if not os.path.exists(nombre_d):
        os.mkdir(nombre_d)
        print(f"Directorio '{nombre_d}' creado.")
    else:
        print(f"El directorio '{nombre_d}' ya existe.")
    print("-"*50)
    
    
def eje4():
    print("Ej4: Cambiar de directorio")
    nombre_d = "mi_nuevo_directorio6"
    if os.path.exists(nombre_d):
        os.chdir(nombre_d)
        print(f"Nuevo Directorio actual '{nombre_d}'.")
    else:
        print(f"En el directorio '{nombre_d}' ya estás dentro.")
    print("-"*50)
    
    
def eje5():
    os.chdir("..")
    direcrotiov = "mi_nuevo_directorio6"
    directorionuevo = "2332aa"
    print("Ej5: Renombrar directorio")
    nombre_d = "mi_nuevo_directorio"
    if os.path.exists(nombre_d):
        os.rename(direcrotiov, directorionuevo)
        print(f"Nuevo Directorio actual '{directorionuevo}'.")
    else:
        print(f"Directorio '{directorionuevo}' no existe.")
    print("-"*50)
    
    
def eje6():
    archivo = "prueba.txt"
    if os.path.exists(archivo):
        os.remove(archivo)
        print(f"Archivo '{archivo}' eliminado.")
    else:
        print(f"Directorio '{archivo}' no existe.")
    print("-"*50)
        
   
def main():
    print ("\nEjercios sobre el módulo OS \n")
    eje1()
    eje2()
    eje3()
    eje4()
    eje5()
    eje6()
       
if __name__ == "__main__":
    main()