"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

### Importar librerías
import os
import csv
import re

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """ 
    with open("data.csv") as file:
        reader = csv.reader(file, delimiter='\t')
        suma = 0
        for row in reader:
            suma = suma + int(row[1])

    return suma


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    with open("data.csv") as file:
        reader = csv.reader(file, delimiter='\t')
        lista_letras = []
        lista_letras_totales = []
        lista_final = []
        for row in reader:
            letra = row[0]
            lista_letras.append(letra) # Agregar la primera columna a una lista
            lista_letras_totales.append(letra)

    lista_letras = list(set(lista_letras)) #Eliminar duplicados
    lista_letras.sort() #Ordenar alfabeticamente  

    for letra in lista_letras:
        cantidad = lista_letras_totales.count(letra) # Contar la cantidad de veces que se repite cada letra
        lista_final.append((letra, cantidad)) # Agregar la letra y la cantidad a una lista

    return lista_final


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    with open("data.csv") as file:
        reader = csv.reader(file, delimiter='\t')
        lista_letras = []
        lista = []
        lista_final = []
        for row in reader:
            letra = row[0]
            suma = int(row[1]) # Sumar la segunda columna
            lista_letras.append(letra) # Agregar la primera columna a una lista
            lista.append((letra, suma)) # Agregar la letra y la suma a una lista

        lista_letras = list(set(lista_letras)) #Eliminar duplicados
        lista_letras.sort() #Ordenar alfabeticamente

        for letra in lista_letras:
            suma = 0
            for letra2 in lista:
                if letra2[0] == letra:
                    suma = suma + letra2[1]
            lista_final.append((letra, suma))
        
    return lista_final


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    with open("data.csv") as file:
        reader = csv.reader(file, delimiter='\t')
        lista_fechas = []
        lista_meses = []
        lista_meses_totales = []
        lista_final = []
        for row in reader:
            fecha = row[2]
            lista_fechas.append(fecha) # Agregar la tercera columna a una lista
            lista_meses_totales.append(fecha)

    #Extraer los meses de la lista
    for fecha in lista_fechas:
        mes = re.findall(r'(?<=-)(.*?)(?=-)', fecha)
        lista_meses.append(mes[0])
        lista_meses_totales.append(mes[0])

    lista_meses = list(set(lista_meses)) #Eliminar duplicados
    lista_meses.sort() #Ordenar

    #Contar la cantidad de veces que se repite cada mes
    for mes in lista_meses:
        cantidad = lista_meses_totales.count(mes)
        lista_final.append((mes, cantidad))


    return lista_final


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    with open("data.csv") as file:
        reader = csv.reader(file, delimiter='\t')
        lista_letras = []
        lista = []
        lista_final = []
        for row in reader:
            letra = row[0]
            columna_2 = int(row[1])
            lista_letras.append(letra) # Agregar la primera columna a una lista
            lista.append((letra, columna_2)) # Agregar la letra y la columna 2 a una lista


        lista_letras = list(set(lista_letras)) #Eliminar duplicados
        lista_letras.sort() #Ordenar alfabeticamente

        lista_A = []
        lista_B = []
        lista_C = []
        lista_D = []
        lista_E = []

        for i in range(len(lista)):
            if lista[i][0] == "A":
                lista_A.append(lista[i][1])
            elif lista[i][0] == "B":
                lista_B.append(lista[i][1])
            elif lista[i][0] == "C":
                lista_C.append(lista[i][1])
            elif lista[i][0] == "D":
                lista_D.append(lista[i][1])
            elif lista[i][0] == "E":
                lista_E.append(lista[i][1])
    
        for letra in lista_letras:
            if letra == "A":
                lista_final.append((letra, max(lista_A), min(lista_A)))
            elif letra == "B":
                lista_final.append((letra, max(lista_B), min(lista_B)))
            elif letra == "C":
                lista_final.append((letra, max(lista_C), min(lista_C)))
            elif letra == "D":
                lista_final.append((letra, max(lista_D), min(lista_D)))
            elif letra == "E":
                lista_final.append((letra, max(lista_E), min(lista_E)))


    return lista_final


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    with open("data.csv") as file:
        reader = csv.reader(file, delimiter='\t')
        diccionario = {}
        lista_final = []
        for row in reader:
            columna_5 = row[4]
            lista = columna_5.split(",")
            for i in range(len(lista)):
                clave = lista[i][0:3]
                valor = lista[i][4:]
                if clave in diccionario:
                    diccionario[clave].append(valor)
                else:
                    diccionario[clave] = [valor]

        diccionario = dict(sorted(diccionario.items())) #Ordenar el diccionario

    for clave in diccionario:
        lista_valores = diccionario[clave]
        lista_valores = list(map(int, lista_valores))
        lista_final.append((clave, min(lista_valores), max(lista_valores)))

    return lista_final


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    with open("data.csv") as file:
        reader = csv.reader(file, delimiter='\t')
        lista_columna_1 = []
        lista = []
        for row in reader:
            columna_2 = row[1]
            lista_columna_1.append(int(columna_2))
            lista.append((int(columna_2), row[0]))

    lista_columna_1 = list(set(lista_columna_1)) #Eliminar duplicados
    lista_columna_1.sort() #Ordenar

    for i in range(len(lista_columna_1)):
        lista_letras = []
        for j in range(len(lista)):
            if lista_columna_1[i] == lista[j][0]:
                lista_letras.append(lista[j][1])
        lista_columna_1[i] = (lista_columna_1[i], lista_letras)

    return lista_columna_1


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    lista = pregunta_07()

    for i in range(len(lista)):
        lista[i] = (lista[i][0], sorted(list(set(lista[i][1]))))
        
    return lista


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    with open("data.csv") as file:
        reader = csv.reader(file, delimiter='\t')
        diccionario = {}
        for row in reader:
            columna_5 = row[4]
            lista = columna_5.split(",")
            for i in range(len(lista)):
                clave = lista[i][0:3]
                if clave in diccionario:
                    diccionario[clave] = diccionario[clave] + 1
                else:
                    diccionario[clave] = 1

    diccionario = dict(sorted(diccionario.items())) #Ordenar el diccionario

    return diccionario


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    with open("data.csv") as file:
        reader = csv.reader(file, delimiter='\t')
        lista = []
        for row in reader:
            columna_1 = row[0]
            columna_4 = row[3]
            columna_5 = row[4]
            lista_columna_4 = columna_4.split(",")
            lista_columna_5 = columna_5.split(",")
            lista.append((columna_1, len(lista_columna_4), len(lista_columna_5)))
    
    return lista


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    with open("data.csv") as file:
        reader = csv.reader(file, delimiter='\t')
        diccionario = {}
        for row in reader:
            columna_2 = int(row[1])
            columna_4 = row[3]
            lista_columna_4 = columna_4.split(",")
            for i in range(len(lista_columna_4)):
                clave = lista_columna_4[i]
                if clave in diccionario:
                    diccionario[clave] = diccionario[clave] + columna_2
                else:
                    diccionario[clave] = columna_2
    
    diccionario = dict(sorted(diccionario.items())) #Ordenar el diccionario

    return diccionario


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    with open("data.csv") as file:
        reader = csv.reader(file, delimiter='\t')
        diccionario = {}
        for row in reader:
            columna_1 = row[0]
            columna_5 = row[4]
            clave = columna_1
            lista_columna_5 = columna_5.split(",")
            for i in range(len(lista_columna_5)):
                lista_columna_5[i] = int(re.sub("[^0-9]", "", lista_columna_5[i])) #Expresión regular para eliminar los números
            if clave in diccionario:
                diccionario[clave] = diccionario[clave] + sum(lista_columna_5)
            else:
                diccionario[clave] = sum(lista_columna_5)

    diccionario = dict(sorted(diccionario.items())) #Ordenar el diccionario
    
    return diccionario
