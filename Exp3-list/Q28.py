"""28.	Store scores of a batsman in 10 matches and calculate:
•	Highest score 
•	Lowest score 
•	Total runs 
•	Average runs 
•	Number of centuries (≥100) 
•	Number of half-centuries (50–99)
"""

scores = [45, 72, 110, 34, 85, 102, 67, 49, 120, 56]

total = sum(scores)
average = total / 10
centuries = 0
half_centuries = 0

for s in scores:
    if s >= 100:
        centuries += 1
    elif s >= 50:
        half_centuries += 1

print("Highest score =", max(scores))
print("Lowest score =", min(scores))
print("Total runs =", total)
print("Average runs =", average)
print("Centuries =", centuries)
print("Half-centuries =", half_centuries)