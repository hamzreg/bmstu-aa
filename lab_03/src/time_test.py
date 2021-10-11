from time import process_time

from sort import *


def get_time_sort(sort, arr, size):
    """
        Замер времени сортировки.
    """

    start = process_time()
    sort(arr, size)
    result = process_time() - start

    return result


def time_test(arr_type, start, end, step, iters):
    """
        Проведение временных замеров 
        работы алгоритмов сортировки  
        для массива определенного типа.
    """

    results = [[], [], []]
    sorts = [selection_sort, shell_sort, gnome_sort]

    for sort in enumerate(sorts):
        for size in range(start, end, step):
            result = 0

            for _ in range(iters):
                arr = arr_type(size)
                result += get_time_sort(sort[1], arr, size)

            results[sort[0]].append(result / iters)
    
    return results
