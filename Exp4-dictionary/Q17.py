# Given two dictionaries, find the keys that are common to both dictionaries.

dict1 = {"Name": "Arpita", "Age": 20, "Marks": 85}
dict2 = {"Name": "Rahul", "Age": 21, "Department": "CSE"}

common = dict1.keys() & dict2.keys()

print("Common keys:", common)