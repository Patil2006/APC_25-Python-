"""
Problem Statement:
Create a base class Animal with a method sound().
Create subclasses Dog, Cat, Cow, and Lion.
Override sound() in each class to display the appropriate sound.
"""

class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog: Bark")


class Cat(Animal):
    def sound(self):
        print("Cat: Meow")


class Cow(Animal):
    def sound(self):
        print("Cow: Moo")


class Lion(Animal):
    def sound(self):
        print("Lion: Roar")


animals = [
    Dog(),
    Cat(),
    Cow(),
    Lion()
]

for animal in animals:
    animal.sound()