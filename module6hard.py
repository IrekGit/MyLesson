import math

class Figure:
    name = 'Загадочные фигуры...'
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = list(color) if self.__is_valid_color(*color) else [0, 0, 0]
        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = list(sides) if self.__is_valid_sides(*sides) else [1] * self.sides_count
        self.filled = False

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count and self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def __len__(self):
        return sum(self.__sides)

    def __is_valid_color(self, r, g, b):
        return all(isinstance(c, int) and 0 <= c <= 255 for c in (r, g, b))

    def __is_valid_sides(self, *sides):
        return all(isinstance(s, int) and s > 0 for s in sides)


class Circle(Figure):
    name = 'Круг'
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    name = 'Треугольник'
    sides_count = 3

    def get_square(self):
        a, b, c = self.get_sides()
        s = sum(self.get_sides()) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Cube(Figure):
    name = 'Куб'
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1:
            sides = [sides[0]] * self.sides_count
        super().__init__(color, *sides)

    def get_volume(self):
        edge = self.get_sides()[0]
        return edge ** 3


circle1 = Circle((200, 200, 100), 10)
print(f'Фигура: {circle1.name}, цвет: {circle1.get_color()}, длина окружности {len(circle1)}')

cube1 = Cube((222, 35, 130), 6)
print(f'Фигура: {cube1.name}, цвет: {cube1.get_color()}, длина ребра {cube1.get_sides()[0]}')

circle1.set_color(55, 66, 77)
print(f'Фигура: {circle1.name}, цвет: {circle1.get_color()}')

cube1.set_color(300, 70, 15)
print(f'Фигура: {cube1.name}, цвет: {cube1.get_color()}')

cube1.set_sides(5, 3, 12, 4, 5)
print(f'Фигура: {cube1.name}, длины {cube1.sides_count} сторон: {cube1.get_sides()}, объем: {cube1.get_volume()}')

circle1.set_sides(15)
print(f'Фигура: {circle1.name}, измененная длина окружности: {circle1.get_sides()}')
print(f'Фигура: {circle1.name}, длина окружности: {len(circle1)}, площадь: {circle1.get_square()}')