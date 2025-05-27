import os

# Direcctorio actual
def eje1():
    print("Eje1: Mostrar el directorio actual")
    directorio_actual = os.getcwd()
    print("El directorio actual: ", directorio_actual)
    print("-"*50)
 
# Listas archivos y directorios de nuestra ubicación   
def eje2():
    print("Eje2: Listas archivos y directorios")
    elementos = os.listdir(os.getcwd())
    print("Elementos del directorio actual:")
    for elemento in elementos:
        print(" - ", elementos)
    print("-"*50)
    
# Crear un directorio nuevo
def eje3():
    print("Eje3: Crear un directorio")
    nombre_d = "mi_nuevo_directorio_2"
    if not os.path.exists(nombre_d):
        os.mkdir(nombre_d)
        print(f"Directorio '{nombre_d}' creado con éxito.")
    else:
        print(f"El directorio '{nombre_d}' ya éxiste")
    print("-"*50)

# Cambiar de directorio
def eje4():
    print("Eje4: Cambiar de directorio")
    nombre_d = "mi_nuevo_directorio_2"
    if os.path.exists(nombre_d):
        os.chdir(nombre_d)
        print(f"Nuevo directotio actual '{nombre_d}'")
    else:
        print(f"El directorio '{nombre_d}' ya éxiste")
    print("-"*50)
    
# Renombrar directorio
def eje5():
    os.chdir("..")
    directorio_v = "mi_nuevo_directorio_2"
    directorio_n = "mnd4"
    if os.path.exists(directorio_v):
        os.rename(directorio_v, directorio_n)
        print(f"Directorio renombrado '{directorio_n}'")
    else:
        print(f"El directorio '{directorio_n}' no éxiste")
    print("-"*50)
    
def eje6():
    archivo = "prueba.txt"
    if os.path.exists(archivo):
        os.remove(archivo)
        print(f"Archivo '{archivo}' borrado")
    else:
        print(f"El archivo '{archivo}' no encontrado")
    print("-"*50)

# Muestra las variables del sistema, en este caso usamos posix, para linux, nt seria para windows    
def eje7():
    print("Eje7: Cambiar de directorio")
    if os.name == 'posix':
        var_usuario = os.environ.get("HOME")
    print("VARIABLES")
    for clave,valor in os.environ.items():
        print(f"{clave}: {valor}")
    print("-"*50)

def main():
    print("\nEjercicios sobre el modulo OS\n")
    eje1()
    eje2()
    eje3()
    eje4()
    eje5()
    eje6()
    eje7()
    
if __name__ == '__main__':
    main()