"""
Задание 2.
Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для
основных классов проекта, проверить на практике работу декоратора @property.
"""
import random
from abc import ABC, abstractmethod


class Outfit(ABC):
    def __init__(self, name, material):
        self.material = material
        self.name = name

    @abstractmethod
    def __mul__(self, other):
        pass

    @abstractmethod
    def quan(self):
        pass


class Coat(Outfit):
    def __init__(self, name, material, v_size):
        super().__init__(name, material)
        self.__v_size = v_size

    def __mul__(self, other):
        return self.quan() * other
        # return self.quantity(self.__v_size) * other

    def quan(self):
        return self.__v_size / 6.5 + 0.5

    """
    @staticmethod
    def quantity(__v_size):
        return __v_size / 6.5 + 0.5
    """

    @property
    def one_piece(self):
        return self.__v_size / 6.5 + 0.5


class Suit(Outfit):
    def __init__(self, name, material, h_size):
        super().__init__(name, material)
        self.__h_size = h_size

    def __mul__(self, other):
        return self.quan() * other
        # return self.quantity(self.__h_size) * other

    def quan(self):
        return self.__h_size * 2 + 0.3

    """
    @staticmethod
    def quantity(__h_size):
        return __h_size * 2 + 0.3
    """

    @property
    def one_piece(self):
        return self.__h_size * 2 + 0.3


my_c = Coat("'Пальто 1'", "'some_material 1'", 50)
my_s = Suit("'Костюм 1'", "'some_material 2'", 1.90)
lst = [my_c, my_s]
a = 0
c_quant = 0
for el in lst:
    c_quant = random.randint(1, 10)
    a += el * c_quant
    print(f"Ткани {el.material} на {c_quant} шт. {el.name} "
          f"надо {round(el * c_quant, 2)} метров")
    print(f"Ткани на 1 штуку {round(el.one_piece, 2)} метров")
print(f"Ткани всего надо {round(a, 2)} метров")
