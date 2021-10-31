from random import randint

START = 0
END = 100


def create_random_matrix(n):
    """
        Создание матрицы
        случайных чисел.
    """

    matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            matrix[i][j] = randint(START, END)

    return matrix


def input_matrix():
    """
        Ввод матрицы.
    """

    try:
        n = int(input("Введите число строк: "))
        m = int(input("Введите число столбцов: "))

        if n < 1 or m < 1:
            print("\nОшибка! Размерность матрицы должна быть больше 0!")
            return []
    except:
        print("\nОшибка! Введено не число!")
        return []

    print("Введите элементы матрицы по одному в строке:")
    matrix = []

    for i in range(n):
        matrix.append([])

        for _ in range(m):
            try:
                elem = int(input())
                matrix[i].append(elem)
            except:
                print("\nОшибка! Введено не число!")
                return []
    
    return matrix


def print_matrix(matrix):
    """
        Печать матрицы.
    """

    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        for j in range(m):
            print(" " + str(matrix[i][j]), end = "")
        print("")


def multiplicate(algorithm):
    """
        Умножение матриц.
    """

    print("\nВведите матрицу A!")
    A = input_matrix()

    if not len(A):
        return
    
    print("\nВведенная матрица A:")
    print_matrix(A)

    print("\nВведите матрицу B!")
    B = input_matrix()

    if not len(B):
        return

    print("\nВведенная матрица B:")
    print_matrix(B)

    if len(A[0]) != len(B):
        print("\nОшибка! Число столбцов матрицы A должно быть равно числу строк матрицы B!\n")
        return

    result = algorithm(A, B)

    print("\nПолученная матрица:")
    print_matrix(result)


def standard_mult(A, B):
    """
        Стандартный алгоритм
        умножения матриц.
    """

    n = len(A)
    m = len(B[0])
    p = len(A[0])

    C = [[0] * m for i in range(n)]

    for i in range(n):
        for j in range(m):
            for k in range(p):
                C[i][j] += A[i][k] * B[k][j]

    return C


def winograd_mult(A, B):
    """
        Умножение матриц
        по алгоритму
        Винограду.
    """

    n = len(A)
    m = len(B[0])
    p = len(A[0])

    C = [[0] * m for _ in range(n)]

    row_factors = [0] * n

    for i in range(n):
        for j in range(p // 2):
            row_factors[i] = row_factors[i] + \
                             A[i][2 * j] * A[i][2 * j + 1]

    column_factors = [0] * m

    for i in range(m):
        for j in range(p // 2):
            column_factors[i] = column_factors[i] + \
                                B[2 * j][i] * B[2 * j + 1][i]

    for i in range(n):
        for j in range(m):
            C[i][j] = -row_factors[i] - column_factors[j]

            for k in range(p // 2):
                C[i][j] = C[i][j] + (A[i][2 * k + 1] + B[2 * k][j]) * \
                                    (A[i][2 * k] + B[2 * k + 1][j])
    
    if p % 2 != 0:
        for i in range(n):
            for j in range(m):
                C[i][j] = C[i][j] + A[i][p - 1] * B[p - 1][j]
    
    return C


def optimized_winograd_mult(A, B):
    """
        Умножение матриц
        по оптимизированному
        алгоритму Винограда.
    """

    n = len(A)
    m = len(B[0])
    p = len(A[0])

    C = [[0] * m for _ in range(n)]

    row_factors = [0] * n

    for i in range(n):
        for j in range(1, p, 2):
            row_factors[i] += A[i][j] * A[i][j - 1]

    column_factors = [0] * m

    for i in range(m):
        for j in range(1, p, 2):
            column_factors[i] += B[j][i] * B[j - 1][i]

    flag = p % 2

    for i in range(n):
        for j in range(m):
            C[i][j] = -(row_factors[i] + column_factors[j])

            for k in range(1, p, 2):
                C[i][j] += (A[i][k - 1] + B[k][j]) * \
                                    (A[i][k] + B[k - 1][j])
    
            if flag:
                C[i][j] += A[i][p - 1] * B[p - 1][j]
    
    return C
