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

#leer el archivo STG_CARGAS

query = "SELECT * FROM STG_CARGAS;"

cargas = pd.read_sql(query,conn)

print ("lectura de STG_CARGAS exitosa")


#Eliminar Duplicado

cargas = cargas.drop_duplicates()


#Truncar tabla INT

cursor.execute ("TRUNCATE TABLE INT_CARGAS")

print ("TABLA INT_CARGAS TRUNCADA")

#insertando datos
for _, row in cargas.iterrows():
    cursor.execute('INSERT INTO INT_CARGAS (ID_Carga, Tipo_Carga, Peso_Kg, Volumen_m3, Cliente) VALUES (?,?,?,?,?)', row ['ID_Carga'],row ['Tipo_Carga'], row ['Peso_Kg'], row ['Volumen_m3'], row ['Cliente'])

#confirmar los cambios y cierre conexion    
conn.commit ()
cursor.close()
conn.close ()

print ("datos insertados exitosamente")

