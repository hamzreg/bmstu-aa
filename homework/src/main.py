from arr import get_random_arr, counting_sort


if __name__ == "__main__":
    size = int(input("Введите размер массива: "))
    arr = get_random_arr(size)
    print("Массив для сортировки: ", arr)
    arr = counting_sort(arr, len(arr))
    print("Отсортированный массив: ", arr)
