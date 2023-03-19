number = int(input("Enter the number\n"))
result = 0
p=number
while number>0:
    rem = number%10
    result = (result*10)+ rem
    number //= 10

if p==result:
    print(p,"is a palindrome number")
else:
    print(p,"is not a palindrome number")