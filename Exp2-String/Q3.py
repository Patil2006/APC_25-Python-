#3.Reverse a String 

s = input("Enter a string: ")
rev = ""
for i in s:
    rev = i + rev

print("Reversed String =", rev)