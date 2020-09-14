# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким
# финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток
# — издержки больше выручки). Выведите соответствующее сообщение. Если фирма
# отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к
# выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в
# расчете на одного сотрудника.

while True:
    debit = input('Выручка: ')
    if debit.isdigit():
        debit = int(debit)
        break
    print('Ошибка введено не число')

while True:
    credit = input('Издержки: ')
    if credit.isdigit():
        credit = int(credit)
        break
    print('Ошибка введено не число')

if debit < credit:
    print('Фирма убыточная')
elif debit == credit:
    print('Работает в 0')
else:
    print('Фирма прибыльная')
    profit = debit - credit
    print(f"Рентабильность = {profit / debit * 100}%")

    while True:
        employees = input('Скольо сотрудников: ')
        if employees.isdigit():
            employees = int(employees)
            break
        print('Ошибка введено не число')

    print(f"Прибыль фирмы в расчете на одного сотрудника: {profit / employees}")
