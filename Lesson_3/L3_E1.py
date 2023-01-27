"""
Задание 1.
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def my_div(val1, val2):
    try:
        return val1 / val2
    except ZeroDivisionError:
        return 'делить на 0 нельзя'


print(f"Реультат деления: "
      f"{my_div(float(input('Число 1: ')), float(input('Число 2: ')))}")
