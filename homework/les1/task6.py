# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a
# километров. Каждый день спортсмен увеличивал результат на 10 % относительно
# предыдущего. Требуется определить номер дня, на который результат спортсмена составит
# не менее b километров. Программа должна принимать значения параметров a и b и выводить
# одно натуральное число — номер дня

while True:
    distance = input('Результат за первый день: ')
    if distance.isdigit():
        distance = int(distance)
        break
    print('Ошибка введено не число')

while True:
    final_distance = input('Необходимо км: ')
    if final_distance.isdigit():
        final_distance = int(final_distance)
        break
    print('Ошибка введено не число')

i = 1
while distance < final_distance:
    # print(f"{i}-й день: {distance}") расчет каждого дня
    i  += 1
    distance = distance + distance / 10
print(f"Ответ: на {i}-й день cпортсмен достиг результата — не менее: {int(distance)} км.")
