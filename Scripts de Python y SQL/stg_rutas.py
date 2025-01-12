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

# leer el archivo RAW_RUTAS

query = "SELECT * FROM RAW_RUTAS;"

rutas = pd.read_sql(query,conn)

print ("lectura de RAW_RUTAS exitosa")


# Realizar las transformaciones

# Eliminar columna Dummy_Column

rutas = rutas.drop(['DUMMY_Column'], axis =1)

# Colocar primer letra en mayuscula en columna Tipo_terreno

rutas ['Tipo_Terreno'] = rutas ['Tipo_Terreno'].str.title()


#Truncar tabla stage

cursor.execute ("TRUNCATE TABLE STG_RUTAS")

print ("TABLA STG_RUTAS TRUNCADA")

#insertando datos
for _, row in rutas.iterrows():
    cursor.execute('INSERT INTO STG_RUTAS (ID_Ruta, Origen, ID_Flota, ID_Carga, Destino, Distancia_Km, Tipo_Terreno) VALUES (?,?,?,?,?,?,?)', row ['ID_Ruta'],row ['Origen'], row ['ID_Flota'], row ['ID_Carga'], row ['Destino'], row ['Distancia_Km'], row ['Tipo_Terreno'])

#confirmar los cambios y cierre conexion    
conn.commit ()
cursor.close()
conn.close ()

print ("datos insertados exitosamente")

