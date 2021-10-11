from arr import sort_arr
from sort import *
from graph_result import get_graph_result

MENU = "\n\nМЕНЮ:\n" + \
       "1. Сортировка выбором\n" + \
       "2. Сортировка Шелла\n" + \
       "3. Гномья сортировка\n" + \
       "4. Построить графики\n" + \
       "0. Выход\n" + \
       "Выбор: "
EXIT = 0
SELECTION = 1
SHELL = 2
GNOME = 3
PLOT = 4


def process():

    process = True

    while process:
        command = int(input(MENU))

        if command == SELECTION:
            sort_arr(selection_sort)
        elif command == SHELL:
            sort_arr(shell_sort)
        elif command == GNOME:
            sort_arr(gnome_sort)
        elif command == PLOT:
            get_graph_result()
        else:
            process = False
            

if __name__ == "__main__":
    process()
