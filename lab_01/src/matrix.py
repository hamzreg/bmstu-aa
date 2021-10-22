from dataclasses import dataclass
from random import randint

@dataclass
class ARR:
    """
        Константы для выбора типа массива.
    """

    msg = "\n\nТип массива:\n" + \
          "1 - отсортированный\n" + \
          "2 - отсортированный в обратном порядке\n" + \
          "3 - случайный\n" + \
          "Выбор: "
    
    sorted = 1
    reversed = 2
    randomed = 3

    low = -1000
    top = 1000


def create_matrix(n, m):
    """
        Создание матрицы.
    """

    matrix = [[0] * m for _ in range(n)]

    for i in range(n):
        matrix[i][0] = i
    
    for j in range(m):
        matrix[0][j] = j

    return matrix


def get_random_arr(size):
    """
        Случайный массив.
    """

    arr = []

    for _ in range(size):
        arr.append(randint(ARR.low, ARR.top))

    return arr
