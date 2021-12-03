import math


class Circle:
    """Окружность - можно считать площадь, диаметр, периметр."""

    def __init__(self, radius: float, name: str):
        """Инициализация окружности, radius - радиус окружности, name - имя окружности."""
        self.radius = radius
        self.name = name

    def get_area(self) -> float:
        """Вычисляет площадь круга."""
        return math.pi * self.radius**2

    def get_length(self) -> float:
        """Вычисляет длину окружности."""
        return 2 * math.pi * self.radius

    def get_diameter(self) -> float:
        """Вычисляет диаметр окружности."""
        return 2 * self.radius

first_circle = Circle(radius=10, name='окружность 1')
second_circle = Circle(radius=20, name='окружность 2')

print(f'Площадь {first_circle.name} - {first_circle.get_area()}')
print(f'Периметр {first_circle.name} - {first_circle.get_length()}')
print(f'Диаметр {first_circle.name} - {first_circle.get_diameter()}')
print(f'Площадь {second_circle.name} - {second_circle.get_area()}')
print(f'Периметр {second_circle.name} - {second_circle.get_length()}')
print(f'Диаметр {second_circle.name} - {second_circle.get_diameter()}')

