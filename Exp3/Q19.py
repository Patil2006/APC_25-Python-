#Check whether a given substring exists in the main string. 

s = input("Enter the main string: ")
sub = input("Enter the substring: ")

if sub in s:
    print("Substring exists")
else:
    print("Substring does not exist")