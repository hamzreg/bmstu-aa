from time import process_time
from copy import deepcopy

FULL = 0
BIN = 1
SEG = 2
ITERS = 40

def measure(data, key, alg):
    """
        Замер времени.
    """

    result = 0

    for _ in range(ITERS):
        if alg == FULL:
            start = process_time()
            data.brute_force(key)
            end = process_time()
        elif alg == BIN:
            sorted_data = data.sort_keys(data.data)
            start = process_time()
            data.binary_search(key, sorted_data)
            end = process_time()
        elif alg == SEG:
            segmented_data = data.segment_data()
            start = process_time()
            data.segment_search(key, segmented_data)
            end = process_time()

        result += end - start
    
    return result / ITERS


def test_time(dict_object):
    """
        Сравнение временных
        характеристик.
    """

    data = dict_object.data
    keys = list(data.keys())

    indexes = [index for index in range(len(keys))]
    results = [[], [], []]
    stage = 0

    for key in keys:
        results[FULL].append(measure(dict_object, key, FULL))
        results[BIN].append(measure(dict_object, key, BIN))
        results[SEG].append(measure(dict_object, key, SEG))

        stage += 1
        print("Progress: ", stage, " keys")
    
    return indexes, results


def sort_compares(compares):
    """
    """

    sorted_compares = deepcopy(compares)

    for i in range(len(sorted_compares) - 1):
        for j in range(len(sorted_compares) - i - 1):
            if sorted_compares[j] < sorted_compares[j + 1]:
                sorted_compares[j], sorted_compares[j + 1] = sorted_compares[j + 1], sorted_compares[j]
    
    return sorted_compares


def test_compares(dict_object):
    """
        Анализ числа сравнений.
    """

    alg = int(input("\nВыберите алгоритм:\n" + \
          "1. Полный перебор\n" + \
          "2. Двоичный поиск\n" + \
          "3. Поиск сегментами\n" + \
          "Выбор: "))

    data = dict_object.data
    keys = list(data.keys())

    indexes = [index for index in range(len(keys))]
    results = []
    stage = 0

    for key in keys:
        if alg == FULL:
            compares, _ = dict_object.brute_force(key)
            results.append(compares)
        elif alg == BIN:
            sorted_data = dict_object.sort_keys(dict_object.data)
            compares, _ = dict_object.binary_search(key, sorted_data)
            results.append(compares)
        elif alg == SEG:
            segmented_data = dict_object.segment_data()
            compares, _ = dict_object.segment_search(key, segmented_data)
            results.append(compares)

        stage += 1
        print("Progress: ", stage, " keys")
    
    sorted_compares = sort_compares(results)
    
    return alg, indexes, [results, sorted_compares]