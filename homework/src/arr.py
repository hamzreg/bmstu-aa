from dataclasses import dataclass
from random import randint

@dataclass
class ARR:
    """
        Константы для массива.
    """

    low = -10
    top = 10


def counting_sort(arr, size):
    """
        Сортировка подсчетом.
    """

    max_elem = arr[0]                       # 1
    min_elem = max_elem                     # 2

    for i in range(1, size):                # 3
        if max_elem < arr[i]:               # 4
            max_elem = arr[i]               # 5
        if min_elem > arr[i]:               # 6
            min_elem = arr[i]               # 7
    
    d = min_elem - 1                        # 8
    add_size = max_elem - min_elem + 1      # 9

    add_arr = [0] * add_size                # 10

    for i in range(size):                   # 11
        j = arr[i] - d - 1                  # 12
        add_arr[j] += 1                     # 13
    
    i = 0                                   # 13

    for j in range(add_size):               # 15
        if add_arr[j] > 0:                  # 16
            for _ in range(add_arr[j]):     # 17
                arr[i] = j + d              # 18
                i += 1                      # 19

    return arr


def get_random_arr(size):
    """
        Случайный массив.
    """

    arr = []

    for _ in range(size):
        arr.append(randint(ARR.low, ARR.top))

    return arr
