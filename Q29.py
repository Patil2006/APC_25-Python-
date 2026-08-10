"""29.	Store the temperature of 30 days and determine:
•	Hottest day 
•	Coldest day 
•	Average temperature 
•	Days above average temperature 
•	Days below average temperature
"""

temp = [30, 32, 29, 35, 31, 28, 33, 34, 30, 29,
        36, 32, 31, 27, 35, 33, 30, 28, 34, 32,
        31, 29, 37, 30, 33, 35, 28, 32, 34, 31]

average = sum(temp) / 30
above = 0
below = 0

for t in temp:
    if t > average:
        above += 1
    elif t < average:
        below += 1

print("Hottest day =", max(temp))
print("Coldest day =", min(temp))
print("Average temperature =", average)
print("Days above average =", above)
print("Days below average =", below)