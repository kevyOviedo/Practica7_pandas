import pandas as pd

"""
Generar un DataFrame con los datos de los cuatro archivos.
Filtrar las columnas del DataFrame para quedarse con las columnas ESTACION, MAGNITUD, AÑO, MES y las correspondientes a los días D01, D02, etc.
Reestructurar el DataFrame para que los valores de los contaminantes de las columnas de los días aparezcan en una única columna.

Añadir una columna con la fecha a partir de la concatenación del año, el mes y el día (usar el módulo datetime).
Eliminar las filas con fechas no válidas (utilizar la función isnat del módulo numpy) y ordenar el DataFrame por estaciones contaminantes y fecha.
Mostrar por pantalla las estaciones y los contaminantes disponibles en el DataFrame.

Crear una función que reciba una estación, un contaminante y un rango de fechas y devuelva una serie con las emisiones del contaminante dado en la estación y rango de fechas dado.
Mostrar un resumen descriptivo (mínimo, máximo, media, etc.) para cada contaminante.
Mostrar un resumen descriptivo para cada contaminante por distritos.

Crear una función que reciba una estación y un contaminante y devuelva un resumen descriptivo de las emisiones del contaminante indicado en la estación indicada.
Crear una función que devuelva las emisiones medias mensuales de un contaminante y un año dados para todos las
estaciones.

Crear un función que reciba una estación de medición y devuelva un DataFrame con las medias mensuales de los distintos tipos de contaminantes.
"""

#1 Generar un DataFrame con los datos de los cuatro archivos.
e2016 = pd.read_csv('emisiones-2016.csv', sep=';')
e2017 = pd.read_csv('emisiones-2017.csv', sep=';')
e2018 = pd.read_csv('emisiones-2018.csv', sep=';')
e2019 = pd.read_csv('emisiones-2019.csv', sep=';')

emisiones_df = pd.concat([e2016, e2017, e2018, e2019], ignore_index = True)

print(emisiones_df)
input("")

#2 Filtrar las columnas del DataFrame para quedarse con las columnas ESTACION, MAGNITUD, AÑO, MES y las correspondientes a los días D01, D02, etc.

df1 = emisiones_df[['ESTACION','MAGNITUD','ANO', 'MES']]
df2 = emisiones_df.iloc[:,7:70:2]

emisiones2_df = df1.merge(df2, how='inner', left_index=True, right_index=True)
print(emisiones2_df)

input("")


#3 Reestructurar el DataFrame para que los valores de los contaminantes de las columnas de los días aparezcan en una única columna.

data_columns = [col for col in emisiones2_df.columns if col.startswith('D')]
emission_data = emisiones2_df[[ 'ESTACION', 'MAGNITUD', 'ANO', 'MES'] + data_columns]

emisiones2_df = pd.melt(emission_data, id_vars=['ESTACION', 'MAGNITUD', 'ANO', 'MES'], var_name='DIA', value_name='EMISION')
emisiones2_df.sort_values(by=['ESTACION', 'MAGNITUD', 'ANO', 'MES', 'DIA'], inplace=True)
emisiones2_df['DIA'] = emisiones2_df['DIA'].str.replace('D', '')

print(emisiones2_df)

input("")


#4 Añadir una columna con la fecha a partir de la concatenación del año, el mes y el día (usar el módulo datetime).
emisiones2_df['ANO'] = emisiones2_df['ANO'].astype(str)
emisiones2_df['MES'] = emisiones2_df['MES'].astype(str)
emisiones2_df['DIA'] = emisiones2_df['DIA'].astype(str)

emisiones2_df['FECHA'] = emisiones2_df['ANO']+'-'+emisiones2_df['MES']+'-'+emisiones2_df['DIA']
emisiones2_df['FECHA'] = pd.to_datetime(emisiones2_df['FECHA'], format = '%Y-%m-%d', errors ='coerce')
print(emisiones2_df)

input("")


#5 Eliminar las filas con fechas no válidas (utilizar la función isnat del módulo numpy) y ordenar el DataFrame por estaciones contaminantes y fecha.

emisiones2_df = emisiones2_df[emisiones2_df['FECHA'].notna()]
print(emisiones2_df)

input("")


#6 Mostrar por pantalla las estaciones y los contaminantes disponibles en el DataFrame.

estaciones = emisiones2_df.ESTACION.unique()
contaminantes = emisiones2_df.MAGNITUD.unique()
print(f"Estaciones: {estaciones},\n\nContaminantes: {contaminantes}")

input("")


#7 Crear una función que reciba una estación, un contaminante y un rango de fechas y devuelva una serie con las emisiones del contaminante dado en la estación y rango de fechas dado.
def emisionesEstFechas(contaminante, estacion, fechaInicio, fechaFinal):
    fechaInicio = '2016-01-04'
    fechaFinal = '2016-01-08'
    df = emisiones2_df[(emisiones2_df['FECHA']>= fechaInicio) & (emisiones2_df['FECHA']<=fechaFinal)]
    df = df[df['ESTACION'] == estacion]
    df = df[df['MAGNITUD'] == contaminante]
    print(df)
    
emisionesEstFechas(contaminante = 1,estacion = 4,fechaInicio = 'a',fechaFinal = 'b')

input("")


#8 Mostrar un resumen descriptivo (mínimo, máximo, media, etc.) para cada contaminante.

contaminantes_df = emisiones2_df.groupby('MAGNITUD')
resumen = contaminantes_df['EMISION'].describe()
print(resumen)

input("")


#9 Mostrar un resumen descriptivo para cada contaminante por distritos.

distritos = emisiones2_df.groupby(['ESTACION','MAGNITUD'])
descripcion = distritos['EMISION'].describe()
print(descripcion)

input("")


#10 Crear una función que reciba una estación y un contaminante y devuelva un resumen descriptivo de las emisiones del contaminante indicado en la estación indicada.
def resumenCont(estacion, contaminante):
    df = emisiones2_df.loc[(emisiones2_df['ESTACION'] == estacion) & (emisiones2_df['MAGNITUD']==contaminante)]
    print(df)

resumenCont(estacion = 4, contaminante = 1)

input("")

#11 Crear una función que devuelva las emisiones medias mensuales de un contaminante y un año dados para todos las estaciones.

def mediaMesAnioCont(contaminante, mes, anio):

    df = emisiones2_df[(emisiones2_df['MES']== mes) & (emisiones2_df['ANO']==anio) & (emisiones2_df['MAGNITUD']==contaminante)]
    media = round(df['EMISION'].mean(), 2)
    print("\nMedia: ", media)

mediaMesAnioCont(contaminante=1,mes='1',anio='2016')

input("")



