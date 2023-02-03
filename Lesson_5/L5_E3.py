"""
Задание 3.
Создать текстовый файл (не программно).
Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
Выполнить подсчёт средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""
salary_list = []
names_list = []
empl = 0
with open("L5_E3_Input.txt", encoding='utf-8') as f_pointer:
    for line in f_pointer:
        salary_list.append(float(line.rstrip()[line.rstrip().find(' ')+1:]))
        names_list.append(line.rstrip()[:line.rstrip().find(' ')])
        empl += 1
# Ищем сотрудников с з/п < 20000
for i in range(empl):
    if salary_list[i] < 20000:
        print(f"{names_list[i]} - {salary_list[i]}")
print(f"Средний доход: {sum(salary_list) / empl}")
# in_file = open("L5_E3_Input.txt", encoding='utf-8')
# in_file.close()
