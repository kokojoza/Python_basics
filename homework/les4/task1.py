# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы
# сотрудника. В расчете необходимо использовать формулу:
# (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

def payroll(output_in_hours: float, rate_per_hour: float, premium:float) -> float:
    return output_in_hours * rate_per_hour + premium

from sys import argv

script_name, output_in_hours, rate_per_hour, premium, *_ = argv

try:
    result = payroll(float(output_in_hours), float(rate_per_hour), float(premium))
    print(f"'ЗП: '{result}")
except ValueError as e:
    print('Ошибка ввода')
    print(e)
