'''
num = 0
num_1 = 1
any = int(input("Enter a number: "))
print(num,num_1,end=" ")
for j in range(1,any+1):
    num2 = num + num_1
    num = num_1
    num_1 = num2
    print(num2,end=" ")


Armstrong = int(input("Enter a number: "))
total = 0
length=(len(str(Armstrong)))
for j in str(Armstrong):
    total += int(j) ** length
if total == Armstrong:
    print(f"{Armstrong} is a Armstrong number")
else:
    print(f"{Armstrong} is not a Armstrong number")


num=int(input("Enter a num: ")
if num % 3 == 0 and num%5 == 0:
    print(f"{num} is Divisible by 3 and 5")
else:
    print(f"{num} is not Divisible by 3 and 5")


num=100
for j in range(1,num+1):
    if j % 3 == 0 and j % 5 == 0:
        print(f"{num} is Divisible by 3 and 5")


num=100
def Divi_(num):
    for j in range(1,num+1):
        if j % 3 == 0 and j % 5 == 0:
            print(f"{num} is Divisible by 3 and 5")
Divi_(num)



any = [34,24,36,17,27]
def sum_even(any):
    total = 0
    for j in any:
        if j % 2 == 0:
            total += j
    print(total)
sum_even(any)


Lambda Function
---------------
-->A lambda function is a small anonymous function
-->This lamda function can take n number of arguments but can only have one expression

syntax--> lambda keyword followed by (arguments): expression

an = lambda a,b:a*b
print(an(5,6))

an = lambda a,b:a+b
print(an(45,67)
'''
a=int(input())
b=int(input())
def square():
    print(a*b)
square()












