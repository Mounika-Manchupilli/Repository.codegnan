'''
while loop
--------------
->This while statement will keep on executing until unless condition becomes true
ex:
v=1
while v<=5:
      print(v)
      v+=1
range()
-----------
-->this range() will generate sequence numbers upto the limit
syntax-->range(starting, ending, step)
eg:
choice_U = int(input("enter the limit:"))
for j in range(100,choice_U+1,3):
    print(j)
'''
'''
for i in range(2,101):
    if i%2==0:
        print(f"{i} is even number")
    else:
        print(f"{i} is odd number")
'''

'''break
--------------
-->this break statement will exit if the condition becomes true, and never enter into next loops
eg:
any = ["aareffa", "mouni","haniya","pujitha"]
for i in any:
       print(i)
       if i=="mouni":
          break
continue
-------------
-->this statement will skip that particular iteration and goes to next iterations
any = ["aareffa", "mouni","haniya","pujitha"]
for i in any:
       if i=="mouni":
          continue
       print(i)

pass
--------------
-->pass is space holder, holds the space not to get any error
a=90
b=90
if a>= b:
    pass

nested loop
---------
--> a loop in side the loopis called nested loop
'''
for j in range(2,100):
    count = 0
    for an in range(1,j+1):
        if j % an==0:
            count+=1
    if count==2:
        print(f"{j} is a prime")
    else:
        print(f"{j} is not a prime")
