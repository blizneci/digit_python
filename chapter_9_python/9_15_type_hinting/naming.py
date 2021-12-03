def is_person_retiree(age: int, sex: str) -> bool:
    """Возвращает True, если человек пенсионер, False в противном случае.
    age - возраст (лет), sex - пол (f для женского пола или m для мужского)."""
    if sex == 'f':
        return age >= 56.5
    elif sex == 'm':
        return age >= 61.5

print(is_person_retiree(age=62, sex='m'))
