'''
Задание 4.
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
'''
number = int(input("Целое положительное число: "))
if number > 10:
    highest_number = -1
    while number > 10:
        last_digit = number % 10
        number //= 10
        if last_digit > highest_number:
            highest_number = last_digit
    print("Самая большая цифра введенного числа:", highest_number)
