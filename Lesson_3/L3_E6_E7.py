"""
Задание 6.
Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Задание 7.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки,
но каждое слово должно начинаться с заглавной буквы. Используйте написанную ранее функцию int_func().

Использовал upper() вместо capitolize(), т.к. ничего не сказано про остальные части слова.
По умолчанию считаю, что изменять их нельзя
"""


# 1 вариант. Предварительная обработка строки в коде программы
def int_func(arg_str):
    return arg_str[0].upper()+arg_str[1:]


# 2 вариант. И одно слово, и строку обрабатываем в функции
def int_func2(arg_str):
    rs_string = ''
    for k in range(arg_str.count(' ') + 1):
        if arg_str.find(' ') >= 0:
            tmp_str = arg_str[:arg_str.find(' ')]
            arg_str = arg_str[arg_str.find(' ') + 1:]
        else:
            tmp_str = arg_str
        rs_string += tmp_str[0].upper()+tmp_str[1:] + " "
    return rs_string[:-1]


# Задание 6
my_word = input("Word: ")
print(int_func(my_word))
# Задание 7
my_string = input("String: ")
my_string2 = my_string
res_string = ''
for i in range(my_string.count(' ')+1):
    if my_string.find(' ') >= 0:
        temp_string = my_string[:my_string.find(' ')]
        my_string = my_string[my_string.find(' ') + 1:]
    else:
        temp_string = my_string
    res_string += int_func(temp_string) + " "
print(res_string[:-1])
# Оба задания функцией int_func2
print(int_func2(my_word))
print(int_func2(my_string2))
