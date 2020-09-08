# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким
# финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток
# — издержки больше выручки). Выведите соответствующее сообщение. Если фирма
# отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к
# выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в
# расчете на одного сотрудника.

debit = int(input('Выручка: '))
credit = int(input('Издержки: '))
if debit < credit:
    print('Фирма убыточная')
else:
    print('Фирма прибыльная')
    profit = debit - credit
    print(f"Рентабильность = {profit / debit * 100}%")
    employees = int(input('Скольо сотрудников: '))
    print(f"Прибыль фирмы в расчете на одного сотрудника: {profit / employees}")