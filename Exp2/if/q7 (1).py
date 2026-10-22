a=int(input("enter a 1st no."))
b=int(input("enter 2nd no."))
c=int(input("enter 3rd no."))
if a<b and a<c:
    print(a,"is smallest")
elif b<c:
    print(b,"is smallest")
else:
    print(c,"is smallest")