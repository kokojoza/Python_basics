# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.


numerals = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}

new_list = []

try:
    with open("task4.txt", encoding='UTF-8-sig') as f_obj:
        for line in f_obj:
            for key, value in numerals.items():
                if line.find(key) != -1:
                    new_list.append(line.replace(key, value))
                    break
except IOError:
    print("Произошла ошибка ввода-вывода!")


out_f = open("new_task4.txt", "w", encoding='UTF-8-sig')
out_f.writelines(new_list)
out_f.close()
