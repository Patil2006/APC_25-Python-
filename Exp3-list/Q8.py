"""8.Store 15 integers in a list. Count how many numbers are:
•	Even 
•	Odd"""

num=[21,12,23,34,56,65,76,87,89,90,25,35,57,95,52]
Even=0
Odd=0
for n in num:
    if n%2==0:
        Even+=1
    else:
        Odd+=1
print("Even",Even) 
print("Odd",Odd)                                                                                                                                                                                                                                                                                                                                                                                           