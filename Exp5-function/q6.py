# 6. Define a function to calculate the area of a circle using its radius.

def circle_area(r):
    return 3.14 * r * r

r = float(input("Enter radius: "))
print("Area of circle =", circle_area(r))