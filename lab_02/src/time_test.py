from dataclasses import dataclass
from time import process_time

from matrix import standard_mult, winograd_mult, optimized_winograd_mult, create_random_matrix

@dataclass
class TimeTest:
    to_ms = 1000
    iters = 10
    min_size = 10
    max_size = 110
    step = 10
    odd = 1


def get_time_alg(alg, A, B):
    """
        Замер времени алгоритма.
    """

    start = process_time()
    alg(A, B)
    result = process_time() - start

    return result


def time_test(size_type):
    """
        Проведение временных замеров 
        работы алгоритмов умножения 
        матриц в зависимости
        от четности размера.
    """

    algorithms = [standard_mult,
                  winograd_mult,
                  optimized_winograd_mult]
    results = [[], [], []]

    if size_type == TimeTest.odd:
        start, stop = TimeTest.min_size + 1, TimeTest.max_size + 1
    else:
        start, stop = TimeTest.min_size, TimeTest.max_size

    for alg in enumerate(algorithms):
        for n in range(start, stop, TimeTest.step):
            result = 0
            A = create_random_matrix(n)
            B = create_random_matrix(n)

            for _ in range(TimeTest.iters):
                result += get_time_alg(alg[1], A, B)
            print("Progress:\t", n, "%")

            results[alg[0]].append(result / TimeTest.iters)
    
    return results


def measure_time():
    """
        Проведение временных замеров 
        работы алгоритмов умножения
        матриц.
    """

    print("Выберите тип размера:\n" + \
          "  1 - нечетный;\n" + \
          "  2 - четный.")
    size_type = int(input("Выбор: "))

    results = time_test(size_type)
    
    return results, size_type

    
def print_time():
    """
        Табличный вывод результатов
        замеров времени.
        Формат для создания таблицы
        в latex.
    """

    results, size_type = measure_time()
    msgs = ["нечетного",
            "четного"]

    print("\n\nРезультаты замеров времени для " + msgs[size_type - 1] + " размера:\n")

    i = 0

    if size_type == TimeTest.odd:
        start, stop = TimeTest.min_size + 1, TimeTest.max_size + 1
    else:
        start, stop = TimeTest.min_size, TimeTest.max_size

    for size in range(start, stop, TimeTest.step):
        print(" %4d & %.4f & %.4f & %.4f \\\\ \n \\hline" %(size, \
            results[1][i] * TimeTest.to_ms, \
            results[0][i] * TimeTest.to_ms, \
            results[2][i] * TimeTest.to_ms))

        i += 1
