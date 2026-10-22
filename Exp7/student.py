# Implementation of class, object, constructor and destructor.

class Student:

    def __init__(self, name, roll_no, branch):
        self.name = name
        self.roll_no = roll_no
        self.branch = branch
        print("Constructor called")

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Branch:", self.branch)

    def __del__(self):
        print("Destructor called")


student1 = Student("Arpita", 101, "CSE")

student1.display()

del student1