from funciones import (
    leer_archivo,
    mostrar_jugadores_dreamteam
)

menu = "{0}\n{1}\n{2} ".format(
"----------------------------------------------------------------",
"""1- Mostrar la lista de todos los jugadores del Dream Team. Con el formato:
Nombre Jugador - Posición. Ejemplo:
Michael Jordan - Escolta\n""",
"Ingrese la opción deseada" 
)

path_JSON = "Parcial\dt.json"

lista_juegos_JSON = leer_archivo(path_JSON)
#print(lista_juegos_JSON)

while True:
    respuesta = input(menu)
    
    match(int(respuesta)):
        case 1:
            mostrar_jugadores_dreamteam(lista_juegos_JSON)