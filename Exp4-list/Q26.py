"""26.	Store marks of 20 students in a list and determine:
•	Highest marks 
•	Lowest marks 
•	Average marks 
•	Number of students scoring above average 
•	Number of students scoring below average
"""

marks = [78, 65, 90, 55, 88, 72, 95, 60, 84, 76,
         69, 92, 58, 81, 73, 67, 89, 50, 85, 71]

average = sum(marks) / 20

above = 0
below = 0

for m in marks:
    if m > average:
        above += 1
    elif m < average:
        below += 1

print("Highest marks =", max(marks))
print("Lowest marks =", min(marks))
print("Average marks =", average)
print("Above average =", above)
print("Below average =", below)