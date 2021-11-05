"""
Функция принимает один аргумен и вызывает функцию say_my_name
внутри себя, выводит на печать результат этой функции.
"""

def say_my_name(name):
    return f"Hi, {name}"

def run(name=None):
    print(say_my_name(name))

run('Kirill')