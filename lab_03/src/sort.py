def selection_sort(arr, size):
    """
        Сортировка выбором.
    """

    for i in range(size - 1):
        min_element = arr[i]
        min_index = i

        for j in range(i + 1, size):
            if arr[j] < min_element:
                min_element = arr[j]
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]


def shell_sort(arr, size):
    """
        Сортировка Шелла.
    """

    d = size // 2

    while d > 0:
        for i in range(0, size):
            for j in range(i + d, size, d):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
        d //= 2


def gnome_sort(arr, size):
    """
        Гномья сортировка.
    """

    i = 1

    while i < size:
        if arr[i - 1] <= arr[i]:
            i += 1
        else:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]

            if i > 1:
                i -= 1
