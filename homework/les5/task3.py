# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
# и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

def my_dict(f_name: str) -> dict:
    '''
    Преобразует строки в файле в словарь
    '''
    try:
        with open(f_name) as f_staff:
            final_list_staff = []
            str_staff = f_staff.read()
            list_staff = str_staff.split('\n')
            for el in list_staff:
                el = el.split(' ')
                final_list_staff.append(el)
            dict_staff = dict(final_list_staff)
            return dict_staff
    except IOError:
        print("Произошла ошибка ввода-вывода!")


def low_salary(dict_staff: dict) -> list:
    '''
    Определяет, кто из сотрудников имеет оклад менее 20 тыс.
    и выводит фамилии этих сотрудников в список
    '''
    try:
        list_low_salary = [key for key, value in dict_staff.items() if float(value) < 20000]
        return list_low_salary
    except ValueError:
        print('Ошибка')


def mean_salary(dict_staff: dict) -> float:
    '''
        Выполняет подсчет средней величины дохода сотрудников
    '''
    sum_salary = 0
    try:
        for key, value in dict_staff.items():
            value = float(value)
            sum_salary += value
        return sum_salary / len(dict_staff.keys())
    except ValueError:
        print('Ошибка')


if __name__ == '__main__':
    b = my_dict('task3.txt')
    print(b)
    c = low_salary(b)
    print('Сотрудники имеет оклад менее 20 тыс', c)
    d = mean_salary(b)
    print('Средняя величина дохода сотрудников', d)
