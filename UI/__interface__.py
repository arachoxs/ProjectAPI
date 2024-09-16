import pandas as pd


def info_user():
    info = []
    while True:
        try:
            # Solicitar al usuario que ingrese un número
            info.append(int(input('Ingrese el numero de datos: ')))
            break  # Si el input es un número, salir del bucle
        except ValueError:
            # Si ocurre un ValueError (es decir, el input no es un número), mostrar un mensaje y repetir el bucle
            print("Eso no es un número válido. Inténtalo de nuevo.")

    info.append(input("Ingrese el nombre del municipio a buscar-> "))

    return info

def show_data(data_api, amount_to_show):
    # me permite mostrar toda la cantidad de datos
    print("\n\n")
    pd.set_option('display.max_rows', int(amount_to_show))
    print(data_api)
    
def frame_inf(data_api):
    #informacion general de lo que conforma el data frame
    print("numero de filas->", data_api.shape[0])
    print("numero de columnas->", data_api.shape[1])
    
    print("Nombre de las columnas->", data_api.columns.values.tolist())
    
    print("Tipo de datos de columna->\n",data_api.dtypes)
    
    #informacion sobre los valores faltantes en el data frame
    columnas_NA=data_api.columns[data_api.isnull().any()].tolist()

    print("Columns con valores faltantes-> ", columnas_NA)
    
    filas_con_na = data_api[data_api.isnull().any(axis=1)].index.tolist() 
        
    print("Numero de filas con valores faltantes -> ", len(filas_con_na))
    print("Indices de ejemplo con datos faltantes ->", filas_con_na[:5]) 
    
