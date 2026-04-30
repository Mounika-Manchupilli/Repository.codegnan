'''
List data type
--------------
-->List is a collection of different data types and it is represent by [] seperated by comma
any = [1,"pujitha",[2,"this is 5th class",3],56]
print(any[2][1][10])
any = [1,"python is a language",67,68,[34,["this is python class"],78,"i'm looking for good bat",[2,"this is 5th class",3],56]]
print(any[4][1][0][14])
methods
-------
1.append()
---------
---->this method is used to add new item into list but it will add in the last index postion
syntax-->vvariable_name.append(item)
eg:
an =[1,2,3,4]
an.append(78)
print(an)
an.append([0,90,78,45])
print(an)
2.extend()
----------

--->This method is also used to add new item into list,but this extend  add as each position  to each index in the list
---->extend only tales itterables linke list,string,tuple
syntax-->variable_name.extend(item(itterables))
eg:
any=[1,2,3,4]
any.append("python")
print(any)
any.extend("python")
print(any)
3.pop()
-------
--->this is used to delete an item from the list,this pop() remove the value based on the index position mentioned in the paprameters
--->if nothing is mentioned in the parameters,it will remove last index position value
syntax-->variable_name.pop(index position)
eg:
any=[1,2,3,4] #it pop only gives the based on the index position
any.pop()     #pop is out of range the error will apear
print(any)
4.remove()
---------
---->This is also used to delete item from the list,but remove() method will delete value
syntax-->variable_name.remove(value)
eg:
any=[1,2,3,4] 
any.remove(4)
print(any)
5.slicing
---------
---->This is used to get the particular part of the list,string or tuple
--->This will work based on index position
syntax->variable_name[starting index : ending index]
eg:
any=[1,2,3,4,5,6,7] 
print(any[2:5])
6.len()
------
---->Method is used to find the number of items present in the list

syntax---->len(variable)
eg:
any=[1,2,34,5,6]
print(len(any))  #o/p:5

any="python is a language"
print(len(any))  #o/p:20
'''
