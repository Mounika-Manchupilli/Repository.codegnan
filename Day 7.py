'''set datatype
---------------
-->set is a collection of unordered elements or unique elements unlike list or tuple set is not permit duplicates in side
-->Indexing is not possible in sets
-->set is mutable
Methods
-------
add()
----
-->This method is used to add new item into the set
syntax --> variable_name.add(item)
'''
sn = {1,2,3,2}
print(sn)
sn.add(4)
print(sn)

'''
remove()
--------
-->This method is used to delete an item in the set
syntax--> variable_name.remove(value)
'''
sn = {1,2,3,2}
sn.remove(3)
print(sn)

'''
pop()
----
-->This is also used to delete element in the set, but we can not specify the element
syntax--> variable_name.pop(no arguments)
'''
sn = {1,2,3,2}
sn.pop()
print(sn)

'''
clear()
------
-->This method is used to delete all elements in the set
syntax-->variable_name.clear()
'''
sn = {1,2,3,4,5}
sn.clear()
print(sn)

'''
update()
-------
-->Same like add but this method will add more than one element
syntax-->variable_name.update([elements])
'''
sn = {1,2,3,4,5}
sn.update([6,7,8])
print(sn)

'''
union()
------
-->This method will return a set all elements from both sets, but not duplicates
syntax--> set_1.union(set_2) or set_1 | set_2

'''
sn = {1,2,3,4,5}
vn = {2,4,6}
print(sn.union(vn))
print(sn | vn)

'''
intersection()
-------------
--> This method will give only the common elements from both sets
syntax--> set_1.intersection(set_2) or set_1 & set_2
'''
sn = {1,2,3,4,5}
vn = {2,4,6}
print(sn.intersection(vn))
print(sn & vn)

'''
difference()
-----------
--> This method is used to get the different elements from both sets
syntax--> set_1.difference(set_2) or set_1 - set_2
'''
sn = {1,2,3,4,5}
vn = {2,4,6}
print(sn.difference(vn))
print(sn - vn)

'''
type conversions
----------------
--> Converting one data type to another data type
int to string and float
'''
a = 8
b = str(a)
print(b)
print(type(b))
c = float(a)
print(c)
'''
float to int and str
'''
z = 56.78
d = int(z)
g = str(z)
print(g)
print(type(g))
'''
str to int,float,list,tuple
'''
c = "67"
i = int(c)
print(i)
print(type(i))

d = "67.98"
i = list(d)
print(i)
print(type(i))

f = "67.98"
i = tuple(f)
print(i)

'''
list to str, tuple
'''
d = [1,2]
i = list(d)
print(i)

d = [3,4]
i = tuple(d)
print(i)




