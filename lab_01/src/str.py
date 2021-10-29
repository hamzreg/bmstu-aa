from random import choice
import string
from distances import Distance

def input_strs():
    """
        Ввод строк.
    """

    str1 = input("Введите строку № 1: ")
    str2 = input("Введите строку № 2: ")

    return str1, str2


def find_distance(algorithm, type):
    """
        Нахождение редакционного
        расстояния.
    """

    str1, str2 = input_strs()

    if type == Distance.matrix or type == Distance.recursion_with_matrix:
        distance = algorithm(str1, str2, output = True)
    else:
        distance = algorithm(str1, str2)

    print("\nПолученное редакционное расстояние:", distance)


def get_random_string(len):
    """
        Создание случайной строки.
    """

    letters = string.ascii_lowercase

    return "".join(choice(letters) for _ in range(len))
