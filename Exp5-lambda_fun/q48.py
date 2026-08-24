# Take employee records containing name and salary, sort them according to salary using lambda.

employees = [
    ("Arpita", 50000),
    ("Rahul", 35000),
    ("Sneha", 60000),
    ("Amit", 40000)
]

sorted_employees = sorted(employees, key=lambda e: e[1])

print("Employees sorted by salary:")
print(sorted_employees)