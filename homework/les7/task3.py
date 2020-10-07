# 3. Реализовать программу работы с органическими клетками.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
# соответствующий количеству клеток (целое число). В классе должны быть реализованы
# методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
# деление (__truediv__()).Данные методы должны применяться только к клеткам
# и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное)
# деление клеток, соответственно. В методе деления должно осуществляться
# округление значения до целого числа.

class Cell:
    def __init__(self, qt_cell: int):
        self.qt_cell = qt_cell

    def __add__(self, other):
        return self.qt_cell + other.qt_cell

    def __sub__(self, other):
        if self.qt_cell > other.qt_cell:
            return self.qt_cell - other.qt_cell
        else:
            return "разность меньше 0"

    def __mul__(self, other):
        return self.qt_cell * other.qt_cell

    def __truediv__(self, other):
        if other.qt_cell > 0:
            return round(self.qt_cell / other.qt_cell)
        else:
            return "на 0 не делим"

    def make_order(self, qt_cell):
        return '\n'.join('*' * qt_cell for _ in range(self.qt_cell // qt_cell)) + '\n' + '*' * (self.qt_cell % qt_cell)


if __name__ == '__main__':
    a = Cell(11)
    b = Cell(0)
    print(f'{a / b}')
    print(a.make_order(3))
