"""
Задание 5.
Программа запрашивает у пользователя строку чисел, разделённых пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введён после нескольких чисел, то вначале нужно добавить
сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""


def summ_count(input_string, prev_summ):
    # Сначала уберем пробелы с конца и с начала и двойные пробелы
    input_string = input_string.strip()
    input_string = " ".join(input_string.split())
    num_list = []
    # Строку в список
    while input_string.find(" ") > 0:
        num_list.append(int(input_string[:input_string.find(" ")]))
        input_string = input_string[input_string.find(" ")+1:]
    num_list.append(int(input_string))
    print(f"Сумма чисел с учетом предыдущего ввода: "
          f"{prev_summ + sum(num_list)}")
    return sum(num_list)


global_summ = 0
while True:
    input_str = input('Введите строку чисел через пробелы\n'
                      'Для расчета нажмите Enter\n'
                      'Для завершения введите e\n')
    """
    Смотрим на последний введенный символ, если это e - завершаем цикл
    Заодно проверяем, ввел пользователь какие-либо числа перед e или нет
    """
    if input_str[-1] == 'e'\
            and any(st.isdigit() for st in input_str):
        global_summ += summ_count(input_str[:-1], global_summ)
        break
    elif input_str[-1] == 'e'\
            and any(st.isdigit() for st in input_str) is False:
        global_summ += summ_count("0", global_summ)
        break
    else:
        # Считаем сумму
        global_summ += summ_count(input_str, global_summ)
