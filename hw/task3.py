# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

months_list = ['Зима', 'Весна', 'Лето', 'Осень']

months_dict = {
    'Зима': [12, 1, 2],
    'Весна': [3, 4, 5],
    'Лето': [6, 7, 8],
    'Осень': [9, 10, 11]
}

while True:
    user_month = input('Введите номер месяца: \n')
    if user_month.isdigit() and int(user_month) > 0 and int(user_month) <= 12:
        user_month = int(user_month)
        break

    print('Ошибка ввода')

season = user_month // 3 % 4
print(months_list[season])

for key, value in months_dict.items():
    if user_month in value:
        print(f"Время года: {key}")
        break
