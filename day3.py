'''Operators
------------
1.Arithmetic Operators
2.Assignment Operator
3.Comparison Operator
4.Logical Operator
5.Identity Operator
6.Membership Operator
7.Bitwise Operator

1.Arithmetic Operator --> +,-,%,*,**
'''
Num = 10
nUm =20
NuM = 30
print(Num + nUm + NuM)
#O\P: 60

num = 6
num_2 = 9
print(num-num_2)
#O\p:3

a = 7
b = 6
print(a%b)
#O\P:1
print(a==b)#False
print(a!=b)#True

digi_ = 9
digi_1 = 3
print(digi_ * digi_1)
#O\P:27
print(digi_ ** digi_1)
#O\P: 729

digi_ = 9.56
digi_1 = 3.8
print(digi_ // digi_1)
#O\P: 2.0

'''Assignment Operator
-----------------------
-->It assigns the datatype to the variable
-->=,+=,-=.*=,\\=
'''

number = 9
number += 1
print(number)
#O\P:10

a= 9
a-= 4
print(a)
#O\P:5

B=79
B*=56
print(B)
#O\P:4424

C= 2.56
C //= 3.26
print(C)

Number = 45
Number_ = 38
print(Number != Number_)
#O\P:True

NUM = 2
NUM_= 3
print(NUM > NUM_)
#O\P:False

NUM_ = 2
NUM_ >= 3
print(NUM_)

'''
Logical Operator
----------------
and --> the 2 conditions should be true
'''
v = 2
n = 3
print( v>10 and v<3)
#O/P: False
print(v<10 and v<3)
#O/P:True

'''
or --> any one condition should be true'''
G = 2
H = 3
print( v>10 or v<3)
#True

'''
not--> to reverse the output'''

i = 2
j = 3
print( not(i>10 or j<3))
#True

'''
Identity Operator
-----------------
is --> It is used to check the object
is not --> this operator is used to check the object not same
'''

y = 9
z = 9
print(y is z)
List = [1,2]
List_= [1,2]
List_3 = List
print(List is List_3)
print(List is List_)
print(id(List))
print(id(List_))
print(id(y))
print(id(z))
print(List is not List_)

'''Bitwise operator
-------------------
&--> Bitwise AND
5-->0101
3-->0011
--------
1-->0001
'''
print(5&3)
      












