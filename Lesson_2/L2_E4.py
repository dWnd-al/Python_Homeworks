"""
Задание 4.
Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки нужно пронумеровать.
Если слово длинное, выводить только первые 10 букв в слове.
"""
# my_string = 'тестовая оченьдлинная строка с пробелами и оченьдлинноеслово'
my_string = input("Введите строку с пробелами: ")
counter = 1
if my_string.find(' ') == -1:
    print(f"В строке нет пробелов")
else:
    for i in range(my_string.count(' ')+1):
        if my_string.find(' ') >= 0:
            # Подстрока до первого пробела
            temp_string = my_string[:my_string.find(' ')]
            # Обрезали основную строку для дальнейшего поиска
            my_string = my_string[my_string.find(' ')+1:]
        else:
            temp_string = my_string  # Если в строке не осталось пробелов
        if len(temp_string) > 10:
            print(f"{counter}: {temp_string[:10]}")
        else:
            print(f"{counter}: {temp_string}")
        counter += 1
