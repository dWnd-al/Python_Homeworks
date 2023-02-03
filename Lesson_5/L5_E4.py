"""
Задание 4.
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
num_dict = {"1": "Один", "2": "Два", "3": "Три", "4": "Четыре"}
out_file = open("L5_E4_Output.txt", "w", encoding='utf-8')
with open("L5_E4_Input.txt", encoding='utf-8') as f_pointer:
    for line in f_pointer:
        rus_line = num_dict.get(line.rstrip()[line.rstrip().rfind(' ') + 1:])\
            + ' - ' + line.rstrip()[line.rstrip().rfind(' ') + 1:]
        out_file.write(rus_line + '\n')
out_file.close()
# eng_line = line.rstrip()[line.rstrip().rfind(' ')+1:]
# rus_line = num_dict.get(str(eng_line)) + " - " + eng_line
