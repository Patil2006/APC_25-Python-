"""
Problem Statement:
Create a base class Student with attributes roll_no, name, and course.
Derive a class Result that stores marks in three subjects and
calculates total marks, percentage, and grade.
"""

class Student:
    def __init__(self, roll_no, name, course):
        self.roll_no = roll_no
        self.name = name
        self.course = course


class Result(Student):
    def __init__(self, roll_no, name, course, m1, m2, m3):
        super().__init__(roll_no, name, course)
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def display(self):
        total = self.m1 + self.m2 + self.m3
        percentage = total / 3

        if percentage >= 75:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        elif percentage >= 40:
            grade = "D"
        else:
            grade = "F"

        print("Roll Number:", self.roll_no)
        print("Name:", self.name)
        print("Course:", self.course)
        print("Total Marks:", total)
        print("Percentage:", percentage)
        print("Grade:", grade)


r = Result(101, "Arpita", "B.Tech CSE", 80, 75, 85)

r.display()