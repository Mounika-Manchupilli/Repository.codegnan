'''
Datatypes
---------
There are 2 types:-
1.mutable
2.Immutable
-->1.mutable datatype: It can modify directly on the variable, which the data type have taken
-->eg: list,dictionary
--->Immutable datatype: Where can't be modify directly on the variable assign to the data type
-->eg: int,string
'''
num = 9
num_2 = 2
print(num + num_2)
print(num)
print(num_2)

'''
integer or int
--------------
-->Storing number or digit in the variable is called int
num = 90

float
-----
-->Storing decimal value in the variable is called float
num_2 = 45.56

string or str
-------------
-->String is a collection of characters that are enclosed in '',"",''' '''
-->It is immutable data type

Methods
-------
replace(): This method is used to replace or change old sub string with the new string
syntax
------
variable_name.replace("old string", "new string "))

indexing
--------
--> This is used to get the particular substring , item from string, list and tuple by calling with index position
syntax
------
variable_name[index_position]
concatenation
-------------
-->A + acts as different ways, if we are adding 2 integers it acts like addition
in other cases such as list, string and tuple it act like concatenation



split()
-------
--> This method is used to separate the string using a substring and it will split into list such as before the substring is one index and after the substring is another index
syntax
------
variable_name.split("substring")
strip()
------
-->This method is used to remove from 1st index position or from last index position
join()
------
syntax
------
(substring.join(variable_name))
lower()
upper()
'''
any = "Python is a programming language"
print(any.replace("Python","Java"))
print(any)
print(any.replace(" ", "_"))
print(any[14])
print(any[9])

k = "python"
y = " language"
print(k+y)
L1 = [1,2]
L2 = [3,4]
print(L1 + L2)

z = "Python is a language"
print(z.split("is"))
print(z.strip("age"))
print(z.strip(" is"))
print("-".join(z))
print(z.lower())
print(z.upper())

NUM = int(input("enter a number:"))
print(f"{NUM} is a even number")




















