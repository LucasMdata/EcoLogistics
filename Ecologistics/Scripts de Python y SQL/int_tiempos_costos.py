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

# leer el archivo STG_TIEMPOS_COSTOS

query = "SELECT * FROM STG_TIEMPOS_COSTOS;"

tiempos_costos = pd.read_sql(query,conn)

print ("lectura de STG_TIEMPOS_COSTOS exitosa")



#Eliminar duplicados

tiempos_costos = tiempos_costos.drop_duplicates()

#Truncar tabla INT

cursor.execute ("TRUNCATE TABLE INT_TIEMPOS_COSTOS")

print ("TABLA INT_TIEMPOS_COSTOS TRUNCADA")

#insertando datos
for _, row in tiempos_costos.iterrows():
    cursor.execute('INSERT INTO INT_TIEMPOS_COSTOS (ID_Tiempo_Costos, ID_Ruta, Tiempo_Transporte_hrs, Costo_total, Fecha_Transporte) VALUES (?,?,?,?,?)', row ['ID_Tiempo_Costos'],row ['ID_Ruta'], row ['Tiempo_Transporte_hrs'], row ['Costo_Total'], row ['Fecha_Transporte'])

#confirmar los cambios y cierre conexion    
conn.commit ()
cursor.close()
conn.close ()

print ("datos insertados exitosamente")
