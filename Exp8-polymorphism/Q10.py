"""
Problem Statement:
Create a class Student containing the student's name and total marks.
Overload the > and < operators to compare the marks of two students.
"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks

    def __lt__(self, other):
        return self.marks < other.marks


s1 = Student("Arpita", 85)
s2 = Student("Rahul", 75)

if s1 > s2:
    print(s1.name, "has higher marks")

if s1 < s2:
    print(s1.name, "has lower marks")