"""
Задание 5.
Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение «Запуск отрисовки»; создать три дочерних класса
Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw.
Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, s_title):
        self.s_title = s_title

    def s_draw(self):
        return f"Рисуем"


class Pen(Stationery):
    def __init__(self, s_title):
        super().__init__(s_title)

    def s_draw(self):
        return f"Рисуем инструментом: {self.s_title}"


class Pencil(Stationery):
    def __init__(self, s_title):
        super().__init__(s_title)

    def s_draw(self):
        return f"Рисуем инструментом: {self.s_title}"


class Handle(Stationery):
    def __init__(self, s_title):
        super().__init__(s_title)

    def s_draw(self):
        return f"Рисуем инструментом: {self.s_title}"


s_pen = Pen("ручка")
s_pencil = Pencil("карандаш")
s_handle = Handle("маркер")
print(s_pen.s_draw())
print(s_pencil.s_draw())
print(s_handle.s_draw())
