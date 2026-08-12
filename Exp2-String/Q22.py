#Run-Length Encoding

s = input("Enter a string: ")

count = 1

for i in range(len(s)):
    if i < len(s) - 1 and s[i] == s[i + 1]:
        count += 1
    else:
        print(s[i] + str(count), end="")
        count = 1