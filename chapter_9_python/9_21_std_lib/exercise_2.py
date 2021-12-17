"""
Напиши программу, которая принимает на вход строку с JSON.
Этот JSON надо разобрать и напечатать с помощью pprint.
Если на вход передан некорректный JSON, программа печатает: 
'некорректный JSON'
"""

"""Sample Input:
[{"phone": "01", "name": "John"}, "2", {"phone": "033", "name": "Vasya"},
"4", {"phone": "777", "name": "Daniel"}]
Sample Output:
[{'name': 'John', 'phone': '01'},
 '2',
 {'name': 'Vasya', 'phone': '033'},
 '4',
 {'name': 'Daniel', 'phone': '777'}]
 """

import json
from json.decoder import JSONDecodeError
from pprint import pprint


input_string = input('Введите словарь в json формате \n')
try:
    dict_obj = json.loads(input_string)
    pprint(dict_obj, indent=4, sort_dicts=True)
except Exception:
    print('Некоректный json')
    exit()

