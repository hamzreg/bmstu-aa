from random import randint

LOW = -1000
TOP = 1000


def input_arr():
    """
        Ввод массива.
    """

    size = int(input("Введите размер массива: "))
    arr = []

    print("Введите элементы массива:")
    for i in range(size):
        arr.append(int(input()))

    return arr


def sort_arr(sort_type):
    """
        Сортировка массива.
    """

    arr = input_arr()
    sort_type(arr, len(arr))
    
    print("Отсортированный массив:")
    print(arr)


def get_sorted_arr(size):
    """
        Отсортированный массив.
    """

    arr = []

    for i in range(size):
        arr.append(i)
    
    return arr


def get_reversed_arr(size):
    """
        Перевернутый массив.
    """

    arr = []

    for i in range(size):
        arr.append(size - i)

    return arr


def get_random_arr(size):
    """
        Случайный массив.
    """

    arr = []

    for _ in range(size):
        arr.append(randint(LOW, TOP))

    return arr
