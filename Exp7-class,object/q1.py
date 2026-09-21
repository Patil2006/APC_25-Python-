# Create a class Student with attributes such as roll_no, name, and marks. Create objects for multiple students and display their details and percentage.

class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        total = sum(self.marks)
        percentage = total / len(self.marks)
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Percentage:", percentage, "%")
        print()

s1 = Student(1, "Rahul", [80, 75, 90, 85, 88])
s2 = Student(2, "Priya", [90, 85, 92, 88, 95])
s3 = Student(3, "Amit", [70, 78, 75, 80, 72])

s1.display()
s2.display()
s3.display()