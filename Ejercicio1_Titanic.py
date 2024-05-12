import pandas as pd

"""
Generar un DataFrame con los datos del archivo.
Mostrar por pantalla las dimensiones del DataFrame, el número de datos que contiene, los nombres de sus columnas y filas, los  tipos de datos de las columnas, las 10 primeras filas y las 10 últimas filas
Mostrar por pantalla los datos del pasajero con identificador 148.
Mostrar por pantalla las filas pares del DataFrame.
Mostrar por pantalla los nombres de las personas que iban en primera clase ordenadas alfabéticamente.
Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron.
Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase.
Eliminar del DataFrame los pasajeros con edad desconocida.

Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase.
Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.
Mostrar por pantalla el porcentaje de menores y mayores de edad que sobrevivieron en cada clase.
"""

#1 Generar Datafram
titanic_df = pd.read_csv('titanic.csv')
print(titanic_df)
input()

#2
#Dimensiones
Dimensiones = titanic_df.shape
print("(renglones, columnas) = ",Dimensiones)
#Numero datos
num_datos = Dimensiones[0]
print("Numero datos: ",num_datos)
#Nombre de columnas
columns = titanic_df.columns
print("Nombre Columnas: ",columns)
#Tipos de datos de columnas
tipos_columnas = titanic_df.dtypes
print("Tipos: \n", tipos_columnas)
#10 primeras filas y 10 ultimas filas
print("Primeras 10 filas:\n", titanic_df.head(10))
print("\n\nUltimas 10 filas:\n", titanic_df.tail(10))
input()

#3 Mostrar datos de id = 148
passenger148 = titanic_df.loc[titanic_df['PassengerId']==148]
print(passenger148)
input()

#4 Filas Pares
Pares = titanic_df[::2]
print(Pares)
input()

#5 Primera Clase ordenados alfabeticamente
pd.set_option('display.max_columns', None)
PrimeraClase = titanic_df.loc[titanic_df['Pclass'] == 1]
Ordenados = PrimeraClase.sort_values('Name')[['PassengerId','Name','Pclass']]
print(Ordenados)
pd.reset_option("max_columns")
input()

#6 Porcentaje muertes y vivos
muertos =  ((len(titanic_df.loc[titanic_df['Survived'] == 0])) / Dimensiones[0]) * 100
vivos = ((len(titanic_df.loc[titanic_df['Survived'] == 1])) / Dimensiones[0]) * 100

print(f"\nMuertos: {round(muertos,2)}%, Vivos: {round(vivos,2)}%")
input()

#7 Porcentaje sobrevivencia por clase
clases = titanic_df.Pclass.unique() # Obtener valores de clases
vivos_df = titanic_df.loc[titanic_df['Survived']==1]
clase1 = ((len(vivos_df.loc[vivos_df['Pclass'] == 1])) / vivos_df.shape[0]) * 100
clase2 = ((len(vivos_df.loc[vivos_df['Pclass'] == 2])) / vivos_df.shape[0]) * 100
clase3 = ((len(vivos_df.loc[vivos_df['Pclass'] == 3])) / vivos_df.shape[0]) * 100

print(f"\nVivos...\nClase 1: {round(clase1,2)}%, Clase 2: {round(clase2,2)}%, Clase 3: {round(clase3,2)}%")
input()

#8 Eliminar con edad desconocida
titanic_df = titanic_df[titanic_df['Age'].notna()]
print(titanic_df) # Se eliminarion 102 filas
input()

#9 Edad media de mujeres que viajaban en cada clase
mujeresVivas_df = vivos_df.loc[vivos_df['Sex'] == 'female']

mujeres_clases = mujeresVivas_df.groupby('Pclass')

med_PC1 = round(mujeres_clases.get_group(1)['Age'].mean(),2)
med_PC2 = round(mujeres_clases.get_group(2)['Age'].mean(),2)
med_PC3 = round(mujeres_clases.get_group(3)['Age'].mean(),2)

print(f"\n\nClase 1: {med_PC1}, \nClase2: {med_PC2}, \nClase3: {med_PC3}")
input()

#10 Anadir Columna para saber si pasajero era menor de edad
titanic_df["isMinor"] = titanic_df["Age"] < 18
print(titanic_df)
input()

#11 Porcentajes mayores y menores de edad que sobrevivieron

vivos = titanic_df.loc[titanic_df['Survived']==1]
minors = vivos['isMinor'].value_counts()

isMinor_P = (minors[True] / len(vivos)) * 100
notMinor_P = (minors[False] / len(vivos)) * 100

print(f"Porcentaje menores: {round(isMinor_P,2)}\nPorcentaje mayores: {round(notMinor_P,2)}")
input()

