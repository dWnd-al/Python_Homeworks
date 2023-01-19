'''
Задание 2.
Пользователь вводит время в секундах.
Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
'''
seconds = int(input("Время в секундах: "))
if seconds < 0:
    seconds *= (-1)
minutes = seconds // 60
hours = minutes // 60
minutes -= hours * 60
seconds -= (seconds // 60) * 60
time = [str(hours), str(minutes), str(seconds)]
for i in range(3):
    if len(time[i]) == 1:
        time[i] = "0" + time[i]
print(f"Время в формате hh:mm:ss: {':'.join(time)}")
