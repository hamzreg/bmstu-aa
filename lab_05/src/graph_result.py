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
    msg = "\n\nПОСТРОИТЬ ГРАФИК:\n" + \
          "1. зависимости времени от длины строки\n" + \
          "2. зависимости времени от числа строк\n" + \
          "0. Выход\n" + \
          "Выбор: "

    len = 1
    count_str = 2

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

    label1 = "Последовательная обработка"
    label2 = "Конвейерная обработка"

    if type_graph == Menu.count_str:
        title = "Зависимость времени от числа строк"
        xlabel = "Число строк"

        args = [10, 20, 30, 40, 50]
        result = [[0.00208726, 0.00298096, 0.00376455, 0.0047981, 0.00612586], 
                  [0.00150191, 0.0026085, 0.00288755, 0.00439648, 0.00562291]]

    elif type_graph == Menu.len:
        title = "Зависимость времени от длины строк"
        xlabel = "Длина строк"

        args = [21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000, 29000, 30000]
        result = [[0.00578205, 0.00665335, 0.00622548, 0.00668922, 0.0063078, 
                   0.00787207, 0.0075988, 0.00811354, 0.00941068, 0.010253],
                  [0.00372732, 0.00455066, 0.004173, 0.00610597, 0.00401028,
                   0.00742847, 0.006465, 0.00507465, 0.00536238, 0.00620687]]
        # result = [[0.00423032, 0.00492197, 0.00982671, 0.0148205, 0.0195122,
        #            0.0263445, 0.0308759, 0.0368916, 0.0488796, 0.0527271], 
        #           [0.00353928, 0.00321933, 0.00478432, 0.0114914, 0.0132036, 
        #            0.0230261, 0.0223084, 0.0344795, 0.0372315, 0.0499187]]

    fig = plt.figure(figsize=(10, 7))
    plot = fig.add_subplot()
    plot.plot(args, result[0], label = label1)
    plot.plot(args, result[1], label = label2)
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

        if command == Menu.count_str:
            get_graph_result(Menu.count_str)
        elif command == Menu.len:
            get_graph_result(Menu.len)
        else:
            process = False
            

if __name__ == "__main__":
    process()