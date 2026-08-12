"""24.	Rotate a list:
•	Left by one position 
•	Right by one position
"""

num = [1, 2, 3, 4, 5]

left = num[1:] + num[:1]

right = num[-1:] + num[:-1]

print("Left =", left)
print("Right =", right)