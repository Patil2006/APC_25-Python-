# Create a module containing functions to calculate gross salary, deductions, and net salary.

def gross_salary(basic_salary, allowance):
    return basic_salary + allowance

def deductions(gross):
    return gross * 0.10

def net_salary(gross, deduction):
    return gross - deduction