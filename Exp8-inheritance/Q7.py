"""
Problem Statement:
Create a base class Shape containing a method to display the name
of the shape. Create three derived classes Circle, Rectangle,
and Triangle. Each class should implement its own method
to calculate the area.
"""

class Shape:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Shape:", self.name)


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


c = Circle(5)
r = Rectangle(10, 5)
t = Triangle(8, 6)

c.display()
print("Area:", c.area())

r.display()
print("Area:", r.area())

t.display()
print("Area:", t.area())