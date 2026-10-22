runs = (45, 72, 18, 95, 63, 81, 37, 54, 88, 29)

total = sum(runs)
highest = runs[0]
lowest = runs[0]

for run in runs:
    if run > highest:
        highest = run
    if run < lowest:
        lowest = run

average = total / len(runs)

print("Runs:", runs)
print("Total runs:", total)
print("Highest score:", highest)
print("Lowest score:", lowest)
print("Average score:", average)