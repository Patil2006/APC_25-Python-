a=int(input("enter a 1st no."))
b=int(input("enter 2nd no."))
c=int(input("enter 3rd no."))
if a>b and a>c:
    print(a,"is largest")
elif b>c:
    print(b,"is largest")
else:
    print(c,"is largest")