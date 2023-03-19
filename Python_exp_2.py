#Pthon Exp 2:
    #Aim - 
        # # Write a pyhton program to accept the cost of bike and display the road tax to be paid according to the following criteria 
        # # Tax  Cost price 
        # # 15%  >100000
        # # 10%  >50000 and <=100000
        # # 5%   <=50000

a = int(input("Entert the cost price of bike\n"))
tax=0
if(a>100000):
    tax = 15/100*a
elif (50000<a<=100000):
    tax = 10/100*a
elif (a<=50000):
    tax = 5/100*a
print("Tax to be paid",tax)
print(" ")
print("---------------------------------------------------------------")

# # Write a program to check whether the number is divisible by 3 and 2

num = int(input("Enter the number\n"))
if(num%2==0 and num%3==0):
    print("The number is divisible by both 2 and 3")
else:
    print("The number is not divisible by 2 and 3 \n")
print(" ")
print("---------------------------------------------------------------")

# Write a program to check if whether is year is leap or not 

n = int(input("Enter the number\n"))
if(n%100==0):
    if(n%400==0):
        print("Given year is lean year\n")
    else:
      print("Given year us not leap yeat\n")
else:
    if(n%4==0):
        print("Given year is leap year\n")
    else:
        print("Given year is not leap year\n")

