import API.__DataAPI__ as DataAPI
import UI.__interface__ as interface

user = interface.info_user()
limite, departamento = user

data_api = DataAPI.get_data(limite, departamento)

while data_api.empty:
    user = interface.info_user()
    limite, departamento = user

    data_api = DataAPI.get_data(limite, departamento)

data_api = DataAPI.data_filter(data_api, "ciudad_municipio_nom", "departamento_nom", "edad",
                               "fuente_tipo_contagio", "estado")

interface.show_data(data_api, limite)
