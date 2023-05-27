import re

from funciones import (
    leer_archivo,
    mostrar_jugadores_dreamteam,
    mostrar_estadisticas,
    validacion_menu,
    guardar_csv_jugador_stats,
    generar_path_jugador,
    mostrar_logros_por_busqueda,
    calcular_promedio_total,
    mostrar_estadistica_por_jugador_ordenado,
    mostrar_jugador_hof,
    mostrar_jugador_mayor_stat,
    mostrar_jugadores_promediado_mas_stat,
    generar_promedio_segun_stat_menos_peor_valor,
    mostrar_jugador_mayor_cant_logros,
    ordenar_lista_segun_key,
    exportar_ranking_csv
)

menu = "{0}".format(
"""--------------------------------------------------------
1- Mostrar la lista de todos los jugadores del Dream Team. Con el formato:
Nombre Jugador - Posición. Ejemplo:
Michael Jordan - Escolta

2- Elegir un jugador por su índice y mostrar sus estadísticas completas, 
incluyendo temporadas jugadas, puntos totales, promedio de puntos por partido, rebotes totales, 
promedio de rebotes por partido, asistencias totales, promedio de asistencias por partido, robos totales, 
bloqueos totales, porcentaje de tiros de campo, porcentaje de tiros libres y porcentaje de tiros triples.

3- Guardar las estadísticas de ese jugador en un archivo CSV. 

4- Buscar un jugador por su nombre y mostrar sus logros, 

5- Mostrar el promedio de puntos por partido de todo el equipo del Dream Team, 
ordenado por nombre de manera ascendente. 

6- Ingresar el nombre de un jugador y mostrar si ese jugador es miembro del Salón de la Fama del Baloncesto.

7- Mostrar el jugador con la mayor cantidad de rebotes totales.

8- Mostrar el jugador con el mayor porcentaje de tiros de campo.

9- Mostrar el jugador con la mayor cantidad de asistencias totales.

10- Ingresar un valor y mostrar los jugadores que han promediado más puntos por partido que ese valor.

11- Ingresar un valor y mostrar los jugadores que han promediado más rebotes por partido que ese valor.

12- Ingresar un valor y mostrar los jugadores que han promediado más asistencias por partido que ese valor.

13- Mostrar el jugador con la mayor cantidad de robos totales.

14- Mostrar el jugador con la mayor cantidad de bloqueos totales.

15- Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor.

16- Mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.

17- Mostrar el jugador con la mayor cantidad de logros obtenidos.

18- Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor.

19- Mostrar el jugador con la mayor cantidad de temporadas jugadas

20- Ingresar un valor y mostrar los jugadores, ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor.

23- BONUS TRACK!!! Generar un .csv de una tabla con la posición de ranking de Puntos, Rebotes, Asistencias y Robos de cada jugador.

0- SALIR

Ingrese la opción deseada: """ 
)

