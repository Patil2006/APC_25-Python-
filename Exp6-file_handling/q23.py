# Q23. Compare two text files and find the first line where they differ
file1 =open("file1.txt","w")
file1.write("New file1\n")
file2 =open("file2.txt","w")
file2.write("New file2\n")

file1 = open("file1.txt", "r")
file2 = open("file2.txt", "r")

lines1 = file1.readlines()
lines2 = file2.readlines()

file1.close()
file2.close()

if lines1 == lines2:
    print("Both files have identical contents.")
else:
    print("Files are different.")

    minimum = min(len(lines1), len(lines2))

    for i in range(minimum):
        if lines1[i] != lines2[i]:
            print("First difference is at line:", i + 1)
            print("File 1:", lines1[i].strip())
            print("File 2:", lines2[i].strip())
            break
    else:
        print("Difference is due to different number of lines.")