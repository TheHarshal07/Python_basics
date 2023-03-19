
li = [23,45,67,34,77]
size = len(li)
print(li[0])
temp =li[0]
print(temp)
li[0] =li[size-1]
li[size-1] = temp
print(li)