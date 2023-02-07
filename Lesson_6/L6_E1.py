"""
Задание 1.
Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов.
При его нарушении выводить соответствующее сообщение и завершать скрипт.

Включение светофора переключением не считаем
"""
import time
import random


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def switch(self):
        if self.__color == 'red':
            for delay in range(7):
                print(delay + 1)
                time.sleep(1)
            self.__color = 'yellow'
        elif self.__color == 'yellow':
            for delay in range(2):
                print(delay + 1)
                time.sleep(1)
            self.__color = 'green'
        elif self.__color == 'green':
            for delay in range(3):
                print(delay + 1)
                time.sleep(1)
            self.__color = 'red'
        return self.__color


starting_light = ['red', 'yellow', 'green']
curr_light = starting_light[random.randint(0, 2)]
print(f"Запустили светофор, для остановки Ctrl+C\n"
      f"Светофор включили со светом:\n{curr_light}")
sw_over = 1
try:
    while True:
        tr_light = TrafficLight(curr_light)
        curr_light = tr_light.switch()
        print(f"\nПереключение {sw_over}\nТекущий свет: {curr_light}\n")
        sw_over += 1
except KeyboardInterrupt:
    pass
