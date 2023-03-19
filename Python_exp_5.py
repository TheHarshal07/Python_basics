#Python Exp 6:

    # Aim - Write a pyhton program for user define function and built in function



# 1. User define function 

def myfunction(fname,lname):
    print(fname+" "+lname)

myfunction("Harshal","Bhogal")   

print("--------------------------------------")
print(" ")

def HEllo(*kids):
    print("The Youngest child id "+kids[1])

HEllo("Thor","Avengers","loki")



# 2. Built in function

li = [1,56,23,86,34,779]

h = li.index(23) # Which give index value at specific position
print(h)

g = li.insert(0,100) # Herer the 100 is inserted at first
print(g)

li.pop() # Which pop the top most element on the list
print(li)

li.append(500) # Here 500 number append at the last
print(li)

li.reverse()
print(li)