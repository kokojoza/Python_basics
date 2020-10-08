# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

try:
    with open("text.txt", "w") as f_obj:
        while True:
            content = input('введите: ')
            if len(content) == 0:
                print("Выход")
                break
            else:
                print(content, file=f_obj)
except IOError:
    print("Произошла ошибка ввода-вывода!")
