"""
Функции можно приравнивать переменным.
функция make_some_stuff определена выше твоего кода (для тестирования на stepik),
принимающая один позициооный строковый аргумент.
Создать переменную new_function, ее значением должна быть эта функция.
Печатать или вызвать функцию не нужно, функция будет вызвана кодом проверки."""

def make_some_stuff(something):
    print(f"make_some_stuff print {something}")

new_function = make_some_stuff

new_function("some cool data")
