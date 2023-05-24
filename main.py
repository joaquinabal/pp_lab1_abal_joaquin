import json
import re

def leer_archivo(ruta:str):
    '''
    Esta función lee un archivo json y lo devuelve como una lista.
    
    Parametro:
    ruta: de tipo string. es la ruta en donde se encuentra el archivo JSON a leer.
    
    Devuelve: una lista que posee el contenido del archivo JSON.
    '''
    with open(ruta, 'r') as archivo:
        diccionario = json.load(archivo)
    return diccionario["jugadores"]




path_JSON = "Parcial\dt.json"

lista_juegos_JSON = leer_archivo(path_JSON)