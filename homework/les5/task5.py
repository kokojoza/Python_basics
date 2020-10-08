# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


def num_sum_in_file(file_name: str) -> float:
    try:
        with open(file_name) as f_obj:
            try:
                numbers_str = f_obj.read()
                num_sum = [float(el) for el in numbers_str.split(' ') if el != '']
                return sum(num_sum)
            except ValueError:
                print("Не число")
    except IOError:
        print("Произошла ошибка ввода-вывода!")


if __name__ == '__main__':
    try:
        with open("task5.txt", "w") as f_obj:
            for i in range(1, 177, 3):
                print(f'{i}', file=f_obj, end=' ')
    except IOError:
        print("Произошла ошибка ввода-вывода!")

    print(num_sum_in_file('task5.txt'))
