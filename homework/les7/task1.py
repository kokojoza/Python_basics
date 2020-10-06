# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
# класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
# первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.




class Matrix:
    def __init__(self, data:list):
        self.data = data

    def __str__(self):
        _result = ''
        for i in self.data:
            _result += ' '.join(map(str, i)) + '\n'
        return _result

    def __add__(self, other):
        _new_matrix = self.data
        try:
            for i in range(len(self.data)):
                for j in range(len(self.data[0])):
                    _new_matrix[i][j] = self.data[i][j] + other.data[i][j]
            return Matrix(_new_matrix)
        except IndexError:
            print('Ошибка')


if __name__ == '__main__':
    a = Matrix([[1, 2, 3, 4], [5, 6, 7, 8]])
    print(a)
    b = Matrix([[1, 2, 3, 4], [5, 6, 7, 8]])
    c = a + b
    print(c)
    e = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(e)
    r = Matrix([[1.9, 2.8, 3.7], [4, 5, 6]])
    t = e + r
    print(t)
