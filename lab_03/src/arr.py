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
    
    print("\nОтсортированный массив:")
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
        Отсортированный в 
        обратном порядке массив.
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
        arr.append(randint(ARR.low, ARR.top))

    return arr
