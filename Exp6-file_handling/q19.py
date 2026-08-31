# Q19. Calculate attendance percentage and display students below 75%

file = open("attendance.txt", "w")

file.write("101,Amit,70,100\n")
file.write("102,Priya,85,100\n")
file.write("103,Rahul,60,100\n")

file.close()

file = open("attendance.txt", "r")

print("Attendance Details:\n")

for line in file:
    roll, name, present, total = line.strip().split(",")

    present = int(present)
    total = int(total)

    percentage = (present / total) * 100

    print(name, ":", percentage, "%")

    if percentage < 75:
        print("Below 75%")

file.close()