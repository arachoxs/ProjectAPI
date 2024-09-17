import pandas as pd
import numpy as np


#Imputacion de datos

def type_casting(data_api):
    data_api.replace('N/A', np.nan, inplace=True) #reemplazo todos los "N/A" por nan debido a que el dataframe no los reconoce como texto
    data_api['edad'] = pd.to_numeric(data_api.edad) #convierte toda la columna de edad en datos numericos
    

def delete_nan(data_api):
    columnas_NA=data_api.columns[data_api.isnull().any()].tolist() #me devuelve la lista con todos las columnas con datos Nan
    data_api = data_api.dropna(subset=columnas_NA)
    return data_api

def fill_data(data_api):
    # Identificar las columnas que contienen valores NaN
    columnas_NA = data_api.columns[data_api.isnull().any()].tolist()
    
    # Aplicar ffill a las columnas identificadas
    data_api[columnas_NA] = data_api[columnas_NA].ffill()