from random import choice
import string

def input_strs():
    """
        Ввод строк.
    """

    str1 = input("Введите строку № 1: ")
    str2 = input("Введите строку № 2: ")

    return str1, str2


def find_distance(algorithm):
    """
        Нахождение редакционного
        расстояния.
    """

    str1, str2 = input_strs()

    distance = algorithm(str1, str2)

    print("Полученное редакционное расстояние:", distance)


def get_random_string(len):
    letters = string.ascii_lowercase

    return "".join(choice(letters) for _ in range(len))