path_JSON = "pp_lab1_abal_joaquin/dt.json"
path_stats_jugadores = 'pp_lab1_abal_joaquin/stats_jugadores/'
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
            if indice.isnumeric() and int(indice) >= 0 and int(indice) <= (len(lista_dreamteam) - 1):
                mensaje = mostrar_estadisticas(lista_dreamteam, int(indice))
                print(mensaje)
            else:
                indice = None
                print("Error al ingresar un índice no válido.")
                                          
        case 3:
            if not indice:
                print("Primero debes seleccionar a un jugador, ingresando desde la opción 2.")
            else:    
                pregunta = input("Quiere exportar las estadísticas del jugador en un .csv? (si/no)")
                if re.match(r"si|no",pregunta,re.I):
                    guardar_csv_jugador_stats(lista_dreamteam,int(indice), generar_path_jugador(lista_dreamteam,int(indice),path_stats_jugadores))
    
        case 4: 
            nombre_jugador = input("Ingrese el nombre del jugador a buscar: ")
            mostrar_logros_por_busqueda(lista_dreamteam, nombre_jugador)

        case 5:
            estadistica_a_buscar = "promedio_puntos_por_partido"
            promedio = calcular_promedio_total(lista_dreamteam, estadistica_a_buscar)
            if promedio:
                mostrar_estadistica_por_jugador_ordenado(lista_dreamteam,"nombre",estadistica_a_buscar)
                print("\nEl promedio total del equipo de {0}: {1}\n".format(
                estadistica_a_buscar.replace("_"," ").capitalize(),
                promedio        
                ))
            else:
                print("La estadística buscada no existe.")

        case 6:
            nombre_jugador = input("Ingrese el nombre del jugador a buscar: ")
            mostrar_jugador_hof(lista_dreamteam, nombre_jugador)
                
        case 7:
            estadistica_a_buscar = "rebotes_totales"
            mostrar_jugador_mayor_stat(lista_dreamteam, estadistica_a_buscar)
            
        case 8:
            estadistica_a_buscar = "porcentaje_tiros_de_campo"
            mostrar_jugador_mayor_stat(lista_dreamteam, estadistica_a_buscar)
            
        case 9:
            estadistica_a_buscar = "asistencias_totales"
            mostrar_jugador_mayor_stat(lista_dreamteam, estadistica_a_buscar)

        case 10:
            estadistica_a_buscar = "promedio_puntos_por_partido"
            valor_ingresado = input("Ingrese un valor para comparar: ")
            if valor_ingresado.replace(".","").isnumeric():
                mostrar_jugadores_promediado_mas_stat(lista_dreamteam,estadistica_a_buscar,float(valor_ingresado))
            else:
                print("Valor ingresado erróneo, por favor vuelva al menú e ingrese una opción nuevamente.")              
                
        case 11:
            estadistica_a_buscar = "promedio_rebotes_por_partido"
            valor_ingresado = input("Ingrese un valor para comparar: ")
            if valor_ingresado.replace(".","").isnumeric():
                mostrar_jugadores_promediado_mas_stat(lista_dreamteam,estadistica_a_buscar,float(valor_ingresado))
            else:
                print("Valor ingresado erróneo, por favor vuelva al menú e ingrese una opción nuevamente.")              
                
        case 12:
            estadistica_a_buscar = "promedio_asistencias_por_partido"
            valor_ingresado = input("Ingrese un valor para comparar: ")
            if valor_ingresado.replace(".","").isnumeric():
                mostrar_jugadores_promediado_mas_stat(lista_dreamteam,estadistica_a_buscar,float(valor_ingresado))
            else:
                print("Valor ingresado erróneo, por favor vuelva al menú e ingrese una opción nuevamente.")
                
        case 13:
            estadistica_a_buscar = "robos_totales"
            mostrar_jugador_mayor_stat(lista_dreamteam, estadistica_a_buscar)
            
        case 14:
            estadistica_a_buscar = "bloqueos_totales"
            mostrar_jugador_mayor_stat(lista_dreamteam, estadistica_a_buscar)
            
        case 15:
            estadistica_a_buscar = "porcentaje_tiros_libres"
            valor_ingresado = input("Ingrese un valor para comparar: ")
            if valor_ingresado.replace(".","").isnumeric():
                mostrar_jugadores_promediado_mas_stat(lista_dreamteam,estadistica_a_buscar,float(valor_ingresado))
            else:
                print("Valor ingresado erróneo, por favor vuelva al menú e ingrese una opción nuevamente.")                            
            
        case 16:
            estadistica_a_buscar = "promedio_puntos_por_partido"
            promedio = generar_promedio_segun_stat_menos_peor_valor(lista_dreamteam, estadistica_a_buscar)
            print("\nEl promedio total del equipo de {0} sin contar el jugador que peor promedia es de: {1}\n".format(
            estadistica_a_buscar.replace("_"," "),
            promedio        
            ))
            
        case 17:
            mostrar_jugador_mayor_cant_logros(lista_dreamteam)
            
        case 18:
            estadistica_a_buscar = "porcentaje_tiros_triples"
            valor_ingresado = input("Ingrese un valor para comparar: ")
            if valor_ingresado.replace(".","").isnumeric():
                mostrar_jugadores_promediado_mas_stat(lista_dreamteam,estadistica_a_buscar,float(valor_ingresado))
            else:
                print("Valor ingresado erróneo, por favor vuelva al menú e ingrese una opción nuevamente.")

        case 19:
            estadistica_a_buscar = "temporadas"
            mostrar_jugador_mayor_stat(lista_dreamteam, estadistica_a_buscar)
    
        case 20:
            lista_ordenada = ordenar_lista_segun_key(lista_dreamteam, "posicion")
            estadistica_a_buscar = "porcentaje_tiros_de_campo"
            valor_ingresado = input("Ingrese un valor para comparar: ")
            if valor_ingresado.replace(".","").isnumeric():
               mostrar_jugadores_promediado_mas_stat(lista_ordenada,estadistica_a_buscar,float(valor_ingresado), True)
            else:
                print("Valor ingresado erróneo, por favor vuelva al menú e ingrese una opción nuevamente.")  

        case 23:
            exportar_ranking_csv(lista_dreamteam, 'pp_lab1_abal_joaquin/ranking_jugadores.csv')
    
        case 0:
            print("Hasta pronto!")
            break


    input("\n\nApriete una tecla para continuar...")
                
        