"""
Задание 3.
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и dict.
"""
# Решение через list
season_list = ["зимнего", "зимнего", "весеннего", "весеннего",
               "весеннего", "летнего", "летнего", "летнего",
               "осеннего", "осеннего", "осеннего", "зимнего"]
month = int(input("Введите номер месяца: "))
if 12 < month or month < 1:
    print(f"Ввод некорректный. Нет месяца с номером {month}")
else:
    print(f"Введен номер {season_list[month-1]} месяца")
