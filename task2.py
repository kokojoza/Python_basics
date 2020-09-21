# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_information(name: str, surname: str, year_of_birth: int, сity: str, email: str, tel: int) -> str:
    """Возвращает данные о пользователе одной строкой"""

    return f"{name} {surname} {year_of_birth} {сity} {email} {tel}"

# print(user_information(name="Рома", surname="Иванов", year_of_birth=1988, сity="Чита", email="roma.ivanov@mail.ru", tel=1234567890))
