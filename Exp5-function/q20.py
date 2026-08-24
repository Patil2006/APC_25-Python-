# 20. Write a function that accepts basic salary and calculates gross salary after adding HRA and DA.

def gross_salary(basic_salary):
    hra = basic_salary * 0.20
    da = basic_salary * 0.10
    gross = basic_salary + hra + da
    return gross

basic_salary = float(input("Enter basic salary: "))

print("Gross Salary =", gross_salary(basic_salary))