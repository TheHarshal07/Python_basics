result =0
print("Entert the number")
number = int(input())
p=number
while number>0:
   sum = number%10
   result = result+(sum*sum*sum)
   number //= 10

if(p==result):
    print(p,"is an Armstrong number\n")
else:
    print(p,"is not armstrong number\n")