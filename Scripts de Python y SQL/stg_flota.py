import pyodbc
import csv
import pandas as pd
import datetime as datetime



#configurar la conexión

connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=DESKTOP-J02QHHP\\SQLSERVERXP2019;"
    "DATABASE=EcoLogistics;"
    "Trusted_Connection=yes;"
)


conn = pyodbc.connect (connection_string)

print ("conexión exitosa")


cursor = conn.cursor()

#leer el archivo RAW_FLOTA

query = "SELECT * FROM RAW_FLOTA;"

flota = pd.read_sql(query,conn)

print ("lectura de RAW_FLOTA exitosa")


#Realizar las transformaciones

# Eliminar str (KG) de la columna capacidad_carga (Kg)

flota ['Capacidad_Carga']= flota['Capacidad_Carga'].str.extract('(\d+)')

# Convertir Columna en INT

flota ['Capacidad_carga'] = flota ['Capacidad_Carga'].astype (int)

# Eliminar fila dummy text

flota.drop(index=30, inplace = True)


#Truncar tabla stage

cursor.execute ("TRUNCATE TABLE STG_FLOTA")

print ("TABLA STG_FLOTA TRUNCADA")

#insertando datos
for _, row in flota.iterrows():
    cursor.execute('INSERT INTO STG_FLOTA (Id_Flota, Tipo_Vehiculo, Capacidad_Carga, Consumo_promedio, Emisiones_CO2, Anio_Fabricacion, Kilometraje) VALUES (?,?,?,?,?,?,?)', row ['Id_Flota'],row ['Tipo_Vehiculo'], row ['Capacidad_Carga'], row ['Consumo_promedio'], row ['Emisiones_CO2'], row ['Año_Fabricacion'], row ['Kilometraje'])

#confirmar los cambios y cierre conexion    
conn.commit ()
cursor.close()
conn.close ()

print ("datos insertados exitosamente")

