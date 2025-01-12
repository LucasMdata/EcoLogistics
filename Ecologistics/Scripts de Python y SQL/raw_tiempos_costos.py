import pyodbc
import csv
import pandas as pd

#leer el archivo CSV

file_path = 'C:/Users/Lindos/Desktop/Trabajo integrador Quales/tiempos_costos.csv'

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

cursor.execute ("TRUNCATE TABLE RAW_TIEMPOS_COSTOS")

print ("TABLA RAW_TIEMPOS_COSTOS TRUNCADA")


#insertando datos
for _, row in data.iterrows():
    cursor.execute('INSERT INTO RAW_TIEMPOS_COSTOS (ID_Tiempo_Costos, ID_Ruta, Tiempo_Transporte_hrs, Costo_Total, Fecha_Transporte) VALUES (?,?,?,?,?)', row ['ID_Tiempo_Costo'],row ['ID_Ruta'], row ['Tiempo_Transporte (hrs)'], row ['Costo_Total ($)'], row ['Fecha_Transporte'])

#confirmar los cambios y cierre conexion    
conn.commit ()
cursor.close()
conn.close ()

print ("datos insertados exitosamente")

