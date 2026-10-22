# Take employee records containing name, department, and salary, use filter(), map(), and sorted() with lambda functions to:
# a) Find employees earning more than ₹50,000.
# b) Increase salaries by 10%.
# c) Sort employees according to salary.

employees = [
    ("Arpita", "CSE", 60000),
    ("Rahul", "IT", 45000),
    ("Sneha", "CSE", 55000),
    ("Amit", "HR", 40000)
]

high_salary = list(filter(lambda e: e[2] > 50000, employees))

increased_salary = list(map(lambda e: (e[0], e[1], e[2] * 1.10), employees))

sorted_employees = sorted(employees, key=lambda e: e[2])

print("Employees earning more than ₹50,000:")
print(high_salary)

print("Salaries after 10% increase:")
print(increased_salary)

print("Employees sorted according to salary:")
print(sorted_employees)