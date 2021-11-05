"""Глава 9.11. Словари"""

"""Измени программу из прошлого урока так, чтоы в полученном словаре
значение ключа special_key было рано 12.
Получившийс dict выводится на печать аналогично прошлому разу
с использованием json.dumps.
Sample Input:
name Петр phone 02 sex male balance 50000
Sample Output:
{"name": "Петр", "phone": "02", "sex": "male", "balance": "50000", "special_key": 12}
"""

import json

my_dict_list = input().split()
print(f"Введенная строка:\n{my_dict_list}")
if len(my_dict_list).__mod__(2):
    del my_dict_list[-1]

my_dict = {my_dict_list[i]: my_dict_list[i + 1] for i in range(0, len(my_dict_list), 2)}

#my_dict = dict(zip(my_dict_list[::2], my_dict_list[1::2]))
my_dict["special_key"] = 12
print(json.dumps(my_dict, ensure_ascii=True))
