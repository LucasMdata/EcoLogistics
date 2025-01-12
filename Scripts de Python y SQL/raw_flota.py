import pyodbc
import csv
import pandas as pd

#leer el archivo CSV

file_path = 'C:/Users/Lindos/Desktop/Trabajo integrador Quales/flota.csv'

data = pd.read_csv(file_path)

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

#Truncar tabla stage

cursor.execute ("TRUNCATE TABLE RAW_FLOTA")

print ("TABLA RAW_FLOTA TRUNCADA")

#insertando datos
for _, row in data.iterrows():
    cursor.execute('INSERT INTO RAW_FLOTA (Id_Flota, Tipo_Vehiculo, Capacidad_Carga, Consumo_promedio, Emisiones_CO2, Año_Fabricacion, Kilometraje) VALUES (?,?,?,?,?,?,?)', row ['ID_Flota'],row ['Tipo_Vehículo'], row ['Capacidad_Carga (kg)'], row ['Consumo_Promedio (kWh/km o L/100km)'], row ['Emisiones_CO2 (g/km)'], row ['Año_Fabricación'], row ['Kilometraje'])

#confirmar los cambios y cierre conexion    
conn.commit ()
cursor.close()
conn.close ()

print ("datos insertados exitosamente")

