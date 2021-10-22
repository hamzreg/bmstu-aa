from dataclasses import dataclass

from arr import sort_arr
from sort import *
from graph_result import get_graph_result
from time_test import print_time

@dataclass
class Menu:
    """
        Константы необходимые в меню.
    """
    msg = "\n\nМЕНЮ:\n" + \
          "1. Сортировка выбором\n" + \
          "2. Сортировка Шелла\n" + \
          "3. Гномья сортировка\n" + \
          "4. Построить графики\n" + \
          "5. Замерить время\n" + \
          "0. Выход\n" + \
          "Выбор: "

    exit = 0
    selection = 1
    shell = 2
    gnome = 3
    plot = 4
    measure = 5


def process():

    process = True

    while process:
        command = int(input(Menu.msg))

        if command == Menu.selection:
            sort_arr(selection_sort)
        elif command == Menu.shell:
            sort_arr(shell_sort)
        elif command == Menu.gnome:
            sort_arr(gnome_sort)
        elif command == Menu.plot:
            get_graph_result()
        elif command == Menu.measure:
            print_time()
        else:
            process = False
            

if __name__ == "__main__":
    process()
