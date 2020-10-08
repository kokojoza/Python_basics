# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

try:
    with open("task2.txt") as f_obj:
        content = f_obj.readlines()
        print('Кол-во строк: ', len(content))
        for el in (content):
            print(f'Кол-во слов в строке {content.index(el) + 1}: ', (len(el.split(' '))))
except IOError:
    print("Произошла ошибка ввода-вывода!")
