import datetime
import pandas as pd
import numpy as np
import csv
"""
file_name = "data/data_base.csv"
"""
def update(file_name):
    datos_pandas = leer_datos(file_name)
    funcion_maximo(datos_pandas)
    funcion_minimo(datos_pandas)
    funcion_Mediana(datos_pandas)
    funcion_Promedio(datos_pandas)
    funcion_Desviacion(datos_pandas)
    funcion_Varianza(datos_pandas)
   
    datos_graficar = leer_datos(file_name)
    return datos_graficar


def funcion_maximo(datos):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    
    resultado_max = max(valores_temperatura)
    
    dato_guardar = [1, date_string, "Maximo", resultado_max]
    guardar(dato_guardar, file_name)


def funcion_minimo(datos):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    
    resultado_min = min(valores_temperatura)
    
    dato_guardar = [1, date_string, "Minimo", resultado_min]
    guardar(dato_guardar, file_name)

def funcion_Promedio(datos):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    
    resultado_promedio = np.mean(valores_temperatura)
    
    dato_guardar = data = [1, date_string, "Promedio", resultado_promedio]
    guardar(dato_guardar, file_name)

def funcion_Mediana(datos):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    
    resultado_mediana = np.median(valores_temperatura)
    
    dato_guardar = data = [1, date_string, "Mediana", resultado_mediana]
    guardar(dato_guardar, file_name)
    

def funcion_Varianza(datos):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
   
    resultado_varianza = np.var(valores_temperatura)

    dato_guardar = data = [1, date_string, "Varianza", resultado_varianza]
    guardar(dato_guardar, file_name)

def funcion_Desviacion(datos):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    
    resultado_desviacion = np.std(valores_temperatura)
    
    dato_guardar = data = [1, date_string, "Desviacion", resultado_desviacion]
    guardar(dato_guardar, file_name)

    

def guardar(data, file_name):    
    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(data)

def leer_datos(file_name):
    datos_pandas = pd.read_csv(file_name, index_col=0, parse_dates=True)
    return datos_pandas