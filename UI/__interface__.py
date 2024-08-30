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
    pd.set_option('display.max_rows', int(amount_to_show))
    print(data_api.to_string(col_space=20))
