# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса
# Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки: {self.title}')


class Pen(Stationery):
    def __init__(self):
        super().__init__('Ручка')

    def draw(self):
        super().draw()
        return 'Рисуем ручкой.'


class Pencil(Stationery):
    def __init__(self):
        super().__init__('Карандаш')

    def draw(self):
        super().draw()
        return 'Рисуем карандашом.'


class Handle(Stationery):
    def __init__(self):
        super().__init__('Маркер')

    def draw(self):
        super().draw()
        return 'Рисуем маркером.'


if __name__ == '__main__':
    pen1 = Pen()
    print(pen1.draw())

    pencil1 = Pencil()
    print(pencil1.draw())

    handle1 = Handle()
    print(handle1.draw())
