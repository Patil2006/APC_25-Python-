# Q13. Create a class StudentResult with student name and marks in five subjects. Use a constructor to initialize the details. Define methods to calculate total, percentage, and grade. Implement a destructor to display a suitable message.

class StudentResult:
    def __init__(self, name, m1, m2, m3, m4, m5):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
        self.m5 = m5

    def total(self):
        return self.m1 + self.m2 + self.m3 + self.m4 + self.m5

    def percentage(self):
        return self.total() / 5

    def grade(self):
        percentage = self.percentage()

        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        else:
            return "F"

    def display(self):
        print("Student Name:", self.name)
        print("Total Marks:", self.total())
        print("Percentage:", self.percentage(), "%")
        print("Grade:", self.grade())

    def __del__(self):
        print("Student result object destroyed")

student = StudentResult("Rahul", 85, 90, 78, 88, 92)

student.display()

del student