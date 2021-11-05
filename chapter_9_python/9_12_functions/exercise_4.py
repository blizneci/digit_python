"""
Функция get_next_prime_number принимает целое положительное число
и возвращает первое простое число, большее заданного.
Функция is_prime_number проверяет является ли переданное число простым.
Простое число делится без остатка только на себя и на единицу.
Внутри get_next_prime_number вызывается is_prime_number, которая
принимает на вход целое полжительное число и возвращает True/False
в зависимости от того, является ли это число простым или нет.
"""

def is_prime_number(number):
    prime_flag = True
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            prime_flag = False
            break
    return prime_flag

def get_next_prime_number(number):
    while True:
        number += 1
        print(f"Следующее возможное простое число: {number}")
        if is_prime_number(number):
            next_prime_number = number
            break
    return next_prime_number

while True:
    answer = input("Введите число, введите q для выхода\n")
    if answer == 'q':
        break 
    number = int(answer)
    print(get_next_prime_number(number))