"""
Problem Statement:
Create a base class Student with a method calculate_grade().
Derive EngineeringStudent, MedicalStudent, and ManagementStudent.
Override the method according to different grading criteria.
"""

class Student:
    def calculate_grade(self, marks):
        return "Grade not defined"


class EngineeringStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 75:
            return "A"
        elif marks >= 60:
            return "B"
        elif marks >= 50:
            return "C"
        else:
            return "F"


class MedicalStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 80:
            return "A"
        elif marks >= 65:
            return "B"
        elif marks >= 50:
            return "C"
        else:
            return "F"


class ManagementStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 70:
            return "A"
        elif marks >= 60:
            return "B"
        elif marks >= 50:
            return "C"
        else:
            return "F"


students = [
    EngineeringStudent(),
    MedicalStudent(),
    ManagementStudent()
]

marks = [70, 85, 65]

for student, mark in zip(students, marks):
    print("Marks:", mark, "Grade:", student.calculate_grade(mark))