
"""Глава 9.11. Словари"""

"""Программа принимает на вход строку, в этой строке четное кол-во слов,
разделенных пробелами (2, 4, 6, 8 или больше).
Сформируй словарь так, чтобы нечетные слова были ключами словаря,
а четные - значениями по этим ключам.
Выведи этот словарь на печать так:
print(json.dumps(my_dict, ensure_ascii=False)).
Функция json.dumps выполняет преобразование переданного в нее
словаря в формат данных JSON.
Если кол-во слов нечетное - программа игнорирует последнее слово.
Возможно пригодится функция range.
Sample Input:
echo "name Петр phone 02 sex male balance 50000" | python3.9 gen_dict.py
и она печатет:
{"name": "Петр", "phone": "02", "sex": "male", "balance": "50000"}
"""

import json

my_dict_list = input().split()
print(f"Введенная строка:\n{my_dict_list}")
if len(my_dict_list).__mod__(2):
    del my_dict_list[-1]

my_dict = {my_dict_list[i]: my_dict_list[i + 1] for i in range(0, len(my_dict_list), 2)}

#my_dict = dict(zip(my_dict_list[::2], my_dict_list[1::2]))
print(json.dumps(my_dict, ensure_ascii=True))
