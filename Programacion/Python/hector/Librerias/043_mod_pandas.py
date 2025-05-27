import pandas as pd

# definir una serie
print("-" * 50)
print("Definir una serie")
serie = pd.Series([10,20,30], index=["a","b","c"])
print(serie)
print("Elemento de la clave a: ", serie["a"])
print("Longuitud de la serie: ", len(serie))
print("-" * 50)

# dataframe
print("-" * 50)
print("Crear un data frame")
datos = {
    "Nombre": ["Ana", "Luis", "Carlos"],
    "Edad": [22,35,29],
    "Ciudad": ["Madrid", "Sevilla", "Valencia"]
}
df = pd.DataFrame(datos)
print(df)
print("-" * 50)

# Mostrar filas
print("Mostrar dos primeras filas")
print(df.head(2))
# Mostrar dos últimas filas
print("-" * 50)
print("Mostrar dos últimas filas")
print(df.tail(2))
print("-" * 50)

# Resumen de datos
print("df.info")
print(df.info())
print("-" * 50)
print("df.describe()")
print(df.describe())
print("-" * 50)

# Selección de datos por columna
print("Seleccionar columnas")
print(df["Edad"])
print("-" * 50)
print("Varias columnas")
print(df[["Nombre", "Ciudad"]])
print("-" * 50)
print("Selección por posición")
print(df.iloc[0])
print("-" * 50)
print("Selección por etiqueta")
print(df.loc[1])
print("-" * 50)

# Filtrar datos
print("Filtrar datos por colummna")
print(df[df["Edad"] > 30])
print("-" * 50)

# Columna nueva
print("Columna nueva de una columna")
df["Edad en 5 años"] = df["Edad"] + 5
print("df =", df)
print("-" * 50)

# Agrupar
print("Groupby")
print("Edad media por ciudad")
print(df.groupby("Ciudad")["Edad"].mean())
print("-" * 50)

# Leer y escribir archivos
# pip install openpyxl
# pip install openpyxl; 
print("Guardar Datos en excell")
#df = pd.read_csv("archivo.csv")
df.to_excel("datos.xlsx")
print("fichero datos.xlsx guardado")
print("-" * 50)