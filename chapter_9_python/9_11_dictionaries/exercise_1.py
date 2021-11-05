"""Глава 9.11. Словари"""

"""Программа принимает на вход словарь в JSON формате, значения являются
целыми числами. Программа находит минимальное значение по словарю
и печатает ключ этого значения.
"""

import json


#my_dict = json.loads(input("Введите словарь ниже:\n"))
my_dict = json.loads('{"key1": 40, "key2": 45, "key3": 100, "key4": 555}')
print(f"Введенный словарь: {my_dict}")
MIN_VALUE = min(my_dict.values())
print(f"Минимальное значение словаря: {MIN_VALUE}")
#   for key, value in my_dict.items():
#       if value == MIN_VALUE:
#           print(key)
KEY_MIN_VALUE = min(my_dict.items(), key=lambda i : i[1])[0]
print(f"Ключ словаря с минимальным значением: {KEY_MIN_VALUE}")
