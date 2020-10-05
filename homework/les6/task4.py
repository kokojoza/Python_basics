# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
# о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Car:
    def __init__(self, speed: int, color: str, name: str, is_police: bool = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина стоит')

    def turn(self, direction):
        if direction == 'лево':
            print('Поворот налево')
        elif direction == 'право':
            print('Поворот направо')
        else:
            print('Непонятно')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 60:
            print(f'{self.speed} -- Привешение скорости')
        else:
            super().show_speed()


class SportCar(Car):
    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name)


class WorkCar(Car):
    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 40:
            print(f'{self.speed} -- Привешение скорости')
        else:
            super().show_speed()


class PoliceCar(Car):
    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name, True)


if __name__ == '__main__':
    a = Car(300, 'красная', 'Tesla')
    print(a.name)
    a.go()
    a.stop()
    a.turn('лево')
    a.show_speed()

    b = TownCar(100, 'белая', 'Лада')
    print(b.name)
    b.show_speed()
    b1 = TownCar(20, 'белая', 'Лада')
    b1.show_speed()

    c = WorkCar(50, 'ржавая', 'ЗаЗ')
    c.show_speed()
    print(c.is_police)

    p = PoliceCar(40, 'спец', 'Уаз')
    print(p.is_police)
