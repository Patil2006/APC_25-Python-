"""
Problem Statement:
Create classes Camera and Phone.
The Camera class should provide methods for taking photographs,
while Phone should provide methods for making calls.
Create a Smartphone class inheriting from both.
"""

class Camera:
    def take_photo(self):
        print("Taking photograph...")


class Phone:
    def make_call(self):
        print("Making phone call...")


class Smartphone(Camera, Phone):
    def display(self):
        print("Smartphone")


s = Smartphone()

s.display()
s.take_photo()
s.make_call()