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

#leer el archivo STG_FLOTA

query = "SELECT * FROM STG_FLOTA;"

flota = pd.read_sql(query,conn)

print ("lectura de STG_FLOTA exitosa")


#Eliminar duplicados

flota = flota.drop_duplicates()


#Truncar tabla INT

cursor.execute ("TRUNCATE TABLE INT_FLOTA")

print ("TABLA INT_FLOTA TRUNCADA")

#insertando datos
for _, row in flota.iterrows():
    cursor.execute('INSERT INTO INT_FLOTA (Id_Flota, Tipo_Vehiculo, Capacidad_Carga, Consumo_promedio, Emisiones_CO2, Anio_Fabricacion, Kilometraje) VALUES (?,?,?,?,?,?,?)', row ['Id_Flota'],row ['Tipo_Vehiculo'], row ['Capacidad_Carga'], row ['Consumo_promedio'], row ['Emisiones_CO2'], row ['Anio_Fabricacion'], row ['Kilometraje'])

#confirmar los cambios y cierre conexion    
conn.commit ()
cursor.close()
conn.close ()

print ("datos insertados exitosamente")

