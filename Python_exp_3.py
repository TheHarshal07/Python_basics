#Python Exp 3:
    #Aim - a
        #write a program to print th following pattern
        #1
        #12
        #123
        #1234
        #12345

print("Number pattern\n")
row=6
for i in range(1,row+1,1):
    for j in range(1,i+1):
        print(j,end='')
    print(" ")


    #Aim - b
        # Write the program to reverse the number 
        # input - 12345 
        # output - 54321

t = int(input("Enter the number\n"))
rev=0
while(t!=0):
    rem = t%10    # 123 % 10 = 3
    rev = rev*10 + rem  #  0 = 0*10 + 3 = 3
    t = t//10     # n = 123//10 = 12
print(rev)


    #Aim - c
        # Write the program to check wether the given number is prime or not 

h = int(input("Enter the number\n"))
k=0
if(h==0 and h==1):
    k=1
for i in range(2,h):
    if h%2==0:
      k=1
if k==1:
    print("The given number is not prime number\n")
else:
    print("The given number is prime number\n")