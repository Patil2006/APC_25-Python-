# 28. Create a dictionary containing names and phone numbers.
# Implement:
# • Add contact
# • Search contact
# • Update contact
# • Delete contact
# • Display all contacts

contacts = {
    "Amit": "9876543210",
    "Sneha": "8765432109",
    "Rahul": "7654321098"
}

contacts["Priya"] = "9123456780"

name = "Sneha"
if name in contacts:
    print("Contact found:", contacts[name])
else:
    print("Contact not found")

contacts["Amit"] = "9988776655"

del contacts["Rahul"]

print("All contacts:")
for name, number in contacts.items():
    print(name, ":", number)