"""Глава 9.10. Множества"""

# Упражнение 3.1
# Программа принимает на вход строку. Напиши код, который убирает все
# повторяющиеся символы из этой строки и выводит на печать получившуюся
# строку. Порядок символов должен сохраниться.

print("Упражнение 3.1")
input_string = input("Введите строку ниже\n")
print(f"Введенная строка: {input_string}")
output_string = ''.join(sorted(set(input_string)))
print(f"Отсортированная строка без дублей: {output_string}")