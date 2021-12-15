import matplotlib.pyplot as plt
from test_func import test_time, test_compares

FULL = 0
BIN = 1
SEG = 2

def graph_time_test(dict_object):
    """
        Графический вывод 
        результатов
        замеров времени.
    """

    indexes, results = test_time(dict_object)

    fig = plt.figure(figsize=(10, 7))
    plot = fig.add_subplot()
    plot.plot(indexes, results[0], label = "Полный перебор")
    plot.plot(indexes, results[1], label = "Бинарный поиск")
    plot.plot(indexes, results[2], label = "Поиск сегментами")

    plt.legend()
    plt.grid()
    plt.title("Сравнение временных характеристик: поиск в словаре")
    plt.ylabel("Время работы(c)")
    plt.xlabel("Индекс ключа")

    plt.show()


def graph_compares_test(dict_object):
    alg, indexes, results = test_compares(dict_object)

    if alg == FULL:
        alg_title = "Полный перебор"
    elif alg == BIN:
        alg_title = "Бинарный поиск"
    elif alg == SEG:
        alg_title = "Поиск сегментами"


    fig, ax = plt.subplots(2, 1, figsize = (10, 10))

    ax[0].bar(indexes, results[0], alpha = 0.5)
    ax[0].set(title = alg_title)
    ax[1].bar(indexes, results[1], alpha = 0.5)
    ax[1].set(title = alg_title + " (отсортированный)")

    for i in range(0, 2):
        ax[i].set_xlabel("Индекс ключа")
        ax[i].set_ylabel("Число сравнений")
        ax[i].grid()
    
    plt.show()
