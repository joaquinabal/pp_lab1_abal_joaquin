import re

from funciones import (
    leer_archivo,
    mostrar_jugadores_dreamteam,
    mostrar_estadisticas,
    validacion_menu,
    guardar_csv_jugador_stats,
    generar_path_jugador
)

menu = "{0}\n{1}\n{2}\n{3}\n{4} ".format(
"----------------------------------------------------------------",
"""1- Mostrar la lista de todos los jugadores del Dream Team. Con el formato:
Nombre Jugador - Posición. Ejemplo:
Michael Jordan - Escolta\n""",
"""
2- Permitir al usuario seleccionar un jugador por su índice y mostrar sus estadísticas completas, 
incluyendo temporadas jugadas, puntos totales, promedio de puntos por partido, rebotes totales, 
promedio de rebotes por partido, asistencias totales, promedio de asistencias por partido, robos totales, 
bloqueos totales, porcentaje de tiros de campo, porcentaje de tiros libres y porcentaje de tiros triples.
""",
"""
3- Después de mostrar las estadísticas de un jugador seleccionado por el usuario, 
permite al usuario guardar las estadísticas de ese jugador en un archivo CSV. 
El archivo CSV debe contener los siguientes campos: nombre, posición, temporadas, 
puntos totales, promedio de puntos por partido, rebotes totales, promedio de rebotes por partido, 
asistencias totales, promedio de asistencias por partido, robos totales, bloqueos totales, 
porcentaje de tiros de campo, porcentaje de tiros libres y porcentaje de tiros triples.

""",
"Ingrese la opción deseada" 
)

path_JSON = "Parcial\dt.json"
path_stats_jugadores = 'Parcial/stats_jugadores/'
indice = None
lista_dreamteam= leer_archivo(path_JSON)

while True:
    respuesta = input(menu)
    while not respuesta.isnumeric() or validacion_menu(respuesta) == False:
        respuesta = input("Opcion Invalida. Ingrese nuevamente: ")
    match(int(respuesta)):
        case 1:
            mostrar_jugadores_dreamteam(lista_dreamteam, False)
            
        case 2:
            mostrar_jugadores_dreamteam(lista_dreamteam, True)
            indice = input("Ingrese el indice del jugador a mostrar las estadísticas. ")
            mensaje = mostrar_estadisticas(lista_dreamteam, int(indice))
            print(mensaje)
                                 
            
        case 3:
            if not indice:
                print("Primero debes seleccionar a un jugador, ingresando desde la opción 2.")
            else:    
                pregunta = input("Quiere exportar las estadísticas del jugador en un .csv? (si/no)")
                if re.match(r"si|no",pregunta,re.I):
                    guardar_csv_jugador_stats(lista_dreamteam,int(indice), generar_path_jugador(lista_dreamteam,int(indice),path_stats_jugadores))
    input("Apriete una tecla para continuar...")
                
        