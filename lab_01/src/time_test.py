from dataclasses import dataclass
from time import process_time

from distances import *
from str import get_random_string

@dataclass
class TimeTest:
    to_ms = 1000
    start_len = 0
    end_len = 9
    iters = 100


def get_time_alg(alg, str1, str2):
    """
        Замер времени алгоритма.
    """

    start = process_time()
    alg(str1, str2)
    result = process_time() - start

    return result


def time_test(type1, type2):
    """
        Проведение временных замеров 
        работы алгоритмов нахождения 
        редакционного расстояния
        в зависимости от длины слов.
    """

    results = [[], []]

    for alg in enumerate([type1, type2]):
        for len in range(TimeTest.start_len, TimeTest.end_len):
            result = 0

            for _ in range(TimeTest.iters):
                str1 = get_random_string(len)
                str2 = get_random_string(len)
                result += get_time_alg(alg[1], str1, str2)

            print("Progress:\t", len * 10, "%")

            results[alg[0]].append(result / TimeTest.iters)
    
    return results


def measure_time():
    """
        Проведение временных замеров 
        работы алгоритмов нахождения
        редакционного расстояния.
    """

    type1 = int(input(Distance.msg))
    type2 = int(input("Выбор: "))
    algorithms = [recursive, matrix_, recursive_with_cache, damerau_levenshtein]

    results = time_test(algorithms[type1 - 1],
                        algorithms[type2 - 1])
    
    return results, type1, type2

    
def print_time():
    """
        Табличный вывод результатов
        замеров времени.
        Формат для создания таблицы
        в latex.
    """

    results, type1, type2 = measure_time()
    msgs = ["рекурсивного алгоритма Левенштейна",
            "матричного алгоритма Левенштейна",
            "рекурсивного алгоритма Левенштейна с матрицей",
            "рекурсивного алгоритма Дамерау-Левенштейна"]

    print("\n\nРезультаты замеров времени для " + msgs[type1 - 1] + " " + msgs[type2 - 1])
    print(results)

    i = 0

    for len in range(TimeTest.start_len, TimeTest.end_len):
        print(" %4d & %.4f & %.4f \\\\ \n \\hline" %(len, \
            results[0][i] * TimeTest.to_ms, \
            results[1][i] * TimeTest.to_ms))

        i += 1
