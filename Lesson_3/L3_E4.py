"""
Задание 4.
Программа принимает действительное положительное число x и целое отрицательное число y.
Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
При решении задания нужно обойтись без встроенной функции возведения числа в степень
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень
с помощью оператора **. Второй — более сложная реализация без оператора **,
предусматривающая использование цикла.
"""


# решение с оператором **
def my_power1(arg, pwr):
    if pwr == 0 or pwr > 0:
        return "неправильный ввод, показатель степени должен быть меньше 0"
    else:
        return arg ** pwr


# решение с циклом
def my_power2(arg, pwr):
    if pwr == 0 or pwr > 0:
        return "неправильный ввод, показатель степени должен быть меньше 0"
    else:
        tmp = 1
        for i in range(abs(pwr)):
            tmp *= arg
        return 1 / tmp


my_var = float(input("Число: "))
var_pwr = int(input("Показатель степени (<0): "))
print(f"Результат 1: {my_power1(my_var, var_pwr)}\n"
      f"Результат 2: {my_power2(my_var, var_pwr)}")
