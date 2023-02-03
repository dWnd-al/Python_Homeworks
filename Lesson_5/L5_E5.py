"""
Задание 5.
Создать (программно) текстовый файл, записать в него программно набор чисел,
разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
"""
import random
with open("L5_E5_Output.txt", "w+", encoding='utf-8') as f_pointer:
    long_str = ''
    for i in range(random.randint(20, 30)):
        long_str = long_str + str(random.randint(0, 100)) + ' '
    f_pointer.write(long_str)
    f_pointer.seek(0)
    int_list = f_pointer.read().split()
    int_list = [int(x) for x in int_list]
    print(f"Суммма чисел: {sum(int_list)}")
