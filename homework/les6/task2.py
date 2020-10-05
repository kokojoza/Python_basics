# 2. Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина). Значения данных атрибутов должны передаваться
# при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т


class Road:
    def __init__(self, length, width):
        self._length = float(length)
        self._width = float(width)

    def all_asphalt_masses(self, asphalt_mass, asphalt_thickness):
        return self._length * self._width * asphalt_mass * asphalt_thickness


if __name__ == '__main__':
    a = Road(20, 5000)
    print(a.all_asphalt_masses(25, 5))
