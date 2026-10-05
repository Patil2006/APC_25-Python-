import numpy as np

marks = np.array([
    [[80, 75, 90], [85, 78, 88]],
    [[70, 82, 76], [92, 89, 95]]
])

print("3D Array:")
print(marks)

print("First student's first subject mark:", marks[0, 0, 0])
print("Second student's second subject mark:", marks[1, 1, 1])
print("Selected elements:")
print(marks[0, :, 1])