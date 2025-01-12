import pyodbc
import csv
import pandas as pd

#leer el archivo CSV

file_path = 'C:/Users/Lindos/Desktop/Trabajo integrador Quales/cargas.csv'

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

#Truncar tabla RAW

cursor.execute ("TRUNCATE TABLE RAW_CARGAS")

print ("TABLA RAW_CARGAS TRUNCADA")

#insertando datos
for _, row in data.iterrows():
    cursor.execute('INSERT INTO RAW_CARGAS (ID_Carga, Tipo_Carga, Peso_Kg, Volumen_m3, Cliente) VALUES (?,?,?,?,?)', row ['ID_Carga'],row ['Tipo_Carga'], row ['Peso (kg)'], row ['Volumen (m³)'], row ['Cliente'])

#confirmar los cambios y cierre conexion    
conn.commit ()
cursor.close()
conn.close ()

print ("datos insertados exitosamente")

