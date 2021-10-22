import matplotlib.pyplot as plt

from time_test import measure_time


def get_graph_result():
    """
        Графический вывод результатов
        замеров времени.
    """

    lens = [int(len) for len in range(9)]
    results, type1, type2 = measure_time()

    labels = ["рекурсивный алгоритм\n Левенштейна",
              "матричный алгоритм\n Левенштейна",
              "рекурсивный алгоритм\n Левенштейна с матрицей",
              "рекурсивный алгоритм\n Дамерау-Левенштейна"]
    
    fig = plt.figure(figsize=(10, 7))
    plot = fig.add_subplot()
    plot.plot(lens, results[0], label = labels[type1 - 1])
    plot.plot(lens, results[1], label = labels[type2 - 1])

    plt.legend()
    plt.grid()
    plt.title("Замеры времени")
    plt.ylabel("Затраченное время(c)")
    plt.xlabel("Длина")

    plt.show()
