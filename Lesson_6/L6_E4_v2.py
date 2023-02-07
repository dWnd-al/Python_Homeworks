"""
Задание 4.
Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""
import random
import time


class Car:
    def __init__(self, c_color, c_name, c_ispolice, c_speed):
        self.c_color = c_color
        self.c_name = c_name
        self.c_ispolice = c_ispolice
        self.c_speed = c_speed

    def is_moving(self):
        if self.c_speed > 0:
            return f"В движении"

    def is_stopped(self):
        if self.c_speed == 0:
            return f"Стоит"

    def show_speed(self):
        return self.c_speed

    def show_turn(self):
        self.direction = random.randint(0, 2)
        if self.direction == 0:
            return f"Повернул налево"
        elif self.direction == 1:
            return f"Повернул направо"
        else:
            return f"Двигается прямо"


class SportCar(Car):
    def __init__(self, c_color, c_name, c_ispolice, c_speed):
        super().__init__(c_color, c_name, c_ispolice, c_speed)


class TownCar(Car):
    def __init__(self, c_color, c_name, c_ispolice, c_speed, c_speedlimit):
        super().__init__(c_color, c_name, c_ispolice, c_speed)
        self.c_speedlimit = c_speedlimit

    def show_speed(self):
        # self.c_speed = random.randint(1, 120)
        if self.c_speed > self.c_speedlimit:
            return f"{self.c_speed}. Превышает!"
        else:
            return self.c_speed


class WorkCar(Car):
    def __init__(self, c_color, c_name, c_ispolice, c_speed, c_speedlimit):
        super().__init__(c_color, c_name, c_ispolice, c_speed)
        self.c_speedlimit = c_speedlimit

    def show_speed(self):
        if self.c_speed > self.c_speedlimit:
            return f"{self.c_speed}. Превышает!"
        else:
            return self.c_speed


class PoliceCar(Car):
    def __init__(self, c_color, c_name, c_ispolice, c_speed):
        super().__init__(c_color, c_name, c_ispolice, c_speed)


while True:
    car_type = input(f"\nЗа какой машиной наблюдаем (1, 2, 3, 4)?\n"
                     f"e-выход,\n"
                     f"Ctrl+C - вернуться к выбору машины\n")
    if car_type == 'e':
        break
    else:
        car_type = int(car_type)
        try:
            while True:
                cars = [SportCar("red", "sport car", False,
                                 random.randint(0, 200)),
                        TownCar("green", "town car", False,
                                random.randint(0, 200), 60),
                        WorkCar("yellow", "work car", False,
                                random.randint(0, 200), 40),
                        PoliceCar("blue/white", "police", True,
                                  random.randint(0, 200))]
                # print(cars[car_type - 1].show_speed())
                print(f"\n====== {cars[car_type - 1].c_name} ======")
                print(f"Цвет: {cars[car_type - 1].c_color}")
                if cars[car_type - 1].c_speed > 0:
                    print(f"Статус: {cars[car_type - 1].is_moving()}")
                    print(f"Скорость: {cars[car_type - 1].show_speed()}")
                    print(f"Направление: {cars[car_type - 1].show_turn()}")
                else:
                    print(f"Статус: {cars[car_type - 1].is_stopped()}")
                time.sleep(1)
        except KeyboardInterrupt:
            pass
