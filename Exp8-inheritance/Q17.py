"""
Problem Statement:
Create a base class Animal with common attributes and methods.
Derive Dog, Cat, and Cow classes and implement their specific
sounds and behaviors.
"""

class Animal:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Animal Name:", self.name)


class Dog(Animal):
    def sound(self):
        print("Sound: Bark")

    def behavior(self):
        print("Behavior: Loyal")


class Cat(Animal):
    def sound(self):
        print("Sound: Meow")

    def behavior(self):
        print("Behavior: Playful")


class Cow(Animal):
    def sound(self):
        print("Sound: Moo")

    def behavior(self):
        print("Behavior: Calm")


d = Dog("Tommy")
c = Cat("Kitty")
w = Cow("Gauri")

d.display()
d.sound()
d.behavior()

print()

c.display()
c.sound()
c.behavior()

print()

w.display()
w.sound()
w.behavior()