num = [1,2,3,4]
any = list(map(lambda x:x*2, num))
print(any)

'''
List Comprehension
------------------
-->List comprehension offers shorter syntax when we want to create a new list based on the values of an existing list

syntax-->[expression loop condition]

old_list = [1,4,2,34,56]
new_list = [i for i in old_list]
print(new_list)

old_list = [1,4,2,34,56]
new_list = [i for i in old_list if i%2 == 0]
print(new_list)


old_list = [2,3,45,6,4]
new_list = ["even" if i%2 == 0 else "odd" for i in old_list]
print(new_list)

old_list = [2,3,45,6,4]
new_list = [i if i%2 != 0 else "even" for i in old_list]
print(new_list)


Dictionary comprehension
------------------------
-->Dict comprehension shorter syntax when we want to create a new dict based on the values of an existing dict.
'''
an = {"a":2, "b":3,"c":5}
any = {x:y for (x,y) in an.items()}
print(any)

nums = [1, 2, 3, 4]
result = {x: "Even" if x % 2 == 0 else "Odd" for x in nums}
print(result)

an = {"a":2, "b":3,"c":5}
any = {x:y for (x,y) in an.items() if y%2==0}
print(any)
