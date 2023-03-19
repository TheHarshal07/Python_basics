# tuplle - is immutable (we can not change value)
# In tuple we can't change, update,insert values 

a = ("Harshal","is","genius","boy")
print(type(a))

# but Yes we can change type from tuple to list, after changing from tuple to list now we make changes 

l = list(a)
l.insert(4,"Yes I am")
print(l)