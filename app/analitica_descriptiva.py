import datetime
import pandas as pd
import numpy as np
import csv

file_name = "data/data_base.csv"

def update(file_name):
    datos_pandas = leer_datos(file_name)
    funcion_Maximo(datos_pandas, file_name)
    funcion_Minimo(datos_pandas, file_name)
    funcion_Mediana(datos_pandas, file_name)
    funcion_Promedio(datos_pandas, file_name)
    funcion_Desviacion(datos_pandas, file_name)
    funcion_Varianza(datos_pandas, file_name)
   """
    Inserte aqui las otras funciones.
    funcion_Minimo ()
    funcion_Mediana ()
    funcion_Promedio ()
    funcion_Desviacion ()
    funcion_Varianza ()
    """
    datos_graficar = leer_datos(file_name)
    return datos_graficar


def funcion_Maximo(datos, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    maximo_valor = max(valores_temperatura)
    dato_guardar = [1, date_string, "Maximo", maximo_valor]
    guardar(dato_guardar, file_name)

def funcion_Minimo(data, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    minimo_valor = min(valores_temperatura)
    dato_guardar = [1, date_string, "Minimo", minimo_valor]
    guardar(dato_guardar, file_name)

    def funcion_Mediana(data, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    valor_mediana = np.median(valores_temperatura)
    dato_guardar = data = [1, date_string, "Mediana", valor_mediana]
    guardar(dato_guardar, file_name)
    
def funcion_Promedio(data, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    valor_promedio = np.mean(valores_temperatura)
    dato_guardar = data = [1, date_string, "Promedio", valor_promedio]
    guardar(dato_guardar, file_name)

def funcion_Desviacion(data, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]    
    valor_desviacion = np.std(valores_temperatura)    
    dato_guardar = data = [1, date_string, "Desviacion", valor_desviacion]
    guardar(dato_guardar, file_name)

def funcion_Varianza(data, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]   
    valor_varianza = np.var(valores_temperatura)
    dato_guardar = data = [1, date_string, "Varianza", valor_varianza]
    guardar(dato_guardar, file_name)



    

def guardar(data, file_name):    
    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(data)

def leer_datos(file_name):
    datos_pandas = pd.read_csv(file_name, index_col=0, parse_dates=True)
    return datos_pandas