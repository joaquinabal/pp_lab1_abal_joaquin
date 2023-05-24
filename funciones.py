import json
import re

def leer_archivo(ruta:str):
    '''
    Esta función lee un archivo json y lo devuelve como una lista.
    ------------
    Parametro:
    ruta: de tipo string. es la ruta en donde se encuentra el archivo JSON a leer.
    ------------
    Devuelve: una lista que posee el contenido del archivo JSON.
    '''
    with open(ruta, 'r') as archivo:
        diccionario = json.load(archivo)
    return diccionario["jugadores"]

def mostrar_jugadores_dreamteam(lista_original: list[dict], flag_indice: bool):
    '''
    Esta función muestra un listado de jugadores, con su nombre y posición.
    ---------
    Parámetros:
    lista_original: tipo list[dict] -> la lista original que se importó del JSON.
    flag_indice: tipo bool -> una flag que permite mostrar, o no, el indice correspondiente al jugador.
    ---------
    Devuelve:
    False: en caso de que lista_original se encuentre vacía.
    '''
    if not lista_original:
        print("La lista original se encuentra vacia.")
        return False
    lista_jugadores = lista_original[:]
    lista_jugadores_nombre_pos = []
    for indice in range(len(lista_jugadores) - 1):
        lista_jugadores_nombre_pos.append([indice, lista_jugadores[indice]["nombre"], lista_jugadores[indice]["posicion"]])
    for jugador in lista_jugadores_nombre_pos:
        if not flag_indice:
            mensaje = "{0} - {1}\n".format(jugador[1],jugador[2])
        else:
            mensaje = "{0} - {1} - {2}\n".format(jugador[0],jugador[1],jugador[2])   
        print(mensaje + "\n")
        
def mostrar_estadisticas(lista_original: list[dict], indice: int):
    if not lista_original:
        print("La lista original se encuentra vacia.")
        return False
    lista_jugadores = lista_original[:]
    mensaje = """
    Estadísticas de {12}:
    
    Temporadas: {0}
    Puntos Totales: {1} 
    Promedio de Puntos por Partido: {2} 
    Rebotes Totales: {3} 
    Promedio de Rebotes Por Partido: {4} 
    Asistencias Totales: {5}
    Promedio de Asistencias Por Partido: {6} 
    Robos Totales: {7} 
    Bloqueos Totales: {8} 
    Porcentaje de Tiros de Campo: {9}% 
    Porcentaje de Tiros Libres:  {10}%
    Porcentaje de Tiros Triples:  {11}%
    """.format(
        lista_jugadores[indice]["estadisticas"]["temporadas"],
        lista_jugadores[indice]["estadisticas"]["puntos_totales"],
        lista_jugadores[indice]["estadisticas"]["promedio_puntos_por_partido"],
        lista_jugadores[indice]["estadisticas"]["rebotes_totales"],
        lista_jugadores[indice]["estadisticas"]["promedio_rebotes_por_partido"],
        lista_jugadores[indice]["estadisticas"]["asistencias_totales"],
        lista_jugadores[indice]["estadisticas"]["promedio_asistencias_por_partido"],
        lista_jugadores[indice]["estadisticas"]["robos_totales"],
        lista_jugadores[indice]["estadisticas"]["bloqueos_totales"],
        lista_jugadores[indice]["estadisticas"]["porcentaje_tiros_de_campo"],
        lista_jugadores[indice]["estadisticas"]["porcentaje_tiros_libres"],
        lista_jugadores[indice]["estadisticas"]["porcentaje_tiros_triples"],
        lista_jugadores[indice]["nombre"]
    )
    return mensaje
