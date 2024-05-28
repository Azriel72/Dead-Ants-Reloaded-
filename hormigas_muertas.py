"""
    Autor: Juan Manuel Abréu
    Fecha: 25-05-2024
    Descripción: Contar las hormigas muertas en un texto.
"""
import re

def dead_ant_count(text: str):

    a, n, t, count = 0, 0, 0, 0  # Inicialización de contadores y variables auxiliares
    char1, char2 = '', ''  # Variables para almacenar partes de hormigas
    text_len = len(text)  # Longitud del texto

    for c in text:
        count += 1  # Incrementa el contador de caracteres recorridos

        # Caso en el que char1 está vacío
        if not char1:
            if c != ' ' and c != '.':
                # Caso especial: último caracter en el texto y sin partes contadas aún
                if a == 0 and n == 0 and t == 0 and count == text_len:
                    if c == 'a':
                        a += 1
                    elif c == 'n':
                        n += 1
                    elif c == 't':
                        t += 1

                if c == 'a':
                    char1 = 'a'
                elif c == 'n':
                    n += 1
                elif c == 't':
                    t += 1
        
        # Caso en el que char1 está lleno pero char2 está vacío
        elif not char2:
            if c != ' ' and c != '.':
                # Caso especial: último caracter en el texto y sin partes contadas aún
                if a == 0 and n == 0 and t == 0 and count == text_len:
                    if c == 'a':
                        a += 1
                    elif c == 'n':
                        n += 1
                    elif c == 't':
                        t += 1

                if c == 'n':
                    char2 = 'n'
                else:
                    a += 1
                    if c == 'a':
                        char1 = 'a'
                    else:
                        t += 1
                        char1 = ''
            else:
                a += 1
                char1 = ''
        
        # Caso en el que char1 y char2 están llenos
        elif char1 and char2:
            if c != ' ' and c != '.':
                if c == 't':
                    char1 = ''
                    char2 = ''
                else:
                    a += 1
                    n += 1
                    if c == 'a':
                        char1 = 'a'
                        char2 = ''
                    else:
                        n += 1
                        char1 = ''
                        char2 = ''
            else:
                if char1 and char2:
                    a += 1
                    n += 1
                    char1 = ''
                    char2 = ''

    return max(a, n, t)  # Devuelve el máximo de las partes contadas (a, n, t)

def dead_ant_count_v2(text: str):
    ''' Esta función cuenta las hormigas muertas en un texto. '''
    text = text.strip(".")
    text = re.split("\.+", text)
    dead_ants = 0
    for word in text:
        if word != "ant":
            match = re.search('^(?!.*ant).*$', word)
            if match:
                debris = match.group(0)  # Obtiene los escombros de hormigas
                if 't' in debris:  # Si 't' se encuentra en los escombros, incrementa el contador de hormigas muertas
                    dead_ants += 1
    return dead_ants
