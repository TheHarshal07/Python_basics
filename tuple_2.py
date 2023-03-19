# Wrtie the program to convert a tupleof string valus to tuple of integers

tuple_str= (('12','124'),('4521','125'))
print("Original numbers\n")
print(tuple_str)
print("New values of tuple \n")
# for i in tuple_str:
#     r+= tuple(int(i[0]))
r=tuple((int(i[0]),int(i[1]))for i in tuple_str)
print(r)

