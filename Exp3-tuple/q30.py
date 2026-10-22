patients = (
    (101, "Amit", 25, "A+"),
    (102, "Sneha", 30, "B+"),
    (103, "Rahul", 22, "O+"),
    (104, "Priya", 28, "A+"),
    (105, "Neha", 35, "B+")
)

print("All Patient Records:")
for patient in patients:
    print(patient)

search_id = int(input("\nEnter Patient ID to search: "))

found = False
for patient in patients:
    if patient[0] == search_id:
        print("Patient Found:", patient)
        found = True
        break

if not found:
    print("Patient not found.")

print("\nTotal number of patients:", len(patients))

blood_group = input("\nEnter blood group to search: ")

print("Patients with blood group", blood_group, ":")
found = False

for patient in patients:
    if patient[3] == blood_group:
        print(patient)
        found = True

if not found:
    print("No patient found with this blood group.")