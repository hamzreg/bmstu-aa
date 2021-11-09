from dataclasses import dataclass
import matplotlib.pyplot as plt

NAME_MULTI = "time_multi.csv"
NAME_SINGLE = "time_single.csv"
NAME_ORDER_MULTI = "time_multi_order.csv"
NAME_ORDER_SINGLE = "time_single_order.csv"

FILE_MULTI = 1
FILE_SINGLE = 2
FILE_ORDER_MULTI = 3
FILE_ORDER_SINGLE = 4

COUNT_THREAD = 1
ORDER = 2
RESULT = 3

@dataclass
class Menu:
    """
        Константы необходимые в меню.
    """
    msg = "\n\nПоиск кратчайших путей в графе.\n" + \
          "ПОСТРОИТЬ ГРАФИК:\n" + \
          "1. зависимости времени от кол-ва потоков\n" + \
          "2. зависимости времени от порядка графа\n" + \
          "0. Выход\n" + \
          "Выбор: "

    count_thread = 1
    order = 2

def get_file_data(filename, data_type):
    """
        Получить данные из файла.
    """

    f = open(filename, "r")

    lines = []

    for line in (f.readlines()):
        lines.append(line.split())
    
    f.close

    sizes, result = [], []

    for data in lines:
        if data_type == Menu.count_thread:
            sizes.append(int(data[COUNT_THREAD]))
        else:
            sizes.append(int(data[ORDER]))
        
        result.append(float(data[RESULT]))
    
    return [sizes, result]


def get_graph_result(type_graph):
    """
        Графический вывод результатов
        замеров времени.
    """

    results = []

    if type_graph == Menu.count_thread:
        title = "Зависимость времени от кол-ва потоков"
        xlabel = "Кол-во потоков"
        
        label1 = "Без распараллеливания"
        label2 = "Многопоточный вариант"

        
        results.append(get_file_data(NAME_SINGLE, Menu.count_thread)) 
        results.append(get_file_data(NAME_MULTI, Menu.count_thread))
        results[0][1] = [results[0][1][0]] * len(results[1][0])

    elif type_graph == Menu.order:
        title = "Зависимость времени от порядка графа"
        xlabel = "Порядок графа"

        label1 = "Без распараллеливания"
        label2 = "4 потока"

        results.append(get_file_data(NAME_ORDER_SINGLE, Menu.order))
        results.append(get_file_data(NAME_ORDER_MULTI, Menu.order))

    fig = plt.figure(figsize=(10, 7))
    plot = fig.add_subplot()
    plot.plot(results[1][0], results[0][1], label = label1)
    plot.plot(results[1][0], results[1][1], label = label2)
    plt.legend()
    plt.grid()
    plt.title(title)
    plt.ylabel("Затраченное время(c)")
    plt.xlabel(xlabel)

    plt.show()


def process():

    process = True

    while process:
        command = int(input(Menu.msg))

        if command == Menu.count_thread:
            get_graph_result(Menu.count_thread)
        elif command == Menu.order:
            get_graph_result(Menu.order)
        else:
            process = False
            

if __name__ == "__main__":
    process()