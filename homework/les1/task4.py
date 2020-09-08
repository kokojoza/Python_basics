# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = input('Введите целое положительное число: ')
while not number.isdigit():
    number = input("Введите целое положительное число: ")
number = int(number)
numeral = 0
while number > 0:
    if (number % 10) > numeral:
        numeral = number % 10
    number //= 10
print('Самая большая цифра в числе: ', numeral)