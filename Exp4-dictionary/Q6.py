# Create a dictionary of employee IDs and names.
# Ask the user for an employee ID and check whether it exists.

employees = {
    101: "Arpita",
    102: "Rahul",
    103: "Sneha",
    104: "Amit"
}

id = int(input("Enter employee ID: "))

if id in employees:
    print("Employee ID exists")
else:
    print("Employee ID does not exist")