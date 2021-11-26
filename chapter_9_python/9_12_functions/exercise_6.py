"""Функция numbers_to_text принимает на вход последовательность цифр
и пробелов и возвращает строку"""



def numbers_to_text(numbers: str):
    numbers_to_text_dict = {
        '1': '.,?!:;',
        '2': 'абвг',
        '3': 'дежз',
        '4': 'ийкл',
        '5': 'мноп',
        '6': 'рсту',
        '7': 'фхцч',
        '8': 'шщъы',
        '9': 'ьэюя',
        '0': ' '
    }
    letters_list = []
    numbers_list = numbers.split()
    for element in numbers_list:
        if len(set(element)) > 1:
            return
        number_value = numbers_to_text_dict.get(element[0])
        letters_list.append(number_value[(len(element) % len(number_value) - 1)])
    return ''.join(letters_list)

input_data = input()
print(numbers_to_text(input_data))
