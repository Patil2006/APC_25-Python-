# Q18. Employee records: display, highest salary, average salary and above given salary

def display_employees(employees):
    print("\nAll Employees:")
    for emp in employees:
        print(emp)


def highest_paid(employees):
    employee = max(employees, key=lambda x: x[3])
    print("\nHighest Paid Employee:")
    print(employee)


def average_salary(employees):
    average = sum(emp[3] for emp in employees) / len(employees)
    print("\nAverage Salary:", average)


def above_salary(employees, salary):
    print("\nEmployees earning above", salary)

    for emp in employees:
        if emp[3] > salary:
            print(emp)


file = open("employees.txt", "w")

file.write("101,Amit,IT,50000\n")
file.write("102,Priya,HR,60000\n")
file.write("103,Rahul,Finance,45000\n")

file.close()

file = open("employees.txt", "r")

employees = []

for line in file:
    emp_id, name, department, salary = line.strip().split(",")
    employees.append((emp_id, name, department, float(salary)))

file.close()

display_employees(employees)
highest_paid(employees)
average_salary(employees)

salary = float(input("\nEnter salary limit: "))

above_salary(employees, salary)