# Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные,
# выведите на экран.

name = 'Толик'
age = 18
profession = 'студент'
print(name, age, profession)

new_name = input("Введите ваше имя: ")
new_age = input("Введите ваш возраст: ")
while not new_age.isdigit():
    new_age = input("Введите возраст числом: ")

new_profession = input("Чем занимаетесь? ")

print('Привет,', new_name, int(new_age), new_profession, end='!', sep='-')