'''
elif statement
--------------
--> This statement gives more options to get the result of that program
Eg
--

marks_stu = int(input("enter your marks:"))
if marks_stu >= 90 :
    print("A+")
elif marks_stu >=80 :
    print("A")
elif marks_stu >= 70:
    print("B+")
elif marks_stu >= 60:
    print("B")
elif marks_stu >= 50:
    print("C+")
else:
    print("Failed")
          
Nested if statement
-------------------
--> if statement in side another if statement is called Nested if statement.

user_SBI_info = {"ATM PIN": "6600"}
User_pin = input("Enter yout ATM: ")
if len(User_pin) == 4:
    if User_pin in user_SBI_info['ATM PIN']:
        print("Welcome to SBI ATM")
    else:
        print("pls enter correct pin")
else:
    print("pls enter 4 digit pin")

for statement
-------------
-->A for statement is used to iterate over items like (string,list,tuple) with fixed number of iterations.

any = [23,56,8,9]
for j in any:
    print(j)
else statement in for
---------------------
--> After completing all iterations will execute

any = [23,56,8,9]
for j in any:
    print(j)
else:
    print("loop finished")
'''

so = "madam"
empty_ = ""
for j in so:
    empty_ = j +empty_
if empty_ == so:
    print("Palindrom")
else:
    print("Not a Palindrom")
















