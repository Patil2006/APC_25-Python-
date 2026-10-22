#Compress repeated characters and return the original string if compression does not reduce the length. 

s = input("Enter a string: ")

result = ""
count = 1

for i in range(len(s)):
    if i < len(s) - 1 and s[i] == s[i + 1]:
        count += 1
    else:
        result += s[i] + str(count)
        count = 1

if len(result) < len(s):
    print(result)
else:
    print(s)