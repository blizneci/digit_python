"""
Для использования в гугл-таблицах указывать delimiter=';' не нужно.
Указание delimiter=';' нужно при работе с файлом в Excel.
"""
import csv


with open('/mnt/d/edu_projects/digit_python/chapter_9_python/users.csv',
          'w', encoding='cp1251') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(['Алексей', 'user1@mail.ru'])
    writer.writerow(['John', 'user2@gmail.com'])
    writer.writerow(['Tom', 'user3@mail.ru'])

