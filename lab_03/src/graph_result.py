import matplotlib.pyplot as plt

from arr import get_sorted_arr, get_reversed_arr, get_random_arr
from time_test import time_test


def get_graph_result():
    """
        Построение графика зависимости
        времени работы алгоритмов сор-
        тировки от типа массива.
    """

    start_size = 100
    end_size = 1000
    step = 100
    iters = 1500

    sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    best_time = time_test(get_sorted_arr,
                          start_size, end_size + 1,
                          step, iters)
    worst_time = time_test(get_reversed_arr, 
                           start_size, end_size + 1,
                           step, iters)
    random_time = time_test(get_random_arr, 
                            start_size, end_size + 1,
                            step, iters)
    
    best_fig = plt.figure(figsize=(10, 7))
    plot = best_fig.add_subplot()
    plot.plot(sizes, best_time[0], label = "Сортировка выбором")
    plot.plot(sizes, best_time[1], label = "Сортировка Шелла")
    plot.plot(sizes, best_time[2], label = "Гномья сортировка")
    plt.legend()
    plt.grid()
    plt.title("Сортировка отсортированного массива")
    plt.ylabel("Время сортировки(c)")
    plt.xlabel("Длина массива")

    worst_fig = plt.figure(figsize=(10, 7))
    plot = worst_fig.add_subplot()
    plot.plot(sizes, worst_time[0], label = "Сортировка выбором")
    plot.plot(sizes, worst_time[1], label = "Сортировка Шелла")
    plot.plot(sizes, worst_time[2], label = "Гномья сортировка")
    plt.legend()
    plt.grid()
    plt.title("Сортировка массива, отсортированного в обратном порядке")
    plt.ylabel("Время сортировки(c)")
    plt.xlabel("Длина массива")

    random_fig = plt.figure(figsize=(10, 7))
    plot = random_fig.add_subplot()
    plot.plot(sizes, random_time[0], label = "Сортировка выбором")
    plot.plot(sizes, random_time[1], label = "Сортировка Шелла")
    plot.plot(sizes, random_time[2], label = "Гномья сортировка")
    plt.legend()
    plt.grid()
    plt.title("Сортировка массива случайных чисел")
    plt.ylabel("Время сортировки(c)")
    plt.xlabel("Длина массива")

    plt.show()
