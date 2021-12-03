import random
import string

class User():
    """docstring"""
    def __init__(self, name: str, age: int):
        """docstring"""
        self.name = name
        self.age = age

    def is_adult(self) -> bool:
        """docstring"""
        return self.age >= 18

    @staticmethod
    def generate_password(length: int) -> str:
        """docstring"""
        return ''.join(random.sample(string.ascii_letters + string.digits, length))

    def get_name(self) -> str:
        return self.name

user = User('John', 19)
if user.is_adult():
    print(f'Пользователь {user.name} совершеннолетний')
else:
    print(f'Пользователь {user.name} несовершеннолетний')

password = user.generate_password(15)
print(password)
