"""Глава 9.11. Словари"""

"""Программа принимает на вход словарь в JSON формате, значения являются
целыми числами. Программа находит минимальное значение по словарю
и печатает ключ этого значения.
"""

import json


my_dict = json.loads(input("Введите словарь\n"))
MIN_VALUE = min(my_dict.values())
for key, value in my_dict.items():
    if value == MIN_VALUE:
        print(key)
