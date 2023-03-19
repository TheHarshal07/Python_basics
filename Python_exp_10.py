# Pyhton Exp 10:

    # Aim -  Write a python program to display a simple calculator

def sum(n1,n2):
    return n1 + n2

def sub(a1,a2):
    return a1 - a2

def mul(b1,b2):
    return b1 * b2

def div (t1,t2):
    return t1 * t2
print("Enter the choice")
n = int(input(" 1.Addition\n 2.Substraction\n 3.Multiplication\n 4.Division\n "))
num1 = int(input("Enter the first number\n"))
num2 = int(input("Enter the second number \n"))

if (n==1):
    print("Addition of the two number is ",sum(num1,num2))
elif(n==2):
    print("Substraction of the two number is ",sub(num1,num2))
elif(n==3):
    print("Multiplication of the two number is ",mul(num1,num2))
elif(n==4):
    print("Division of the two number is ",div(num1,num2))
else:
    print("Error")
    

