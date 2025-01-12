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

# leer el archivo RAW_TIEMPOS_COSTOS

query = "SELECT * FROM RAW_TIEMPOS_COSTOS;"

tiempos_costos = pd.read_sql(query,conn)

print ("lectura de RAW_TIEMPOS_COSTOS exitosa")


# Realizar las transformaciones

# Transformación de fila para corregir nulo

tiempos_costos = tiempos_costos.drop(tiempos_costos.index[2015], axis=0)

# Convertir columna Fecha_trasporte en date (esto unifica a todas las fechas separadas por - en lugar barras)

tiempos_costos ['Fecha_Transporte'] = tiempos_costos ['Fecha_Transporte'].str.replace('-','/')





#Truncar tabla stage

cursor.execute ("TRUNCATE TABLE STG_TIEMPOS_COSTOS")

print ("TABLA STG_TIEMPOS_COSTOS TRUNCADA")

#insertando datos
for _, row in tiempos_costos.iterrows():
    cursor.execute('INSERT INTO STG_TIEMPOS_COSTOS (ID_Tiempo_Costos, ID_Ruta, Tiempo_Transporte_hrs, Costo_Total, Fecha_Transporte) VALUES (?,?,?,?,?)', row ['ID_Tiempo_Costos'],row ['ID_Ruta'], row ['Tiempo_Transporte_hrs'], row ['Costo_Total'], row ['Fecha_Transporte'])

#confirmar los cambios y cierre conexion    
conn.commit ()
cursor.close()
conn.close ()

print ("datos insertados exitosamente")

