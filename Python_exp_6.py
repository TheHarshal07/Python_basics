#Python Exp 6:
    #Aim - Write a program for demonstration of object oriented concept like classes, objects, inheritance.

    #Pyhton program using Inheritance
class Parent:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    
    def printname(self):
        print(f"My name is:{self.fname} {self.lname}")
    #single Inheritance...
a=str(input("Enter your First Name"))
b=str(input("Enter your Last Name"))
x = Parent(a,b)
x.printname()

    #multi Inheritance...
class Student(Parent):
    pass

c=str(input("Enter your First Name"))
d=str(input("Enter your Last Name"))
x = Student(c,d)
x.printname()

    #Super...
class Spec(Parent):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.gradYear = year

    def wlcm(self):
        print("Welcome",self.fname, self.lname,"to the class of",self.gradYear)

y=int(input("Enter your Graduation Year"))
x = Spec(c,d,y)
x.wlcm()








    # pyhton progrm using classes and objects
class Emp:
    count =0
    
    def __init__(self,name,lname,Empid):
        self.name = name
        self.lname = lname
        self.Empid = Empid
        Emp.count+=1
    
    def displacement(self):
        print("Total Employee %d" %Emp.count)
     
    def displayEmp(self):
        print("Name",self.name,"\n" "Lname:",self.lname,"\n" "ID",self.Empid)
        print(" ")
        

emp1 = Emp("Harshal","Bhogal",123)
emp2 = Emp("Ram","Charan",456)    


emp1.displayEmp()
emp2.displayEmp()
emp2.displacement()