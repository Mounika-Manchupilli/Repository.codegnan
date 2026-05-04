'''
Pattern programs
----------------

num = int(input("Enter number:"))
for j in range(1,num+1):
    for i in range(1,j+1):
        print("*", end = "")#end is used to print stars side by side
    print()#to end loop and print stars we use this print


Pattern printing by using numbers
---------------------------------
num = int(input("Enter number:"))
for j in range(1,num+1):
    for i in range(1,j+1):
        print(i, end = "")
    print()

Reversing the pattern
---------------------
num = int(input("Enter number: "))
for i in range(num,0,-1):
    for j in range(1,i+1):
        print("*",end = "")
    print()
Reversing the pattern using numbers
-----------------------------------
num = int(input("Enter number: "))
for i in range(num,0,-1):
    for j in range(1,i+1):
        print(j,end = "")
    print()


num = int(input("Enter number: "))
for i in range(num):
   print(" ",end="")
   for j in range(i+1):
       print("*",end ="")
    print()


num = int(input("Enter number: "))
for i in range(num):
    for j in range(num-i-1,0,-1):
        print(" ",end = "")
    for k in range(i+1):
        print("* ",end ="")
    print()


num_ = int(input("Enter a first number: "))
num_2 = int(input("Enter a second number: "))
choice = int(input("\n1.Add \n2.sub \n3.Multiplication \n4.square"))
if choice == 1:
    print(num_ + num_2)
elif choice == 2:
    print(num_ - num_2)
elif choice == 3:
    print(num_ * num_2)
elif choice == 4:
    print(num_ ** num_2)
'''
















   
