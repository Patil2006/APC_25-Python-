"""
Problem Statement:
Create two classes Academic and Sports.
Academic stores marks obtained by a student.
Sports stores sports points.
Create a Student class that inherits from both classes
and calculates the student's overall performance.
"""

class Academic:
    def __init__(self, marks):
        self.marks = marks


class Sports:
    def __init__(self, points):
        self.points = points


class Student(Academic, Sports):
    def __init__(self, marks, points):
        Academic.__init__(self, marks)
        Sports.__init__(self, points)

    def performance(self):
        total = self.marks + self.points
        print("Academic Marks:", self.marks)
        print("Sports Points:", self.points)
        print("Overall Performance:", total)


s = Student(80, 15)

s.performance()