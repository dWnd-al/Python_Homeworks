"""
Задание 6.
Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать
учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
Сюда должно входить и количество занятий.
Необязательно, чтобы для каждого предмета были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр)
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
my_dict = {}
with open("L5_E6_Input.txt", encoding='utf-8') as f_pointer:
    for line in f_pointer:
        hours_line = line.rstrip()[line.rstrip().rfind(':')+1:]
        hours_real = 0
        while hours_line.find('(') != -1:
            hours_real += int(hours_line[:hours_line.find('(')])
            hours_line = hours_line[hours_line.find(')')+1:]
        my_dict[line.rstrip()[:line.rstrip().rfind(':')]] = hours_real
print(my_dict)
