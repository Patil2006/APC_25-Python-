# Q14. Create an array and insert elements.

from array import array

a = array('i', [10, 20, 30])

a.append(40)
a.insert(1, 15)

print("Array:", a)