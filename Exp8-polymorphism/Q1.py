"""
Problem Statement:
Create a base class Shape with a method area().
Derive Circle, Rectangle, and Triangle classes and override
the area() method in each class.
Create objects of each class and demonstrate runtime polymorphism.
"""

class Shape:
    def area(self):
        print("Area of shape")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shapes = [
    Circle(5),
    Rectangle(10, 5),
    Triangle(8, 6)
]

for shape in shapes:
    print("Area:", shape.area())