# 17. Take marks of 20 students, calculate the class average
# and display the marks of students who scored above the average.

import numpy as np

marks = np.array([65, 78, 45, 89, 56, 72, 91, 63, 84, 50,
                  76, 68, 95, 55, 81, 70, 42, 88, 74, 60])

average = np.mean(marks)

print("Marks of 20 Students:")
print(marks)

print("\nClass Average:", average)

print("\nStudents who scored above average:")
print(marks[marks > average])