from time import process_time

from sort import *
from arr import ARR, get_sorted_arr, get_reversed_arr, get_random_arr

TO_MS = 1000

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


def measure_time():
    """
        Вывод таблицы 
        замеров времени.
    """

    start_size = 100
    end_size = 1100
    step = 100
    iters = 1500

    arr_type = int(input(ARR.msg))

    if arr_type == ARR.sorted:
        results = time_test(get_sorted_arr,
                            start_size, end_size, 
                            step, iters)
    elif arr_type == ARR.reversed:
         results = time_test(get_reversed_arr,
                            start_size, end_size, 
                            step, iters) 
    elif arr_type == ARR.randomed:
         results = time_test(get_random_arr,
                            start_size, end_size, 
                            step, iters)
    
    print("\n\nРезультаты замеров времени:")
    i = 0

    for size in range(start_size, end_size, step):
        print(" %4d & %.4f & %.4f & %.4f \\\\ \n \\hline" %(size, \
            results[0][i] * TO_MS, \
            results[1][i] * TO_MS, \
            results[2][i] * TO_MS))

        i += 1
