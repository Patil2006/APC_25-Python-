"""11.Create a list of 10 numbers and display:
•	First 5 elements 
•	Last 5 elements 
•	Middle 4 elements 
•	Alternate elements 
•	Reverse list using slicing"""

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("First 5 =", num[:5])
print("Last 5 =", num[-5:])
print("Middle 4 =", num[3:7])
print("Alternate =", num[::2])
print("Reverse =", num[::-1])