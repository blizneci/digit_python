from typing import Iterable


def send_mail(to: Iterable, subject: str, message: str, bcc: Iterable = None) -> None:
    """Sends email 'message' to user or users 'to' with specified 'subject'
        and optional hidden email(s) 'bcc'.

        Позиционные аргументы:
        to - строка или итер последовательность строк, список получателей
        subject - строка, тема письма
        message - строка, текст письма
        bcc - строка или итер последовательность, email для скрытой копии письма
    """

    pass
#   if type(email_list) is str:
#       print(f'email to {email_list} with subject {subject}, with message {message}\n bcc is {bcc}')
#   else:
#       for email in to:
#           print(f'email to {email} with subject {subject}, with message {message}\n bcc is {bcc}')
    
email_list = ['email@gmail.com', 'email2@gmail.com']
message_subject = 'Greeting'
message_message = 'Hello'
bcc = ['email@mail.ru', 'email2@mail.ru', 'email3@mail.ru']
send_mail(to=email_list, subject=message_subject, message=message_message,)
