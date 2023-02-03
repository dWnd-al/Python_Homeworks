"""
Задание 1.
Создать программный файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая строка.
"""
out_file = open("L5_E1_Output.txt", "w", encoding='utf-8')
while True:
    tmp_str = input()
    if len(tmp_str) > 0:
        out_file.write(tmp_str + '\n')
    else:
        break
out_file.close()
