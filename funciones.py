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

def mostrar_jugadores_dreamteam(lista_original: list[dict]):
    '''
    Esta función muestra un listado de jugadores, con su nombre y posición.
    ---------
    Parámetros:
    lista_original: tipo list[dict] -> la lista original que se importó del JSON.
    ---------
    Devuelve:
    False: en caso de que lista_original se encuentre vacía.
    '''
    if not lista_original:
        print("La lista original se encuentra vacia.")
        return False
    lista_jugadores = lista_original[:]
    lista_jugadores_nombre_pos = []
    for jugador in lista_jugadores:
        lista_jugadores_nombre_pos.append([jugador["nombre"], jugador["posicion"]])
    for jugador in lista_jugadores_nombre_pos:
        mensaje = "{0} - {1}".format(jugador[0],jugador[1])
        print(mensaje + "\n")
