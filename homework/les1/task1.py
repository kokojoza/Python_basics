# Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные,
# выведите на экран.

name = 'Толик'
age = 18
profession = 'студент'
print(name, age, profession)

new_name = input("Введите ваше имя: ")
new_age = None
while not new_age:
    tmp = input("Введите возраст числом: ")
    if tmp.isdigit():
        new_age = int(tmp)
    else:
        print("ошибка ввода, введено не число")

new_profession = input("Чем занимаетесь? ")

print('Привет,', new_name, (new_age), new_profession, end='!', sep='-')
