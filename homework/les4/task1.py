# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы
# сотрудника. В расчете необходимо использовать формулу:
# (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

script_name, output_in_hours, rate_per_hour, premium = argv
try:
    output_in_hours, rate_per_hour, premium = float(output_in_hours), float(rate_per_hour), float(premium)
    print(f"'ЗП: '{output_in_hours * rate_per_hour + premium}")
except ValueError:
    print('Не числа')
