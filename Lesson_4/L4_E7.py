"""
Задание 7.
Реализовать генератор с помощью функции с ключевым словом yield,
создающим очередное значение. При вызове функции должен создаваться объект-генератор.
Функция вызывается следующим образом: for el in fact(n). Она отвечает за получение факториала числа.
В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n.
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""
from itertools import count


# Ф-я для варианта 1
def generator(cnt_limit):
    for each_el in count(1):
        if each_el > cnt_limit:
            break
        print(each_el)
        yield each_el


# Ф-я для варианта 1
def fact():
    fact1 = 1
    for elem in generator(count_limit):
        fact1 *= elem
    return fact1


# Ф-я для варианта 2
def factr(limit):
    for each_el in count(1):
        if each_el > limit:
            break
        else:
            yield each_el


count_limit = int(input("Число: "))
# Вариант 1
print("===== Вариант 1 =====")
print(f"{count_limit}! = {fact()}")
# Вариант 2
print("===== Вариант 2 =====")
ffact = 1
for el in factr(count_limit):
    print(el)
    ffact *= el
print(f"{count_limit}! = {ffact}")
