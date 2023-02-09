"""
Задание 1.
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31    32         3    5    32        3    5    8    3
37    43         2    4    6         8    3    7    1
51    86        -1   64   -8
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

Для простоты считаем квадратную матрицу
"""
import random


class Matrix:
    def __init__(self, input_list):
        self.input_list = input_list
        self.__result_matrix = ''

    def __str__(self):
        for m_row in range(len(self.input_list)):
            self.__result_matrix +=\
                ' '.join(str(elem) for elem in self.input_list[m_row]) + '\n'
        return f"{self.__result_matrix}"

    def __add__(self, other):
        for r_row in range(len(self.input_list)):
            for r_line in range(len(self.input_list[r_row])):
                self.input_list[r_row][r_line] +=\
                    other.input_list[r_row][r_line]
        return Matrix(self.input_list)


m_first = []
m_second = []
m_size = int(input("Размер мартицы (m x m): "))
for el in range(m_size):
    m_first.append([random.randint(0, 100) for elm1 in range(m_size)])
    m_second.append([random.randint(0, 100) for elm2 in range(m_size)])
m1 = Matrix(m_first)
m2 = Matrix(m_second)
print(f"Матрица 1\n{m1}")
print(f"Матрица 2\n{m2}")
print(f"Сумма матриц:\n{m1 + m2}")
