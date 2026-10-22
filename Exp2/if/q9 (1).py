n=int(input("enter a year:"))
if (n%4==0) and (n%100==0)& (n%400==0):
    print("leap year")
else:
    print("non leap year")