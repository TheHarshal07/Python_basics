#Pyhton Exp 4:
    # Aim - Write the program to find the second last number in the list

print("-----------------------------------------------------------------------------")
print("Write the program to find the second last number in the list\n")
l =[34,24,54]
l.sort()   # Here the sort the given list as [24,34,54]
print(l[-2]) 


    # Aim -  Write the program to find index of an item in tuple

print("-----------------------------------------------------------------------------")
print("Write the program to find index of an item in tuple\n")
t1 = ("Hello Harshal How are you ?\n")
print(t1.index("Harshal"))
print(t1.index("H",8,20))

    #Aim -  Write the program to convert a tuple if string values to a tuple of integer value

print("-----------------------------------------------------------------------------")
print("Write the program to convert a tuple if string values to a tuple of integer value\n")
r=0
tuple_str= (('12','124'),('4521','125'))
print("Original numbers\n")
print(tuple_str)
print("New values of tuple \n")
# for i in tuple_str:
#     r+= tuple(int(i[0]))
r=tuple((int(i[0]),int(i[1]))for i in tuple_str)
print(r)