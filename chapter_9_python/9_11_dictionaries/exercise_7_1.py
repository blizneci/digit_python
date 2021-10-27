"""Глава 9.11. Словари"""

"""Программа принимает на вход словарь в JSON формате, значения являются
целыми числами. Программа находит минимальное значение по словарю
и печатает ключ этого значения.
"""

import json

print("Программа принимает на вход словарь.")
print("Введите словарь ниже:")
my_dict = json.loads(input())
print(f"Введенный словарь:\n{my_dict}")
MIN_VALUE = min(my_dict.values())
print(f"Минимальное значение словаря: {MIN_VALUE}")
print("Обработка в цикле for")
for key, value in my_dict.items():
    if value == MIN_VALUE:
        break
print(f"Ключ минимального значения словаря: {key}")
print("Обработка без цикла for")
key_of_min_value = min(my_dict.items(), key=lambda i: i[1])[0]
print(f"Ключ минимального значения словаря: {key_of_min_value}")
