
#1. Generar en una estructura todas las estadísticas asociadas a cada jugador o jugadora.

def estructura (names, goals, goals_avoided, assists):
    equipo = {}
    names = names.split()
    for name, gol, gol_evitado, asistencia in zip(names, goals, goals_avoided, assists):
        equipo[name] = (gol, gol_evitado, asistencia)
    return equipo


#2. Conocer el nombre y la cantidad de goles del goleador o goleadora.

def goleadorx(jugadores):
    maximo = ["name", 0]
    for jugador in jugadores:
        if jugadores[jugador][0] > maximo[1]:
            maximo[0]= jugador
            maximo[1]= jugadores[jugador][0]
    tupla = (maximo[0], maximo[1])
    return tupla


#3. Conocer el nombre del jugador o jugadora más influyente, esto se consigue sumando goles a favor, goles evitados y cantidad de asistencias. La particularidad es que los goles a favor, evitados y las asistencias NO valen lo mismo (es un promedio ponderado): goles a favor: 1,5 --- goles evitados: 1,25 --- asistencias: 1

def max_inf(jug3):
    maximo = ["name", 0]
    for jugador in jug3:
        contador = (jug3[jugador][0]*1.5 ) + (jug3[jugador][1]*1.25) + (jug3[jugador][2])
        if contador > max[1]:
            maximo[0] = jugador
            maximo[1] = contador
    return maximo[0]  #retorno solo el nombre del jugador mas influyente


#4. Conocer el promedio de goles por partido del equipo en general. Dato: Se jugaron 25 partidos en la temporada

def promedio (jug4, partidos):
    total = 0
    for jugador in jug4:
        total += jug4[jugador][0]
    total = total/partidos
    return total


#5. Conocer el promedio de goles por partido del goleador o goleadora. Dato: Se jugaron 25 partidos en la temporada.

def prom_goleadorx(goles, partidos):
    total = goles / partidos
    return total

