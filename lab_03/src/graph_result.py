import matplotlib.pyplot as plt

from arr import ARR
from time_test import measure_time


def get_graph_result():
    """
        Графический вывод результатов
        замеров времени.
    """

    sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    results, arr_type = measure_time()

    if arr_type == ARR.sorted:
        title = "Сортировка отсортированного массива"
    elif arr_type == ARR.reversed:
        title = "Сортировка массива, отсортированного в обратном порядке"
    elif arr_type == ARR.randomed:
        title = "Сортировка массива случайных чисел"
    
    fig = plt.figure(figsize=(10, 7))
    plot = fig.add_subplot()
    plot.plot(sizes, results[0], label = "Сортировка выбором")
    plot.plot(sizes, results[1], label = "Сортировка Шелла")
    plot.plot(sizes, results[2], label = "Гномья сортировка")
    plt.legend()
    plt.grid()
    plt.title(title)
    plt.ylabel("Время сортировки(c)")
    plt.xlabel("Длина массива")

    plt.show()
