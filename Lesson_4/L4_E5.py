"""
Задание 5.
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти чётные числа от 100 до 1000 (включая границы).
Нужно получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce


def multiply(prev_el, cur_el):
    return prev_el * cur_el


def generator():
    for each_el in range(100, 1001):
        if each_el % 2 == 0:
            yield each_el


my_list = [el for el in generator()]
print(f"{my_list}\n{reduce(multiply, my_list)}")
