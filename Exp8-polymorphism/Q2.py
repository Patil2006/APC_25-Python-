"""
Problem Statement:
Create a base class Employee with a method calculate_salary().
Derive Manager, Developer, and Tester classes.
Override the method in each class to calculate salary according
to the employee's role.
"""

class Employee:
    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary

    def calculate_salary(self):
        return self.basic_salary


class Manager(Employee):
    def calculate_salary(self):
        return self.basic_salary + 10000


class Developer(Employee):
    def calculate_salary(self):
        return self.basic_salary + 7000


class Tester(Employee):
    def calculate_salary(self):
        return self.basic_salary + 5000


employees = [
    Manager("Rahul", 50000),
    Developer("Amit", 40000),
    Tester("Sneha", 35000)
]

for employee in employees:
    print(employee.name, "Salary:", employee.calculate_salary())