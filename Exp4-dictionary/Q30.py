# 30. Take a dictionary containing student names and their departments;
# create a new dictionary that groups students according to their department.

students = {
    "Amit": "CSE",
    "Sneha": "IT",
    "Rahul": "CSE",
    "Priya": "ENTC",
    "Neha": "IT"
}

departments = {}

for name, department in students.items():
    if department not in departments:
        departments[department] = []
    departments[department].append(name)

print("Students grouped by department:")
print(departments)