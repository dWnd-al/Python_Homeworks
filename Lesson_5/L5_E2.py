"""
Задание 2.
Создать текстовый файл (не программно), сохранить в нём несколько строк,
выполнить подсчёт строк и слов в каждой строке.
"""
counter = 1
with open("L5_E2_Input.txt", encoding='utf-8') as in_file:
    for line in in_file:
        print(f"В строке {counter} - {len(line.split())} слов")
        counter += 1
print(f"В файле {counter-1} строк")
# in_file = open("L5_E2_Input.txt", encoding='utf-8')
# in_file.close()
