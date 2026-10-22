# 26. Create a dictionary containing employee names and salaries. Find:
# • Highest salary
# • Lowest salary
# • Average salary
# • Employees earning more than ₹50,000

employees = {
    "Amit": 45000,
    "Sneha": 60000,
    "Rahul": 75000,
    "Priya": 50000,
    "Neha": 55000
}

highest = max(employees.values())
lowest = min(employees.values())
average = sum(employees.values()) / len(employees)

print("Highest salary:", highest)
print("Lowest salary:", lowest)
print("Average salary:", average)

print("Employees earning more than ₹50,000:")
for name, salary in employees.items():
    if salary > 50000:
        print(name, ":", salary)