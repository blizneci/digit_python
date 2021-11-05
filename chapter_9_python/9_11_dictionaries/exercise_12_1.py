"""Глава 9.11. Словари"""

"""Принимает на вход номер телефона и стандартизирует его,
печатая в стандартизированном виде.
Формат телефона, который должен быть на выходе: 8 (9хх) ххх-хх-хх
Форматы телефонов на входе:
1. 89ххххххххх
2. 9ххххххххх - пропущена первая 7 или 8, в выходном формте первая 9
меняется на 8 (9
3. 79ххххххххх - в выходном формате первые символы 79 меняются на 8 (9
4. +79ххххххххх - в выходном формате первые символы +79 меняются
на 8 (9)
5. форматы выше с любыми нечисловыми символами внутри, например
8 9хх-ххх-хх-ххб +79хх-ххх-хххх и т.д.
Если телефон не подходит по формату ничему перечисленному, программа
выводит на печать исходный телефон, в котором оставлены только цифры.
Sample Input 1:
8 912 345 67 89
Sample Output 1:
8 (912) 345-67-89
Sample Input 2:
8 (912)345-6789
Sample Output 2:
8 (912) 345-67-89
Sample Input 3:
912)345-6789
Sample Output 3:
8 (912) 345-67-89
Sample Input 4:
7912345 67-89
Sample Output 4:
8 (912) 345-67-89
Sample Input 5:
+79123456789
Sample Output 5:
8 (912) 345-67-89
Sample Input 6:
3 45 678 90-98-76-54-32
Sample Output 6:
3456789098765432
"""

# input phone number as string.
# delete not number simbols.
# проверить длину получунного номера.
# если не соответствует российскому формату вывести просто полученный номер
# разделить на номер абонента, префикс. 
# проверить префикс на наличие 9
# выдать ошибку, если префикс не начинается с 9, завершить.
# если префикс валидный, формат валидный, то объединить номер,
# форматировать в нужном виде абонент


#input_string = input("Введите номер телефона:\n")
#phone_numbers = ''.join(element for element in input_string if element.isdigit())

#phone_numbers = ''.join(el for el in input() if el.isdigit())
phone_numbers = ''.join(filter(str.isdigit, input()))

if len(phone_numbers) < 10 or len(phone_numbers) > 11:
    print(phone_numbers)
    exit()
elif len(phone_numbers) >= 10 and int(phone_numbers[-10]) !=9:
    print(phone_numbers)
    exit()
elif len(phone_numbers) == 11 and int(phone_numbers[-11]) not in (7, 8):
    print(phone_numbers)
    exit()

prefix, number = phone_numbers[-10:-7], phone_numbers[-7:]
print(f"Форматированный номер : 8 ({prefix}) {number[0:3]}-{number[3:5]}-{number[5:]}")
