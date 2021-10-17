"""
    Работа с аргументами командной сторки, if-else.
"""

import sys
import time

def stop_exercise():
    """Если n - функция завершает работу модуля. Если y - переходит
    к следующему упражнению."""
    answer = input("Перейти к следующему упражнению? y/n ")
    if answer == 'n':
        print("Завершение работы программы")
        time.sleep(2)
        exit()

# Глава 9.9. Работа с аргументами командной строки. if-else.
# Упражнение 5.1
# Напиши программу, которая принимает на вход два целочисленных числа,
# если оба больше 100, то выводит на печать максимальное из них,
# в противном случае вываодит на печать сумму второго и числа 112.

print("Упражнение 5.1")
if len(sys.argv) < 3:
    print("Введите числа")
    exit()
first_number_string = sys.argv[1]
second_number_string = sys.argv[2]
try:
    first_number = int(first_number_string)
    second_number = int(second_number_string)
    print(f"Число один: {first_number}, число два: {second_number}")
except ValueError:
    print("Введено не целочисленное число")
    exit()
if first_number > 100 and second_number > 100:
    print(max(first_number, second_number))
else:
    print(second_number + 112)
