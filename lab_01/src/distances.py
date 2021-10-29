from dataclasses import dataclass

from matrix import *

@dataclass
class Cost:
    """
        Стоимости операций.
    """

    deletion = 1
    insertion = 1
    replacement = 1
    transposition = 1

@dataclass
class Distance:
    """
        Константы для выбора
        алгоритмов нахождения
        редакционного расстояния.
    """

    msg = "\n\nТип алгоритма:\n" + \
          "1 - рекурсивный (Левенштейн)\n" + \
          "2 - матричный (Левенштейн)\n" + \
          "3 - рекурсивный с использованием матрицы (Левенштейн)\n" + \
          "4 - рекурсивный (Дамерау-Левенштейн)\n" + \
          "Выбор: "

    recursion = 1
    matrix = 2
    recursion_with_matrix = 3
    damerau_levenshtein = 4


def recursive(str1, str2):
    """
        Рекурсивная версия
        алгоритма нахождения
        расстояния Левенштейна.
    """

    n = len(str1)
    m = len(str2)

    if n == 0 or m == 0:
        return abs(n - m)

    cost_replacement = Cost.replacement if str1[-1] != str2[-1] else 0

    deletion = recursive(str1[:-1], str2) + Cost.deletion
    insertion = recursive(str1, str2[:-1]) + Cost.insertion
    replacement = recursive(str1[:-1], str2[:-1]) + cost_replacement

    min_distance = min(deletion, insertion, replacement)

    return min_distance


def matrix_(str1, str2, output = False):
    """
        Матричная версия
        алгоритма нахождения
        расстояния Левенштейна.
    """

    n, m = len(str1), len(str2)
    matrix = create_matrix(n + 1, m + 1)

    for i in range(1, n + 1):
        for j in range(1, m + 1):

            cost_replacement = Cost.replacement if str1[i - 1] != str2[j - 1] else 0
            matrix[i][j] = min(matrix[i - 1][j] + Cost.deletion,
                               matrix[i][j - 1] + Cost.insertion,
                               matrix[i - 1][j - 1] + cost_replacement)

    if output:
        print_matrix(matrix, str1, str2)
    
    return matrix[n][m]


def recursive_(str1, str2, n, m, matrix):
    """
        Рекурсия для алгоритма
        нахождения расстояния
        Левенштейна с использованием
        матрицы.
    """

    if matrix[n][m] != -1:
        return matrix[n][m]

    if n == 0:
        matrix[n][m] = m
        return matrix[n][m]
    
    if n > 0 and m == 0:
        matrix[n][m] = n
        return matrix[n][m]

    cost_replacement = Cost.replacement if str1[n - 1] != str2[m - 1] else 0

    deletion = recursive_(str1, str2, n - 1, m, matrix) + Cost.deletion
    insertion = recursive_(str1, str2, n, m - 1, matrix) + Cost.insertion
    replacement = recursive_(str1, str2, n - 1, m - 1, matrix) + cost_replacement
    
    matrix[n][m] = min(deletion,
                       insertion,
                       replacement)

    return matrix[n][m]


def recursive_with_cache(str1, str2, output = False):
    """
        Рекурсивная версия
        алгоритма нахождения
        расстояния Левенштейна
        с использованием матрицы.
    """

    n, m = len(str1), len(str2)
    matrix = [[-1] * (m + 1) for _ in range(n + 1)]

    recursive_(str1, str2, n, m, matrix)

    if output:
        print_matrix(matrix, str1, str2)

    return matrix[n][m]


def damerau_levenshtein(str1, str2):
    """
        Рекурсивная версия
        алгоритма нахождения
        расстояния Дамерау-
        Левенштейна.
    """

    n = len(str1)
    m = len(str2)

    if n == 0 or m == 0:
        return abs(n - m)

    cost_replacement = Cost.replacement if str1[-1] != str2[-1] else 0

    deletion = damerau_levenshtein(str1[:-1], str2) + Cost.deletion
    insertion = damerau_levenshtein(str1, str2[:-1]) + Cost.insertion
    replacement = damerau_levenshtein(str1[:-1], str2[:-1]) + cost_replacement

    if n > 1 and m > 1 and str1[-1] == str2[-2] and str1[-2] == str2[-1]:
        transposition = damerau_levenshtein(str1[:-2], str2[:-2]) + Cost.transposition
        return min(deletion, insertion, replacement, transposition)

    return min(deletion, insertion, replacement)
