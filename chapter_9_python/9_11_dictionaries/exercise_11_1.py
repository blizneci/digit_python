"""Глава 9.11. Словари"""

"""Программа принимает на вход словарь в JSON формате. Если в словаре
есть ключ special_key, удали его и выведи на печать получившийся словарь,
если нет - просто выведи исходный словарь. Для форматирования словаря
при печати используй json.dumps.
Sample Input:
{"key1": 1, "key2": 11, "key3": 11000, "key4": 50}
Sample Output:
{"key1": 1, "key2": 11, "key3": 11000, "key4": 50}
"""

import json
import time

input_dict = json.loads(input())
start = time.time()
#if 'special_key' in input_dict:
#    del input_dict['special_key']
input_dict.pop('special_key', print("special_key is not found"))
print(json.dumps(input_dict))
end = time.time()
print("Elapsed time: ", end - start)
