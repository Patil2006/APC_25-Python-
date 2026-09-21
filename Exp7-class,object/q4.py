# Q4. Create a class Circle with an attribute radius. Define methods to calculate the area and circumference of the circle.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def circumference(self):
        return 2 * math.pi * self.radius

c = Circle(5)

print("Radius:", c.radius)
print("Area:", c.area())
print("Circumference:", c.circumference())