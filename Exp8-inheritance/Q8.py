"""
Problem Statement:
Create a base class Employee containing employee ID, name,
and basic salary. Create derived classes Manager, Developer,
and Tester. Each derived class should calculate salary differently
based on its respective allowances.
"""

class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary


class Manager(Employee):
    def salary(self):
        return self.basic_salary + 10000


class Developer(Employee):
    def salary(self):
        return self.basic_salary + 7000


class Tester(Employee):
    def salary(self):
        return self.basic_salary + 5000


m = Manager(101, "Rahul", 50000)
d = Developer(102, "Amit", 40000)
t = Tester(103, "Sneha", 35000)

print("Manager Salary:", m.salary())
print("Developer Salary:", d.salary())
print("Tester Salary:", t.salary())