"""
Задание 3.
Реализовать функцию my_func(), которая принимает три позиционных аргумента
и возвращает сумму наибольших двух аргументов
"""


def my_func(arg1, arg2, arg3):
    arg_list = sorted([arg1, arg2, arg3])
    return arg_list[1] + arg_list[2]


var1 = int(input('Число 1: '))
var2 = int(input('Число 2: '))
var3 = int(input('Число 3: '))
print(f"Сумма двух наибольших чисел: {my_func(var1, var2, var3)}")
# Можно и так, но строка не влезает в 79 символов
# print(f"Сумма двух наибольших чисел: "
#       f"{my_func(int(input('Число 1: ')), int(input('Число 2: ')), int(input('Число 3: ')))}")
