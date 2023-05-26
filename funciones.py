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
    for indice in range(len(lista_jugadores)):
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
    False: en caso de que lista_original se encuentre vacía.
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
    False: en caso de que lista_original se encuentre vacía.
    path_final: tipo string -> la ruta incluyendo el nombre del jugador.
    '''
    if len(lista_original) == 0:
        print("Lista vacía.")
        return False   
    lista = lista_original[:]
    nombre_jugador = lista[indice]["nombre"]
    path_final = path + nombre_jugador.replace(" ","_") + ".csv"
    return path_final

def guardar_csv_jugador_stats(lista_original: list, indice: int, path: str):
    '''
    Esta función genera un .csv de los datos y estadísticas del jugador seleccionado por índice.
    ------------
    Parámetros
    lista_original: tipo list[dict] -> la lista original que se importó del JSON.
    indice: tipo int -> el índice del jugador que se quiere seleccionar.
    path: tipo string -> la ruta del directorio donde se quiere generar el archivo .csv.
    ------------
    Retorna:
    False: en caso de que lista_original se encuentre vacía.
    '''
    if len(lista_original) == 0:
        print("Lista vacía.")
        return False
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

def buscar_por_nombre(lista_original: list[dict], jugador: dict, nombre: str):
    '''
    Esta función busca a través de RegEx la coincidencia entre el param "nombre" y 
    el nombre del jugador pasado por param.
    -----------
    Parámetros:
    lista_original: tipo list[dict] -> la lista original que se importó del JSON.
    busqueda: tipo match.object | null -> el resultado de del re.match utilizado.
    '''
    if len(lista_original) == 0:
        print("Lista vacía.")
        return -1
    if nombre == " ":
        print("Ingrese un nombre válido.")
    else:  
        busqueda = re.search(f'{nombre}', jugador["nombre"], re.I)
        return busqueda
        

def mostrar_logros_por_busqueda(lista_original: list[dict], nombre: str):
    '''
    Esta función muestra los logros de todos los jugadores cuyos nombres coincidan con la búsqueda pasada por param.
    ------------
    lista_original: tipo list[dict] -> la lista original que se importó del JSON.
    nombre: tipo str -> string que posee el nombre o parte del nombre del jugador a buscar.
    ------------
    Retorna:
    False: en caso de que lista_original se encuentre vacía.    
    '''
    if len(lista_original) == 0:
        print("Lista vacía.")
        return False
    if nombre == " ":
        print("Ingrese un nombre válido.")
    else:
        lista = lista_original[:]
        flag_jugador = False
        for jugador in lista:
            busqueda = buscar_por_nombre(lista, jugador, nombre)
            if busqueda:
                flag_jugador = True
                print(jugador["nombre"] + "\n")
                for logro in jugador["logros"]:
                    print("- " + logro + "\n")       
        if flag_jugador == False:
            print("No existe jugador con ese nombre.")

def calcular_promedio_total(lista_original: list[dict], estadistica: str):
    '''
    Esta función calcula el promedio total de la estadística seleccionada.
    ------------
    Parámetros:
    lista_original: tipo list[dict] -> la lista original que se importó del JSON.
    estadistica: tipo string -> la key de la estadística para calcular el promedio.
    ------------
    Retorna:
    False: en caso de que lista_original se encuentre vacía. 
    promedio: tipo float -> el promedio calculado.
    '''
    if len(lista_original) == 0:
        print("Lista vacía.")
        return False
    lista = lista_original[:]
    if len(lista) <= 1:
        return lista
    contador = 0
    acumulador = 0
    if estadistica in lista[0]["estadisticas"].keys():
        for jugador in lista:
            acumulador += jugador["estadisticas"][estadistica]
            contador += 1
        promedio = acumulador / contador
        return promedio
    else:
        print("Estadística inexistente.")

def ordenar_lista_segun_key(lista_original:list, key_a_ordenar: str, flag_estadistica= False, orden_asc=True)->list:
    '''
    Esta función genera una lista ordenada según el param "key_a_ordenar" a través de un método de ordenamiento.
    -----------
    Parámetros:
    lista_original: tipo list[dict] -> la lista original que se importó del JSON.
    key_a_ordenar: tipo string -> la key cuyo valor se va a utilizar como el parámetro del ordenamiento.
    flag_estadistica: tipo bool - definido en False -> flag que determina si la key a ordenar se encuentra dentro de "estadisticas" o no.
    orden_asc: tipo bool - definido en True -> variable que determina si el orden es ascendente(True) o descendente(False)
    -----------
    Retorna:
    False: en caso de que lista_original se encuentre vacía. 
    lista: tipo list -> la lista ordenada.
    '''
    if len(lista_original) == 0:
        print("Lista vacía.")
        return False
    lista = lista_original[:]
    rango_a = len(lista)
    flag_swap = True
    contador = 0
    while(flag_swap):
        flag_swap = False
        rango_a = rango_a - 1
        for indice_A in range(rango_a):
            contador += 1
            if flag_estadistica == False:
                if orden_asc == True:   
                    if lista[indice_A][key_a_ordenar] > lista[indice_A+1][key_a_ordenar]:
                        lista[indice_A],lista[indice_A+1] = lista[indice_A+1],lista[indice_A]
                        flag_swap = True
                elif orden_asc == False:
                    if lista[indice_A][key_a_ordenar] < lista[indice_A+1][key_a_ordenar]:
                        lista[indice_A],lista[indice_A+1] = lista[indice_A+1],lista[indice_A]
                        flag_swap = True
            elif flag_estadistica == True:
                if orden_asc == True:   
                    if lista[indice_A]["estadisticas"][key_a_ordenar] > lista[indice_A+1]["estadisticas"][key_a_ordenar]:
                        lista[indice_A],lista[indice_A+1] = lista[indice_A+1],lista[indice_A]
                        flag_swap = True
                elif orden_asc == False:
                    if lista[indice_A]["estadisticas"][key_a_ordenar] < lista[indice_A+1]["estadisticas"][key_a_ordenar]:
                        lista[indice_A],lista[indice_A+1] = lista[indice_A+1],lista[indice_A]
                        flag_swap = True
    return lista

def mostrar_estadistica_por_jugador_ordenado(lista_original: list[dict], key_orden: str, estadistica: str):
    '''
    Esta función muestra un listado ordenado según "key_orden", del nombre de los jugadores 
    junto a la estadística pasada por param.
    -----------
    Parámetros:
    lista_original: tipo list[dict] -> la lista original que se importó del JSON.
    key_orden: tipo string -> la key cuyo valor se va a utilizar como el parámetro del ordenamiento.
    estadistica: tipo string -> la key cuyo valor se quiere mostrar en el listado.
    -----------
    Retorna:
    False: en caso de que lista_original se encuentre vacía. 
    lista_jugador_nombre: tipo list[list] -> una lista de listas que posee el nombre y el valor de la estadística.  
    '''   
    if len(lista_original) == 0:
        print("Lista vacía.")
        return False
    lista_aux = lista_original[:]
    lista = ordenar_lista_segun_key(lista_aux, key_orden)
    lista_jugador_nombre = []
    for jugador in lista:
        lista_jugador_nombre.append([jugador["nombre"], jugador["estadisticas"][estadistica]])
    estadistica_str = estadistica.replace("_"," ").capitalize()
    for jugador in lista_jugador_nombre:
        mensaje = "Jugador: {0}\n{1}: {2}\n".format(
            jugador[0],
            estadistica_str,
            jugador[1])
        print(mensaje)
    return lista_jugador_nombre    

def mostrar_jugador_hof(lista_original: list[dict], nombre: str):
    '''
    Esta función muestra un listado de jugadores, junto a su nombre y si se encuentran o no en el salon de la fama. )HOF)
    ------------
    lista_original: tipo list[dict] -> la lista original que se importó del JSON.
    nombre: tipo str -> string que posee el nombre o parte del nombre del jugador a buscar.
    ------------
    Retorna:
    False: en caso de que lista_original se encuentre vacía.    
    '''
    if len(lista_original) == 0:
        print("Lista vacía.")
        return False
    if nombre == " ":
        print("Ingrese un nombre válido.")
    else:
        lista = lista_original[:]
        logro_hof = "Miembro del Salon de la Fama del Baloncesto"
        lista_jugadores_hof = []
        flag_jugador = False
        for jugador in lista:
            busqueda = buscar_por_nombre(lista, jugador, nombre)
            if busqueda:
                flag_jugador = True
                for logro in jugador["logros"]:
                    if logro == logro_hof:
                        lista_jugadores_hof.append([jugador["nombre"],"Si"])
                        break
                else:
                    lista_jugadores_hof.append([jugador["nombre"],"No"])
        mensaje = ""
        if flag_jugador == False:
            print("No existe jugador con ese nombre.")
        else:
            for jugador in lista_jugadores_hof:
                mensaje += "Nombre: {0}\nSe encuentra dentro del HOF?: {1}\n\n".format(
                    jugador[0],
                    jugador[1]
                )
            print(mensaje)

def mostrar_jugador_mayor_stat(lista_original: list[dict], estadistica: str):
    '''
    Esta función muestra al jugador que posea el mayor valor de la estadística deseada.
    -----------
    Parámetros:
    lista_original: tipo list[dict] -> la lista original que se importó del JSON.
    estadistica: tipo string -> la key de la estadística a chequear.
    ------------
    Retorna:
    False: en caso de que lista_original se encuentre vacía.
    '''
    if len(lista_original) == 0:
        print("Lista vacía.")
        return False
    lista = lista_original[:]
    estadistica_str = estadistica.replace("_"," ")
    lista_jugador_mayor_valor_stat = ["",-1]
    for jugador in lista:
        if jugador["estadisticas"][estadistica] > lista_jugador_mayor_valor_stat[1]:
            lista_jugador_mayor_valor_stat = [jugador["nombre"], jugador["estadisticas"][estadistica]]
    print("El jugador con más {0} es {1}, con {2}".format(
        estadistica_str, lista_jugador_mayor_valor_stat[0], lista_jugador_mayor_valor_stat[1] 
    ))
    
def mostrar_jugadores_promediado_mas_stat(lista_original: list[dict], estadistica: str, valor_stat: float):
    '''
    Esta función muestra al jugador que posea el mayor valor de la estadística deseada.
    ------------
    Parámetros:
    lista_original: tipo list[dict] -> la lista original que se importó del JSON.
    estadistica: tipo string -> la key de la estadística a chequear.
    ------------
    Retorna:
    False: en caso de que lista_original se encuentre vacía.
    '''
    if len(lista_original) == 0:
        print("Lista vacía.")
        return False
    lista = lista_original[:]
    estadistica_str = estadistica.replace("_"," ")
    lista_jugadores_prom_mayor = []
    for jugador in lista:
        if jugador["estadisticas"][estadistica] > valor_stat:
            lista_jugadores_prom_mayor.append([jugador["nombre"], jugador["estadisticas"][estadistica]])
    if not lista_jugadores_prom_mayor:
        print("Ningún jugador posee un mayor valor que el ingresado en {0}".format(estadistica_str))
    else:
        mensaje = "\nValor Ingresado: {0}\nJugadores que superar ese valor en {1}:\n".format(valor_stat, estadistica_str)
        for jugador in lista_jugadores_prom_mayor:
            mensaje += "{0} - {1}\n".format(jugador[0], jugador[1])
        print(mensaje)
    
def generar_promedio_segun_stat_menos_peor_valor(lista_original: list[dict], estadistica: str):
    '''
    Esta función genera el promedio de la suma de la estadística elegida, sin tener en cuenta el stat del jugador que peor promedia.
    ------------
    Parámetros:
    lista_original: tipo list[dict] -> la lista original que se importó del JSON.
    estadistica: tipo string -> la key de la estadística a chequear.
    ------------
    Retorna:
    False: en caso de que lista_original se encuentre vacía.
    promedio: tipo float -> el valor del promedio calculado.
    '''
    if len(lista_original) == 0:
        print("Lista vacía.")
        return False
    lista_aux = lista_original[:]
    contador = 0
    acumulador = 0
    if estadistica in lista_aux[0]["estadisticas"].keys():
        lista_ordenada = ordenar_lista_segun_key(lista_aux,estadistica, True, False)
        lista_ordenada.pop()
        for jugador in lista_ordenada:
            acumulador += jugador["estadisticas"][estadistica]
            contador += 1
        promedio = acumulador / contador
        return promedio
    else:
        print("Estadística inexistente.")

    

        
        
    