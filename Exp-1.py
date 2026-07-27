Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import keyword
print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

#DataTypes:
#1)String
x="Hello"
type(x)
<class 'str'>
#2) Integer
x=100
type(x)
<class 'int'>
#3)Float:
x=1.2
type(x)
<class 'float'>
#4) Complex:
x=aj
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    x=aj
NameError: name 'aj' is not defined
x=1j
type(x)
<class 'complex'>
#5) List
x=["Apple","Banana"]
type(x)
<class 'list'>
#6) Tuple
x=("Mango","Kiwi")
type(x)
<class 'tuple'>
x=range(6)
type(x)
<class 'range'>
x={"name" : "John" ,"age":36}
type(x)
<class 'dict'>
x={"Apple","Banana"}
type(x)
<class 'set'>
x=frozenset({"Apple","Banana"})
type(x)
<class 'frozenset'>
x=True
type(x)
<class 'bool'>
x=b"Hello"
type(x)
<class 'bytes'>
x=bytearray(5)
type(x)
<class 'bytearray'>
x= memoryview(bytes(5))
type(x)
<class 'memoryview'>
x=None
type(x)
<class 'NoneType'>



#List and Tuple are Mutable and immutable
x=[10,20,30,40]
x.append(50,60)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    x.append(50,60)
TypeError: list.append() takes exactly one argument (2 given)
x.append(60)
print(x)
[10, 20, 30, 40, 60]
x=(10,20,30)
x.append(40)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    x.append(40)
AttributeError: 'tuple' object has no attribute 'append'
print(x)
(10, 20, 30)


#List and Tuple is order or not:
x=[10,20,30]
print(x[2])
30
x=(10,20,30,40)
print(x[2])
30

x=["Ram","Sham","Sam"]
x[2]
'Sam'
x="Ram","Sham","Sam"]
SyntaxError: unmatched ']'
x=("Ram","Sham","Sam","Shravani")
x[3]
'Shravani'
x={"Ram","Sham","Sam","Shravani"}
x[2]
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    x[2]
TypeError: 'set' object is not subscriptable
x={"name" : "John" ,"age":36}
x[1]
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    x[1]
KeyError: 1


#Operators
x=10
y=20
z=x+y
print(z)
30
#ii)Substraction
x=30
y=20
z=x-y
print(z)
SyntaxError: multiple statements found while compiling a single statement
SyntaxError: multiple statements found while compiling a single statement
SyntaxError: invalid syntax
x=30
y=29
z=x-y
print(z)
1
#iii)Mul
x=30
y=67
z=x*y
print(z)
2010
#Div
x=20
y=10
z=x/y
print(z)
2.0
#Modulus
x=30
y=9
z=x%y
print(z)
3
#Exponential
x=3
y=4
z=x**y
print(z)
81
#Floor divison
x=90
y=18
z=x//y
print(z)
5

#2)Assignment Operator
#Equal to
x=16
print(x)
16
#+=
x=16
x+=5
print(x)
21
#-=
x=16
x-=5
print(x)
11
#*=
x=20
x*=6
print(x)
120
#/=
x=21
x/=3
print(x)
7.0
#&=
x=14
x&=3
print(x)
2
#!=
x=12
x!=4
True
x=12
x^=5
print(x)
9
#>>=
x=16
x>>=3
print(x)
2
x=4
print(:=5)
SyntaxError: invalid syntax
#%=
x=45
x%=3
print(x)
0
#//=
x=34
x//=7
print(x)
4
#**=
x=4
x**=5
print(x)
1024


#Comparison Opeartor
x=3
y=3
z=x==y
print(z)
True
x=3
y=3
z=x!=y
print(z)
SyntaxError: multiple statements found while compiling a single statement
x=4
y=5
z=x!=y
print(z)
SyntaxError: multiple statements found while compiling a single statement
x=4
y=10
z=x!=y
print(z)
True
x=10
y=5
z=x>y
print(z)
True
x=12
y=11
z=x<y
print(z)
False
x=10
y=10
z=x>=y
print(z)
True
x=10
y=12
z=x<=y
print(z)
True


#Logical Operators
KeyboardInterrupt
age = 20
has_id = True

print(age >= 18 and has_id)
SyntaxError: multiple statements found while compiling a single statement
age = 20
has_id = True
print(age>= 18 and has_id)
True
is_sunday = False
is_monday = True
print(is_sunday or is_monday)
True
is_raining = False
print(not is_raining)
True
a=[10,20,30]
b=a
print(a is b)
True
a=[10,20,30]
b=a
print(a is not b)
False


#Membership Operator
fruits=["Apple" ,"Mango","Banana"]
print("Mango" in fruits)
True
fruits =["Apple","Mango","Banana"]
print("Mango" not in fruits)
False

#Bitwise Operator
x=10
y=10
z=x&y
print(z)
10
x=1
y=1
print(x|y)
1
x=10
y=10
print(x^y)
0
x=10
print(~x)
-11
x=10
print(x>>)
SyntaxError: invalid syntax
x=10
print(x>>1)
5
x=12
print(x<<1)
24
x=10
y=10
print(x&y)
10


#if statement
num=int(input("Enter the number:"))
Enter the number:10
if num%2==0:
    print("Number is Even)
          
SyntaxError: unterminated string literal (detected at line 2)
print("Number is Even")
          
Number is Even
num=input(("Enter the number:"))
          
Enter the number:10
if num%2==0:
          print("Number is even")

          
Traceback (most recent call last):
  File "<pyshell#246>", line 1, in <module>
    if num%2==0:
TypeError: not all arguments converted during string formatting
>>> x=10
...           
>>> if x%2==0
...           
SyntaxError: expected ':'
>>> x=10
...           
>>> if x%2==0:
...           print("Even number")
... 
...           
Even number
>>> #if-else:
...           
>>> x=10
...           
>>> if x>18:
...           print("You are eligible")
... else:
...     print("You are not Eligible")
... 
...     
You are not Eligible
>>> #elif statement
>>> x=80
>>> if(x>=80):
...     print("Excellent")
... elif:
...     
SyntaxError: invalid syntax
>>> x=90
>>> if x>=90:
...     print("Excellent")
... elif x>=70:
...     print("Average")
... elif x>=60:
...     print("Good")
... else:
...     printf("Need to Improvement")
... 
...     
Excellent
