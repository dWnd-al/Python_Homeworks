"""
Задание 1.
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных
Будем считать, что год должен быть в пределах 1900 - 2023
"""
import random
from datetime import datetime


class MyDate:
    def __init__(self, date_str):
        self.date_str = date_str
        self.__nums_list = []

    def __str__(self):
        return self.date_str

    @staticmethod
    def validate_nums(dates_list):
        if 1 <= dates_list[0] <= 31 and 1 <= dates_list[1] <= 12\
                and 1900 <= dates_list[2] <= 2023:
            return f"Date is OK"
        else:
            return f"Date is incorrect"

    @classmethod
    def get_nums_2(cls, date_str):
        __nums_list = str(date_str).split("-")
        __nums_list = [int(el) for el in __nums_list]
        return MyDate.validate_nums(__nums_list)


print(f"Текущая дата: {MyDate(datetime.today().strftime('%d-%m-%Y'))} - "
      f"{MyDate.get_nums_2(datetime.today().strftime('%d-%m-%Y'))}")
rand_date = f"{random.randint(0, 50)}-{random.randint(0, 20)}-" \
            f"{random.randint(1800, 2040)}"
print(f"Случайная дата: {MyDate(rand_date)} - {MyDate.get_nums_2(rand_date)}")
