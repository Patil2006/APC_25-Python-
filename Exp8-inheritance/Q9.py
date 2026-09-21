"""
Problem Statement:
Create a class Person.
Derive Student and Faculty from Person.
Create another class TeachingAssistant that inherits from both
Student and Faculty. Display the details and demonstrate the use
of multiple and hierarchical inheritance together.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def student_details(self, roll_no, course):
        self.roll_no = roll_no
        self.course = course


class Faculty(Person):
    def faculty_details(self, subject):
        self.subject = subject


class TeachingAssistant(Student, Faculty):
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll Number:", self.roll_no)
        print("Course:", self.course)
        print("Subject:", self.subject)


ta = TeachingAssistant("Arpita", 20)

ta.student_details(101, "B.Tech CSE")
ta.faculty_details("Python")

ta.display()