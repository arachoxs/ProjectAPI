import API.__DataAPI__ as DataAPI
import UI.__interface__ as interface
import Datacleaning.__datacleaning__ as cleaning

user = interface.info_user()
limite, departamento = user

data_api = DataAPI.get_data(limite, departamento)

while data_api.empty:
    user = interface.info_user()
    limite, departamento = user

    data_api = DataAPI.get_data(limite, departamento)

data_api = DataAPI.data_filter(data_api, "ciudad_municipio_nom", "departamento_nom", "edad",
                               "fuente_tipo_contagio", "estado")

cleaning.type_casting(data_api) 

interface.frame_inf(data_api)

interface.show_data(data_api, limite)

""" Tecnica de eliminacion de datos nan 
data_api=cleaning.delete_nan(data_api)

interface.show_data(data_api, limite)

"""

""" tecnica de imputacion de datos con el dato siguiente -error-


"""
cleaning.fill_data(data_api)
interface.show_data(data_api,limite)





