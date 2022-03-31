# Original Code:

# class Rectangle:
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
# class AreaCalculator:
#
#     def __init__(self, shapes):
#
#         assert isinstance(shapes, list), "`shapes` should be of type `list`."
#         self.shapes = shapes
#
#     @property
#     def total_area(self):
#         total = 0
#         for shape in self.shapes:
#             total += shape.width * shape.height
#
#         return total
#
#
# shapes = [Rectangle(2, 3), Rectangle(1, 6)]
# calculator = AreaCalculator(shapes)
# print("The total area is: ", calculator.total_area)


# Refactored Code:

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return (self.height * self.width) / 2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return pi * (self.radius ** 2)


class TotalAreaCalculator:
    def __init__(self, list_of_shapes):
        assert isinstance(list_of_shapes, list), "`shapes` should be of type `list`."
        self.list_of_shapes = list_of_shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.list_of_shapes:
            total += shape.calculate_area()

        return total


shapes = [Rectangle(2, 3)]
calculator = TotalAreaCalculator(shapes)
print("The total area is: ", calculator.total_area)

shapes = [Rectangle(1, 6), Triangle(2, 3), Circle(3)]
calculator = TotalAreaCalculator(shapes)
print(f"The total area is: {calculator.total_area}")