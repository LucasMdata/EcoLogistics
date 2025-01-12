import pyodbc
import csv
import pandas as pd

#leer el archivo CSV

file_path = 'C:/Users/Lindos/Desktop/Trabajo integrador Quales/rutas.csv'

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

#Truncar RAW

cursor.execute ("TRUNCATE TABLE RAW_RUTAS")

print ("TABLA RAW_RUTAS TRUNCADA")

#insertando datos
for _, row in data.iterrows():
    cursor.execute('INSERT INTO RAW_RUTAS (ID_Ruta, Origen, ID_Flota, ID_Carga, Destino, Distancia_Km, Tipo_terreno, DUMMY_Column)   VALUES (?,?,?,?,?,?,?,?)', row ['ID_Ruta'],row ['Origen'],row ['ID_Flota'], row ['ID_Carga'], row ['Destino'], row ['Distancia (km)'], row ['Tipo_Terreno'], row ['DUMMY_Column'])

#confirmar los cambios y cierre conexion    
conn.commit ()
cursor.close()
conn.close ()

print ("datos insertados exitosamente")

