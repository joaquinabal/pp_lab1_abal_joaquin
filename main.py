from funciones import (
    leer_archivo,
    mostrar_jugadores_dreamteam,
    mostrar_estadisticas
)

menu = "{0}\n{1}\n{2}\n{3} ".format(
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
"Ingrese la opción deseada" 
)

path_JSON = "Parcial\dt.json"

lista_dreamteam= leer_archivo(path_JSON)
#print(lista_juegos_JSON)

while True:
    respuesta = input(menu)
    
    match(int(respuesta)):
        case 1:
            mostrar_jugadores_dreamteam(lista_dreamteam, False)
            
        case 2:
            mostrar_jugadores_dreamteam(lista_dreamteam, True)
            indice = input("Ingrese el indice del jugador a mostrar las estadísticas. ")
            print(mostrar_estadisticas(lista_dreamteam, int(indice)))