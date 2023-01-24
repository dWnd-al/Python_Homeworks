"""
Задание 1.
Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""
list_1 = [1, 'safds']
tuple_string = ("tuple", 8)
my_var = {'set', 5}
my_dict = {"Var_1": 100, "Var_2": True}
my_list = [2, 3.1415926, 'some text', None, False, complex(5, 6),
           list_1, tuple_string, my_var, my_dict]
print(f"Список: {my_list}")
for position_in_list in range(len(my_list)):
    print(f"Тип элемента \"{my_list[position_in_list]}\" - "
          f"{str(type(my_list[position_in_list]))[8:-2]}")
