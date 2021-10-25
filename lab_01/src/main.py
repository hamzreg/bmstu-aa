from dataclasses import dataclass

from str import find_distance
from distances import *
from graph_result import get_graph_result
from time_test import print_time

@dataclass
class Menu:
    """
        Константы необходимые в меню.
    """
    msg = "\nМЕНЮ:\n" + \
          "Найти расстояние Левенштейна при помощи:\n" + \
          "     1 - рекурсивного алгоритма;\n" + \
          "     2 - матричного алгоритма;\n" + \
          "     3 - рекурсивного алгоритма с использованием матрицы.\n" + \
          "Найти расстояние Дамерау-Левенштейна при помощи:\n" + \
          "     4 - рекурсивного алгоритма.\n" + \
          "     5 - Построить графики.\n" + \
          "     6 - Замерить время.\n" + \
          "     7 - Найти расстояние при помощи всех алгоритмов.\n" + \
          "     0 - Выход.\n" + \
          "Выбор: "

    exit = 0
    recursion = 1
    matrix = 2
    recursion_with_matrix = 3
    damerau_levenshtein = 4
    plot = 5
    measure = 6
    all_alg = 7


def process():

    process = True

    while process:
        command = int(input(Menu.msg))

        if command == Menu.recursion:
            find_distance(recursive)
        elif command == Menu.matrix:
            find_distance(matrix_)
        elif command == Menu.recursion_with_matrix:
            find_distance(recursive_with_cache)
        elif command == Menu.damerau_levenshtein:
            find_distance(damerau_levenshtein)
        elif command == Menu.plot:
            get_graph_result()
        elif command == Menu.measure:
            print_time()
        elif command == Menu.all_alg:
            test_all()
        else:
            process = False
            

if __name__ == "__main__":
    process()
