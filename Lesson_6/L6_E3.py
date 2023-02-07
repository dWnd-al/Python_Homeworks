"""
Задание 3.
Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""
import random


class Worker:
    def __init__(self, w_name, w_surname, w_pos, w_income):
        self.w_name = w_name
        self.w_surname = w_surname
        self.w_pos = w_pos
        self._w_income = w_income


class Position(Worker):
    def __init__(self, w_name, w_surname, w_pos, _w_income):
        super().__init__(w_name, w_surname, w_pos, _w_income)

    def get_full_name(self):
        return f"{self.w_name} {self.w_surname}"

    def get_total_icome(self):
        return f"{self._w_income['wage'] + self._w_income['bonus']}"


w_names = ["Вася", "Петя", "Витя", "Толя", "Саша"]
w_surnames = ["Петров", "Иванов", "Сидоров", "Семенов", "Павлов"]
w_positions = ['Манагер', 'Водятел', 'Монтажник']
empl = []
for w_line in range(5):
    dict_income = {"wage": random.randint(100, 200),
                   "bonus": random.randint(1, 25)}
    empl.append(Position(w_names[random.randint(0, 4)],
                         w_surnames[random.randint(0, 4)],
                         w_positions[random.randint(0, 2)],
                         dict_income))
    print(f"======= {empl[w_line].w_pos} =======")
    print(f"ФИО: {empl[w_line].get_full_name()}")
    print(f"Доход: {empl[w_line].get_total_icome()}")
