#Python Exp 7:
    #Aim - Write a program in python to implement polymorphism using methode overloading.

    # Method overloading using polymorphism

class Square():
    a = 5
    def cal_area(self):
        return self.a * self.a

class triangle():
    b = 6
    c =  7
    def cal_area(self):
        return 0.5 * self.b * self.c

s = Square()
t = triangle()

for obj in (s,t):
    print(obj.cal_area())


# print("Area of the square is ", s.cal_area())
# print("Area of the triangle is ", t.cal_area())
    
