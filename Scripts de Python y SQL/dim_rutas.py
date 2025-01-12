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

# leer el archivo INT_RUTAS

query = "SELECT * FROM INT_RUTAS;"

rutas = pd.read_sql(query,conn)

print ("lectura de INT_RUTAS exitosa")


#Eliminar duplicados

rutas = rutas.drop_duplicates()


#Eliminar Nulos

rutas = rutas.dropna(subset=['ID_Ruta'])

#insertando datos
for _, row in rutas.iterrows():
    cursor.execute('INSERT INTO DIM_RUTAS (ID_Ruta, Origen, ID_Flota, ID_Carga, Destino, Distancia_Km, Tipo_Terreno) VALUES (?,?,?,?,?,?,?)', row ['ID_Ruta'],row ['Origen'], row ['ID_Flota'], row ['ID_Carga'], row ['Destino'], row ['Distancia_Km'], row ['Tipo_Terreno'])

#confirmar los cambios y cierre conexion    
conn.commit ()
cursor.close()
conn.close ()

print ("datos insertados exitosamente")
