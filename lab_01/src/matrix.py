from dataclasses import dataclass
from random import randint


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


def print_matrix(matrix, str1, str2):
    print("\n0  0  " + "  ".join([let for let in str2]))

    for i in range(len(str1) + 1):
        
        print(str1[i - 1] if (i != 0) else "0", end = "")

        for j in range(len(str2) + 1):

            print("  " + str(matrix[i][j]), end = "")

        print("")
