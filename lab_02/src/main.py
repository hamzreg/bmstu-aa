from dataclasses import dataclass
from matrix import multiplicate, optimized_winograd_mult, standard_mult, winograd_mult

from graph_result import get_graph_result
from time_test import print_time

@dataclass
class Menu:
    """
        Константы необходимые в меню.
    """
    msg = "\nМЕНЮ:\n" + \
          "  1 - стандартное умножение матриц;\n" + \
          "  2 - умножение матриц по алгоритму Винограда;\n" + \
          "  3 - умножение матриц по оптимизированному алгоритму Винограда;\n" + \
          "  4 - построить графики;\n" + \
          "  5 - замерить время;\n" + \
          "  0 - выход.\n" + \
          "Выбор: "

    exit = 0
    standard = 1
    winograd = 2
    optimized = 3
    plot = 4
    measure = 5


def process():

    process = True

    while process:
        command = int(input(Menu.msg))

        if command == Menu.standard:
            multiplicate(standard_mult)
        elif command == Menu.winograd:
            multiplicate(winograd_mult)
        elif command == Menu.optimized:
            multiplicate(optimized_winograd_mult)
        elif command == Menu.plot:
            get_graph_result()
        elif command == Menu.measure:
            print_time()
        else:
            process = False
            

if __name__ == "__main__":
    process()
