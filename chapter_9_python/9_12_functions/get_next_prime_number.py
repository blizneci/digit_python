"""
Функция get_next_prime_number принимает целое положительное число
и возвращает первое простое число, большее заданного.
Функция is_prime_number проверяет является ли переданное число простым.
Простое число делится без остатка только на себя и на единицу.
Внутри get_next_prime_number вызывается is_prime_number, которая
принимает на вход целое полжительное число и возвращает True/False
в зависимости от того, является ли это число простым или нет.
"""


def get_next_prime_number(number):
    """Возвращает следующее простое число"""
    set_numbers = set(range(2, number + 1))
    set_prime_numbers = set()
    while set_numbers:
        i = min(set_numbers)
        set_prime_numbers.add(i)
        set_numbers -= set(range(i, (number + 1), i))
   # print(sorted(set_prime_numbers))

    not_prime_flag = True
    next_number = number 
    while not_prime_flag:
        next_number += 1 
        for i in set_prime_numbers:
            if next_number % i == 0:
                not_prime_flag = True
                break
            not_prime_flag = False
    next_prime_number = next_number

    return next_prime_number

count = 10
while count != 0:
    answer = input("Введите целое число, введите q для выхода:")
    if answer == 'q':
        break
    number = int(answer)
    print(f"Введено число: {number}")
    next_prime_number = get_next_prime_number(number)
    print(f"Следующее действительно простое число: {next_prime_number}")
    count -= 1
