"""
Задание 7.
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число». Реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
Проверял здесь: https://ru.onlinemschool.com/math/assistance/complex_number/calculation/
"""
import random


class MyComplex:
    def __init__(self, real, imagine):
        self.real = real
        self.imagine = imagine
        self.__allreal = 0
        self.__allimagine = 0

    def __str__(self):
        if int(self.imagine) > 0:
            return f"{self.real}+{self.imagine}i"
        else:
            return f"{self.real}{self.imagine}i"

    def __add__(self, other):
        if int(self.imagine) + int(other.imagine) < 0:
            return f"{int(self.real) + int(other.real)}" \
                   f"{int(self.imagine) + int(other.imagine)}i"
        else:
            return f"{int(self.real) + int(other.real)}+" \
                   f"{int(self.imagine) + int(other.imagine)}i"

    def __mul__(self, other):
        self.__allreal = int(self.real) * int(other.real) - \
                         int(self.imagine) * int(other.imagine)
        self.__allimagine = int(self.real) * int(other.imagine) + \
                            int(other.real) * int(self.imagine)
        if self.__allimagine > 0:
            return f"{int(self.__allreal)}+{self.__allimagine}i"
        else:
            return f"{int(self.__allreal)}{self.__allimagine}i"


mc1 = MyComplex(random.randint(-100, 100), random.randint(-100, 100))
mc2 = MyComplex(random.randint(-100, 100), random.randint(-100, 100))
print(f"Число 1: {mc1}\nЧисло 2: {mc2}")
print(f"Сумма: {mc1 + mc2}")
print(f"Произведение: {mc1 * mc2}")
