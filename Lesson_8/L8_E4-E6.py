"""
Задание 4.
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
Задание 5.
Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в
определённое подразделение компании. Для хранения данных о наименовании и количестве единиц
оргтехники, а также других данных, можно использовать любую подходящую структуру (например, словарь).
Задание 6.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
"""
import random


def get_scanners():
    sc_list = []
    with open("scanners_list.txt", encoding='utf-8') as in_file:
        for line in in_file:
            sc_list.append(line.rstrip().split(','))
    return sc_list


def get_printers():
    pr_list = []
    with open("printers_list.txt", encoding='utf-8') as in_file:
        for line in in_file:
            pr_list.append(line.rstrip().split(','))
    return pr_list


class GlobalStorage:
    def __init__(self, address, square, storage_id):  # , hw_id, hw_quantity):
        self.address = address
        self.square = square
        self.storage_id = storage_id
        self.stored = []

    def __str__(self):
        return self.stored

    @classmethod
    def get_to_storage(cls, hw_type, hw_id, hw_quantity):
        stored = [hw_type, hw_id, hw_quantity]
        return stored

    @classmethod
    def send_to_branch(cls, hw_type, hw_id, hw_quantity, branch_id):
        sent_to_br = [hw_type, hw_id, hw_quantity, branch_id]
        return sent_to_br


class AllTech:
    def __init__(self, techtype, vendor_name, model):
        self.techtype = techtype
        self.vendor_name = vendor_name
        self.model = model


class Printer(AllTech):
    def __init__(self, techtype, vendor_name, model,
                 printer_type, is_mfp, serial_num):
        super().__init__(techtype, vendor_name, model)
        self.printer_type = printer_type
        self.is_mfp = is_mfp
        self.serial_num = serial_num

    def __str__(self):
        return f"{self.techtype} {self.vendor_name} {self.model} " \
               f"{self.printer_type} {self.is_mfp} {self.serial_num}"


class Scanner(AllTech):
    def __init__(self, techtype, vendor_name, model, scanner_type,
                 serial_num):
        super().__init__(techtype, vendor_name, model)
        self.scannner_type = scanner_type
        self.serial_num = serial_num

    def __str__(self):
        return f"{self.techtype} {self.vendor_name} {self.model} " \
               f"{self.scannner_type} {self.serial_num}"


class IncorrectInput(Exception):  # если вместо числа ввели символ
    def __str__(self):
        return f"Ошибка, введено не число"


# подготовка (списки с оборудованием и т.д.)
printers_list = get_printers()
scanners_list = get_scanners()
printer_class_list = []  # список экземпляров класса принтеров
scanner_class_list = []  # список экземпляров класса сканеров
for el in range(8):
    printer_class_list.append(Printer(
        printers_list[el][0], printers_list[el][1],
        printers_list[el][2], printers_list[el][3],
        printers_list[el][4], printers_list[el][5]))
for el in range(8):
    scanner_class_list.append(Scanner(
        scanners_list[el][0], scanners_list[el][1],
        scanners_list[el][2], scanners_list[el][3],
        scanners_list[el][4]))
global_storage = GlobalStorage("Address_1", "100500", 'storage_id')
global_storage_list = []  # Список оборудования на складе
"""
Заполняем склад
Тип оборудования, модель и количество
"""
for el in range(8):
    global_storage_list.append(
        global_storage.get_to_storage(printer_class_list[el].techtype,
                                      printer_class_list[el].model,
                                      random.randint(10, 30)))
for el in range(8):
    global_storage_list.append(
        global_storage.get_to_storage(scanner_class_list[el].techtype,
                                      scanner_class_list[el].model,
                                      random.randint(10, 30)))
print("На складе: ")
for el in range(16):
    print(f"{global_storage_list[el]}")
"""
Список переданного оборудования
Тип оборудования, модель, количество и id офиса
"""
sent_hw_list = []  # Список переданного оборудования
for el in range(2):
    random_hw = random.randint(0, 7)
    sent_hw_list.append(
        global_storage.send_to_branch(printer_class_list[random_hw].techtype,
                                      printer_class_list[random_hw].model,
                                      3,
                                      "Office_" + str(random.randint(1, 3))))
    random_hw = random.randint(0, 7)
    sent_hw_list.append(
        global_storage.send_to_branch(scanner_class_list[random_hw].techtype,
                                      scanner_class_list[random_hw].model,
                                      random.randint(1, 5),
                                      "Office_" + str(random.randint(1, 3))))
print("Передано: ")
for el in range(4):
    print(f"{sent_hw_list[el]}")
# Проверка класса исключений
my_str = input(f"Введите количество принтеров {printer_class_list[0].model}"
               f" для отправки в Office_5: ")
try:
    if my_str.isnumeric() is False:
        raise IncorrectInput
except IncorrectInput as my_error:
    print(my_error)
else:
    sent_hw_list.append(
        global_storage.send_to_branch(printer_class_list[0].techtype,
                                      printer_class_list[0].model,
                                      int(my_str), "Office_5"))
    print("Передано: ")
    for el in range(5):
        print(f"{sent_hw_list[el]}")
