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
