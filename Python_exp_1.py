#Python Exp - 1:
    #Aim - write a program to find the area of triangle, square and circle

# Area of the circle

a = int(input("Enter the radius of circle\n"))
ans = 3.14*a*a
print("Area of the circle is {} ".format(ans))

# area of square 

b = int(input("Enter the sides of square\n"))
sq = b*b
print("Area of the square is {}".format(sq))

# Area of the traingle

t = int(input("Enter the base\n"))
t2 = int(input("Enter the height\n"))
area = 0.5*t*t2
print("Area of the triangle si {} ".format(area))