"""
Задание 3.
Реализовать программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное
(с округлением до целого) деление клеток, соответственно.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки.
Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
иначе выводить соответствующее сообщение.
Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как произведение количества
ячеек этих двух клеток.
Деление. Создаётся общая клетка из двух.
Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
"""


class Cell:
    def __init__(self, subcells, r_length):
        self.subcells = subcells
        self.r_length = r_length
        self.out_str = ''

    def __str__(self):
        return str(self.subcells)

    def __add__(self, other):
        self.subcells += other.subcells
        return Cell(str(self.subcells), self.r_length)

    def __sub__(self, other):
        self.subcells -= other.subcells
        return Cell(str(self.subcells), self.r_length)

    def __mul__(self, other):
        self.subcells *= other.subcells
        return Cell(str(self.subcells), self.r_length)

    def __truediv__(self, other):
        self.subcells /= other.subcells
        return Cell(str(int(self.subcells)), self.r_length)

    def makeorder(self):
        self.out_str = ''
        count = 0
        for el in range(self.subcells // self.r_length):
            for el1 in range(self.r_length):
                self.out_str += "*"
            self.out_str += '\n'
            count += 1
        if self.subcells - self.r_length * count > 0:
            self.out_str += '*' * (self.subcells - self.r_length * count) + '\n'
        print(self.out_str)

    def mkordr(self, r_len):
        self.out_str = ''
        count = 0
        for el in range(self.subcells // r_len):
            for el1 in range(r_len):
                self.out_str += "*"
            self.out_str += '\n'
            count += 1
        if self.subcells - r_len * count > 0:
            self.out_str += '*' * (self.subcells - r_len * count) + '\n'
        print(self.out_str)


def input_vars():
    g_c1 = input("Введите кол-во ячеек клетки 1: ")
    g_c2 = input("Введите кол-во ячеек клетки 2: ")
    g_l = input("Введите длину ряда: ")
    return [g_c1, g_c2, g_l]


basic_vars = input_vars()
cell1 = Cell(int(basic_vars[0]), int(basic_vars[2]))
cell2 = Cell(int(basic_vars[1]), int(basic_vars[2]))
my_divider = "==========================="
print(f"{my_divider}")
while True:
    print(f"Кол-во ячеек клетки 1: {cell1.subcells}\n"
          f"Кол-во ячеек клетки 2: {cell2.subcells}\n"
          f"Длина ряда: {basic_vars[2]}\n{my_divider}")
    selection = input("Что будем запускать?\n"
                      "1 - сложение\n"
                      "2 - вычитание\n"
                      "3 - умножение\n"
                      "4 - деление\n"
                      "5 - организация по рядам, решение 1 "
                      "(на примере первой клетки)\n"
                      "6 - организация по рядам, решение 2 "
                      "(на примере второй клетки)\n"
                      "0 - повторно ввести данные\n"
                      "e - выход\n")
    if selection == "e":
        break
    elif selection == "0":
        basic_vars = input_vars()
        cell1 = Cell(int(basic_vars[0]), int(basic_vars[2]))
        cell2 = Cell(int(basic_vars[1]), int(basic_vars[2]))
        print(f"{my_divider}")
    elif selection == "1":
        tmp_cell = Cell(int(basic_vars[0]), int(basic_vars[2]))
        print(f"{my_divider}\nСумма ячеек: {tmp_cell + cell2}"
              f"\n{my_divider}")
    elif selection == "2":
        if cell1.subcells < cell2.subcells:
            print(f"{my_divider * 2}\nВ данном случае нельзя вычитать "
                  f"из меньшего большее\n{my_divider * 2}")
        else:
            tmp_cell = Cell(int(basic_vars[0]), int(basic_vars[2]))
            print(f"{my_divider}\nРазность ячеек: {tmp_cell - cell2}"
                  f"\n{my_divider}")
    elif selection == "3":
        tmp_cell = Cell(int(basic_vars[0]), int(basic_vars[2]))
        print(f"{my_divider}\nПроизведение ячеек: {tmp_cell * cell2}"
              f"\n{my_divider}")
    elif selection == "4":
        tmp_cell = Cell(int(basic_vars[0]), int(basic_vars[2]))
        try:
            print(f"{my_divider}\nЧастное от деления ячеек:"
                  f" {tmp_cell / cell2}\n{my_divider}")
        except ZeroDivisionError:
            print(f"{my_divider}\nНа ноль делить нельзя!\n{my_divider}")
    elif selection == "5":
        cell1.makeorder()
    elif selection == "6":
        cell2.mkordr(int(basic_vars[2]))
