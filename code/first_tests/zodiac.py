"""
Работа с аргументами командной строки, if-else.
"""

# Напиши программу, которая печатае знак задиака по переданному
# номеру месяца и дню месяца.
# Нумерация месяцев и дней месяца начинается с 1.
# Пример вызова скрипта для 10 января:
# echo "1 10" | python3 zodiac.py
# Для передачи параметров используется input()

print("Упражнение 6.1")
print("Введите месяц и день")
input_string = input()
print(f"Введенные данные: {input_string}")
month_string, day_string, *others = input_string.split()
del others
try:
    month = int(month_string)
    day = int(day_string)
    print(f"Месяц: {month} день: {day}")
except ValueError:
    print("Введена некорректная дата")

if (month == 12 and 22 < day < 31) or (month == 1 and 1 < day < 19):
    print("22.12 - 19.01: 'Capricorn', 'Козерог'")
elif (month == 1 and 20 < day < 31) or (month == 2 and 1 < day < 18):
    print("20.01 - 18.02: 'Aquarius', 'Водолей'")
elif (month == 2 and 19 < day < 29) or (month == 3 and 1 < day < 20):
    print("19.02 - 20.03: 'Pisces', 'Рыбы'")
elif (month == 3 and 21 < day < 31) or (month == 4 and 1 < day < 19):
    print("21.03 - 19.04: 'Aries', 'Овен'")
elif (month == 4 and 20 < day < 30) or (month == 5 and 1 < day < 20):
    print("20.04 - 20.05: 'Taurus', 'Телец'")
elif (month == 5 and 21 < day < 31) or (month == 6 and 1 < day < 20):
    print("21.05 - 20.06: 'Gemini', 'Близнецы'")
elif (month == 6 and 21 < day < 30) or (month == 7 and 1 < day < 22):
    print("21.06 - 22.07: 'Cancer', 'Рак'")
elif (month == 7 and 23 < day < 31) or (month == 8 and 1 < day < 22):
    print("23.07 - 22.08: 'Leo', 'Лев'")
elif (month == 8 and 23 < day < 31) or (month == 9 and 1 < day < 22):
    print("23.08 - 22.09: 'Virgo', 'Дева'")
elif (month == 9 and 23 < day < 30) or (month == 10 and 1 < day < 22):
    print("23.09 - 22.10: 'Libra', 'Весы'")
elif (month == 10 and 23 < day < 31) or (month == 11 and 1 < day < 21):
    print("23.10 - 21.11: 'Scorpio', 'Скорпион'")
elif (month == 11 and 22 < day < 30) or (month == 12 and 1 < day < 21):
    print("22.11 - 21.12: 'Sagittarius', 'Стрелец'")
else:
    print("Введена некорректная дата")
