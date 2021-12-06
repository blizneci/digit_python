import random
import string

class User():
    """Создает пользователя."""
    def __init__(self, name: str, age: int):
        """Иницализация пользователя с именем name и возрастом age."""
        self.name = name
        self.age = age

    def is_adult(self) -> bool:
        """Проверяет, является ли пользователь совершеннолетним"""
        return self.age >= 18

    @staticmethod
    def generate_password(length: int) -> str:
        """Генерирует пароль с переданной длиной length."""
        return ''.join(random.sample(string.ascii_letters + string.digits, length))

    def get_name(self) -> str:
        """Возвращает имя пользователя."""
        return self.name

user = User('John', 19)
if user.is_adult():
    print(f'Пользователь {user.name} совершеннолетний')
else:
    print(f'Пользователь {user.name} несовершеннолетний')

password = user.generate_password(15)
print(password)