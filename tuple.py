
# Write pythonn progrogram to calculate the product multyplying all number of the given tuple
H = (1,2,3,5,6,)
print("Original numbers\n")
print(H)
li = list(H)
product = 1
for i in H:
    product *= i
print("Product multyplying all the product ",product)