# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

while True:
    number = input('Введите целое положительное число: ')
    if number.isdigit():
        number = int(number)
        break
    print('Ошибка введено не число')
numeral = 0
while number > 0:
    if (number % 10) > numeral:
        numeral = number % 10
    number //= 10
print('Самая большая цифра в числе: ', numeral)
