# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание,
# что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import cycle
from itertools import count
from sys import argv

def generating_integers(opening_num: int, ending_num: int) -> int:
    """
    Итератор, генерирующий целые числа, начиная с указанного и заканчивая указаным числом
    opening_num - начальное число
    ending_num - конечное число
    Возвращает целые числа
    """
    for el in count(opening_num):
        if el > ending_num:
            break
        else:
            print(el)

def repeating_elements(repeat: int, step: int) -> str:
    """
    итератор, повторяющий элементы некоторого списка, определенного заранее
    c условие, при котором повторение элементов списка будет прекращено
    repeat: кол-во повторений
    step: шаг
    """
    с = 0
    for el in cycle("ABC"):
        if с > repeat:
            break
        print(el)
        с += step

proc = {
    '1': generating_integers,
    '2': repeating_elements
}

script_name, name_func, a, b = argv
try:
    proc[name_func](int(a), int(b))
except ValueError:
    print('Не числа')
except KeyError:
    print('1 или 2')
