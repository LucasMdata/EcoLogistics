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

#leer el archivo RAW_CARGAS

query = "SELECT * FROM RAW_CARGAS;"

cargas = pd.read_sql(query,conn)

print ("lectura de RAW_CARGAS exitosa")


#Realizar las transformaciones

# Colocar todas las palabras CLIENTE POR Clientes

cargas ['Cliente'] = cargas ['Cliente'].str.title()

cargas ['Cliente'] = cargas ['Cliente'].str.replace('Client ','Cliente ')

cargas ['Cliente'] = cargas ['Cliente'].str.replace('Cliente_','Cliente ')

cargas ['Cliente'] = cargas ['Cliente'].str.strip()


#Truncar tabla stage

cursor.execute ("TRUNCATE TABLE STG_CARGAS")

print ("TABLA STG_CARGAS TRUNCADA")

#insertando datos
for _, row in cargas.iterrows():
    cursor.execute('INSERT INTO STG_CARGAS (ID_Carga, Tipo_Carga, Peso_Kg, Volumen_m3, Cliente) VALUES (?,?,?,?,?)', row ['ID_Carga'],row ['Tipo_Carga'], row ['Peso_Kg'], row ['Volumen_m3'], row ['Cliente'])

#confirmar los cambios y cierre conexion    
conn.commit ()
cursor.close()
conn.close ()

print ("datos insertados exitosamente")

