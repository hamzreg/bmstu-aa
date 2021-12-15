from dataclasses import dataclass

from dictionary import Dictionary
from graph_result import graph_time_test, graph_compares_test
from test_func import test_time

@dataclass
class Menu:
    """
        Константы необходимые в меню.
    """

    msg = "\nПОИСК В СЛОВАРЕ:\n" + \
          "1. Полный перебор\n" + \
          "2. Двоичный поиск\n" + \
          "3. Поиск сегментами\n" + \
          "4. Все варианты поиска\n" + \
          "5. Построить графики\n" + \
          "6. Замерить время\n" + \
          "7. Анализ числа сравнений\n" + \
          "8. Вывод словаря\n" + \
          "0. Выход\n" + \
          "Выбор: "

    exit = 0
    full = 1
    bin = 2
    seg = 3
    all = 4
    plot = 5
    measure = 6
    compare = 7
    output = 8


def process():

    process = True
    dictionary = Dictionary("data/netflix.csv")

    while process:
        command = int(input(Menu.msg))

        if command == Menu.full:
            dictionary.search(Menu.full)
        elif command == Menu.bin:
          dictionary.search(Menu.bin)
        elif command == Menu.seg:
          dictionary.search(Menu.seg)
        elif command == Menu.all:
          dictionary.search(Menu.all)
        elif command == Menu.plot:
            graph_time_test(dictionary)
        elif command == Menu.measure:
            test_time(dictionary)
        elif command == Menu.compare:
            graph_compares_test(dictionary)
        elif command == Menu.exit:
            process = False
        else:
            print("\nВыбран неверный пункт меню.\n")


if __name__ == "__main__":
    process()