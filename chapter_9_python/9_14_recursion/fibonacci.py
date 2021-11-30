"""Модуль для поиска чисел Фибоначчи
Рекурсивная и нерекурсивная реализация алгоритма поиска."""

def get_fib_rec(n):
    """Рекурсивный поиск n-го числа Фибоначчи"""
    if n in (1, 2):
        return 1
    else:
        return get_fib_rec(n - 1) + get_fib_rec(n - 2)

def get_fib_iter(n):
    fib1 = fib2 = 1
    if n in (1, 2):
        return 1
    else:
        for i in range(0, n - 2):
            fib = fib1 + fib2
            fib1, fib2 = fib2, fib1 + fib2
        return fib


n = int(input('Введите номер числа Фибоначчи \n'))
print(f'Поиск {n}-го числа Фибоначчи')
#print(f'Рекурсивный поиск: {get_fib_rec(n)}')
print(f'Итеративный поиск: {get_fib_iter(n)}')
