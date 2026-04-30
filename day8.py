'''
User input
----------


SBI_PIN = input("Enter the pin:")
if len(SBI_PIN) == 4:
    print("welcome")

int datatype
------------

any = int(input("enter a number:"))
print(type(any))

string datatype
---------------

an = input("Enter the word:")
print(type(an))

passing two values
------------------
a,b = map(int,input("Enter two numbers: ").split())
print(a)
print(type(a))
print(b)
print(type(b))

list datatype
-------------

CV = list(map(int,input("Enter the number: ").split()))
print(CV)
print(type(CV))

Tuple datatype
--------------

CV = tuple(map(int,input("Enter the number: ").split()))
print(CV)
print(type(CV))

A = 34
B = 23
print("Added A and B and the result is",A+B)
print(f"A + B = {A+B}")
print("A + B", A+B)


if statement
------------
this is used to check the condition is true or not
AN = 9
if AN >= 9:
    print(f"AN is greater than {9}")

else statement
--------------
-->else is fall-back statement, incase if statement becomes false, it will enter into else

ANY = 9
if ANY >= 9:
    print(f"ANY is greater than {9}")
else:
    print(f"ANY is not greater than {9}")

num = 10
if num >=11:
    print(f"{num} is greater than {11}")
else:
    print(f"{num} is lesser than {11}")
eval()
-----
v = eval(input("Enter:"))
print(type(v))
print(v)
b = eval(input("Enter:"))
print(type(b))
print(b)

num = 7
num_2 = 56
if num > num_2:
    print(f"{num} is greater than {num_2}")
else:
    print(f"{num_2} is greater than {num}")


age = int(input("Enter your age:"))
if age >=18:
    print("You are eligible to vote:")
else:
    print(f"You have to wait {18 - age} more years")


marks = int(input("enter your marks:"))
if marks >= 35:
    print("Pass")
else:
    print("Fail")
'''








