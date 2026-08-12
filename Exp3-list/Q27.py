"""27.	Store salaries of employees and determine:
•	Highest salary 
•	Lowest salary 
•	Average salary 
•	Employees earning above ₹50,000 
•	Employees earning below ₹30,000 
"""

salary = [25000, 35000, 45000, 55000, 60000, 28000, 75000, 30000, 50000, 65000]

average = sum(salary) / len(salary)

above_50k = 0
below_30k = 0

for s in salary:
    if s > 50000:
        above_50k += 1
    if s < 30000:
        below_30k += 1

print("Highest salary =", max(salary))
print("Lowest salary =", min(salary))
print("Average salary =", average)
print("Above ₹50,000 =", above_50k)
print("Below ₹30,000 =", below_30k)