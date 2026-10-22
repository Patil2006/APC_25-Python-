"""30.	Store patient names and ages using lists.
Perform:
•	Add a patient 
•	Delete a patient 
•	Search a patient 
•	Display all patients 
•	Count total patients
"""

names = ["Amit", "Rahul", "Sneha"]
ages = [25, 30, 22]

names.append("Priya")
ages.append(28)

name = input("Enter patient to delete: ")

if name in names:
    i = names.index(name)
    names.pop(i)
    ages.pop(i)

name = input("Enter patient to search: ")

if name in names:
    i = names.index(name)
    print("Patient found:", name, "Age =", ages[i])
else:
    print("Patient not found")

print("All patients:")
for i in range(len(names)):
    print(names[i], ages[i])

print("Total patients =", len(names))