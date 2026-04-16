
'''variables
----------
To define a variable, we have 2 rules
1.Good way to define a variable(No error)
2.Bad way to define a variable (will get error)'''

A = 90
print(A)

_v = 90
print(_v)


num = 90

'''Note:-
-->We are going to use meaningful words or name for defining variables'''
num = 90
num_2= 60

'''Keywords
-------
-->This keywords not gonna use as a variable
-->Identifiers are nothing but keywords
-->Ex:-if,for,while'''

a, b, c = 23, 56, 78
print(a)
print(b)
print(c)
print(a+b)
print(f"\n{a}, \n{b} ,\n{c}")

'''Tokens
--------
-->Nothing but a small program or code in python to complete the task'''

a=2
b=3
print(a+b)


'''Comments
---------
-->These are 2 types
1.single line
-->This is used to explain about that oarticular line in a code, for this we can use # simbol
2.multi line
--> To comment more than single we can use multi line commenting """double triple codes"""
'''
a, b, c = 23, 56, 78 #here in the same line i declared three variables



'''Boolean type
-->this is used to find out the statement is True or false'''

a = 90
b = 9
print(a==b)
print(a!=b)

num=7
if num%2==0:
    print(f"{num} is even number")
else:
    print(f"{num} is odd number")

