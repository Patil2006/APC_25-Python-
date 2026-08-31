# Import the required functions from salary_utils module.

from salary_utils import gross_salary, deductions, net_salary

name = input("Enter employee name: ")
basic = float(input("Enter basic salary: "))
allowance = float(input("Enter allowance: "))

gross = gross_salary(basic, allowance)
deduction = deductions(gross)
net = net_salary(gross, deduction)

print("\nEmployee Salary Details")
print("Name:", name)
print("Gross Salary:", gross)
print("Deductions:", deduction)
print("Net Salary:", net)