temperatures = (32, 35, 31, 36, 34, 33, 37)

maximum = temperatures[0]
minimum = temperatures[0]

for temp in temperatures:
    if temp > maximum:
        maximum = temp
    if temp < minimum:
        minimum = temp

average = sum(temperatures) / len(temperatures)

print("Temperatures:", temperatures)
print("Maximum temperature:", maximum)
print("Minimum temperature:", minimum)
print("Average temperature:", average)