"""
Напиши функцию is_password_hard, которая принимает на вход пароль
и возвращает True, если он надежный или False в противном случае.
Надежный пароль - длина больше 12 символов, содержит хотя бы
1 букву в большом регистре, хотя бы 1 букву в маленьком регистре
и хотя бы одну цифру.
Sample Input:
password
Sample Output:
пароль ненадежный
"""

def is_password_hard(password):
    HARD_PASSWORD_FLAG = False
    UPPER_LETTER_FLAG = False
    LOWER_LETTER_FLAG = False
    NUMBER_FLAG = False

    if len(password) < 12:
        return HARD_PASSWORD_FLAG

    for i in password:
        if i.isupper():
            UPPER_LETTER_FLAG = True
        if i.islower():
            LOWER_LETTER_FLAG = True
        if i.isnumeric():
            NUMBER_FLAG = True
    
    HARD_PASSWORD_FLAG = UPPER_LETTER_FLAG and LOWER_LETTER_FLAG and NUMBER_FLAG
    return HARD_PASSWORD_FLAG

while True:
    password = input("Введите пароль, q для выхода:")
    if password == 'q':
        break
    print('пароль надежный') if is_password_hard(password) else print('пароль ненадежный')
#   if is_password_hard(password):
#       print('пароль надежный')
#   else:
#       print('пароль не недежный')

