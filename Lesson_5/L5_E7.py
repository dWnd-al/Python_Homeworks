"""
Задание 7.
Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
"""
import json
company_dict = {}
avg_profit_dict = {"Avg. profit": ''}
with open("L5_E7_Input.txt", encoding='utf-8') as f_pointer:
    counter = 0
    avg_profit = 0
    for line in f_pointer:
        in_line = line.rstrip().split()
        company_dict[in_line[0]] = int(in_line[2])-int(in_line[3])
        if int(company_dict[in_line[0]]) > 0:
            avg_profit += int(company_dict[in_line[0]])
            counter += 1
    avg_profit_dict["Avg. profit"] = round(avg_profit / counter, 2)
    company_list = list([company_dict, avg_profit_dict])
    print(company_list)
with open('L5_E7_Output.json', "w+", encoding='utf-8') as j_poiter:
    json.dump(company_list, j_poiter)
    # Прочитаем в качестве теста
    j_poiter.seek(0)
    print(json.load(j_poiter))
