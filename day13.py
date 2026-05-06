'''
Function
--------
-->This is the block of code that can be reusable
-->A function can only run when it is called.
-->def is the keyword used to define the function

def func_name(parameters):
    ---------
    ---------
func_name(arguments)



num = 9
def even_odd(num):
    if num % 2 == 0:
        print(f"{num} is a even number")
    else:
        print(f"{num} is a odd number")
even_odd(num)
even_odd(39)


Required arguments
------------------
-->A fuction must called with the correct number of arguments, that means if function expects 2 arguments, we have to call function with 2 arguments not less or not more.

def even_odd(num,num1):
    print(num+num1)
even_odd(9,43,67)#There is a mismatch in arguments so type error will come

def even_odd(num,num1):
    print(num+num1)
even_odd(9,43)


Default Arguments
-----------------
-->By default, value is taken from the calling function 


def even_odd(name = "mounika"):
    print(f"hai {name}")
even_odd("manchupilli")
even_odd("pujitha")
even_odd()


Keyword Arguments
-----------------
-->Here we can send arguments with a key = value syntax. By this the order of arguments does not matter.
'''

def even_odd(num_2,num_3,num):
    print(num+num_2+num_3)
even_odd(num=9 ,num_2=8, num_3=1)
























