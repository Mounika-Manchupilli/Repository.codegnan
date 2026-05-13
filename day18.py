'''
Modules
-------
-->A module is a file containing python code such as:
variables
functions
classes

import my_module
print(my_module.add(5,3))
print(my_module.sub(4,2))
print(my_module.mul(4,2))
print(my_module.div(4,2))
print(my_module.module1())
print(my_module.hello_world())


Modules help us:
-->Reuse of code
-->reduce code duplicate

Types of modules
----------------
-->User defined modules
eg
import my_module
print(my_module.div(4,2))
print(my_module.module1())

-->In -built modules
--os
--math
import math
print(math.sqrt(49))
print(math.sin(90))
print(math.factorial(9))

--sys module
-----------
-->sys module is system-soecific parameters and functions.

import sys
print(sys.version)

-->To use all this modules, we have to import with module name

ways to import modules
----------------------
1.using Alia(as) name

import my_module as my
print(my.div(4,2))
print(my.module1())

2.import entire module
import my_module
print(my_module.add(5,3))
print(my_module.sub(4,2))

3.import all functions

from math import *
print(pow(49))

4.import specific function

from math import sqrt
print(add(4,7))


random module
-------------

import random

otp = random.randint(1000,9999)
print("Your OTP is",otp)

import random
score = 0
for round in range(1, 4):
    print("Round", round)
    computer = random.randint(1, 10)
    user = int(input("Guess a number between 1 to 10: "))             
    if user == computer:
        print("Correct Guess!")
        score += 2
    else:
        print("Wrong Guess!")
        print("Correct number was:", computer)
    print("Current Score:", score)
    print()
if score > 0:
    print("You Won")
else:
    print("You Fail")
'''
a = "Python is easy to learn"
b = a.split()
count = 0
for i in b:
    count += b
    print(count)
















