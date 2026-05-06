'''
so = eval(input("Enter items of list: "))
empty_ = []
for i in so:
    if i not in empty_:
        empty_.append(i)
print(empty_)
'''

nums = [10,2,20,76,4,46,99]
max1 = 0
max2 = 0

for num in nums:
    if num > max1:
        max2 = max1
        max1 = num
print(max2)
 
