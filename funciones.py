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
        
def validacion_menu(numero) -> bool:
    '''
    Esta función busca validar el numero ingresado para que sea apto para el menú.(1-20,23)
    -----------
    Parámetros:
    numero: tipo int -> el numero que se evaluará la validación.
    -----------
    Retorna:
    True: En caso que haya coincidido el re.match.
    False: En caso que no haya coincidido.
    '''
    validacion = re.match(r'[1]?[0-9]{1}$|20|23', numero)
    if validacion:
        return True
    else:
        return False
                

def mostrar_estadisticas(lista_original: list[dict], indice: int):
    '''
    Esta función muestra las estadísticas por consola del jugador elegído según su índice.
    -----------
    Parámetros:
    lista_original: tipo list[dict] -> la lista original que se importó del JSON.
    indice: tipo int -> el índice del jugador que se quiere seleccionar.
    -----------
    Retorna:
    mensaje: tipo string -> el string que contiene las estadisticas del jugador.
    '''
    
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

def generar_path_jugador(lista_original: list, indice: int, path: str):
    '''
    Esta función genera una ruta que incluye el nombre del jugador seleccionado por indice.
    --------------
    Parámetros:
    lista_original: tipo list[dict] -> la lista original que se importó del JSON.
    indice: tipo int -> el índice del jugador que se quiere seleccionar.
    path: tipo string -> la ruta del directorio donde se quiere generar el path.
    --------------
    Retorna:
    path_final: tipo string -> la ruta incluyendo el nombre del jugador.
    '''
    if len(lista_original) == 0:
        print("Lista vacía.")
        return -1   
    lista = lista_original[:]
    nombre_jugador = lista[indice]["nombre"]
    path_final = path + nombre_jugador.replace(" ","_") + ".csv"
    return path_final

def guardar_csv_jugador_stats(lista_original: list, indice: int, path: str):
    '''
    Esta función genera un .csv de los datos y estadísticas del jugador seleccionado por índice.
    ------------
    lista_original: tipo list[dict] -> la lista original que se importó del JSON.
    indice: tipo int -> el índice del jugador que se quiere seleccionar.
    path: tipo string -> la ruta del directorio donde se quiere generar el archivo .csv.
    ------------
    Retorna:
    No retorna nada.
    '''
    if len(lista_original) == 0:
        print("Lista vacía.")
        return -1
    lista = lista_original[:]
    lista_keys = ["nombre","posicion"]
    lista_valores_stats = [lista[indice]["nombre"], lista[indice]["posicion"]]
    lista_keys.extend(lista[indice]["estadisticas"].keys())
    for value in lista[indice]["estadisticas"].values():
        lista_valores_stats.append(str(value))
    lista_valores_stats_string = ",".join(lista_valores_stats)
    lista_keys_string = ",".join(lista_keys)
    datos_para_csv = lista_keys_string + "\n" + lista_valores_stats_string
    print(datos_para_csv)
    with open(path, "w") as archivo:
        archivo.writelines([datos_para_csv])
    print("el archivo fue creado en {0}".format(path))

def mostrar_logros_por_busqueda(lista_original: list[dict], nombre: str):
    if len(lista_original) == 0:
        print("Lista vacía.")
        return -1
    lista = lista_original[:]
    flag_jugador = False
    for jugador in lista:
        busqueda = re.search(f'{nombre}', jugador["nombre"], re.I)
        if busqueda:
            flag_jugador = True
            print(jugador["nombre"] + "\n")
            for logro in jugador["logros"]:
                print("- " + logro + "\n")       
    if flag_jugador == False:
        print("No existe jugador con ese nombre.")