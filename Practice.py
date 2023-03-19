
a= int(input("Enter the first number: "))
b= int(input("Enter the sevond number: "))
c=a+b
print("Addition of the two numbers is ",c)
# print(type(c)) # ( typecasting )  by using this we can check which type of string 
# print("Addion of the two number is ",end='') # end='' - which skip new line i.e print two at string on same line 
# print(c)
# print("Hello", "python","Harshu","hey",sep = " ") # sep+" " - Which use to seperate the string
# name = input("Enter your name\n") # which take input from user
# print("Your name is ",name)
# print("{} is good boy, {} boy".format(a,b)) # Which print value of a and b instead of {} by using format function

# a =int( input("Enter the value of a ")) # typecasting
# print(a)
    

#                           ## String slicing ##

# str = "Harshal is good boy"
# print(str)
# print(len(str))  # which print length of string

# print(str[0:19]) # Here we can find lenght of string at any positon (0 - including and 19 - excluding )
# print(str[0::7]) # Here [0:] - will take full length of string after [:7] - skip 7th character 
# print(str[::-1]) # Here it will print string in reverse order
# print(str[::-2]) # which print string reverse order and skiping 1 character
# print(str[0:7:2]) # Here string print from 0 to 7 -(Harshal) and then skiping 1 character 

# print(str.isalpha()) # they check if string is alpha numeric or not - (false)
# print(str.isalnum()) # they check if string is numeric or not  - (false)
# print(str.endswith("boy")) # check if string is ending with which character
# print(str.count("i")) # count number of character in string ( count "i" in string )
# print(str.capitalize()) # Capitalize character in string 
# print(str.find("good")) # find the word in string at which index they start 

# print(str.lower()) # Convert it into lower case 
# print(str.upper()) # Convert the string into upper case
# print(str.replace("is","are")) # replace string with another string 


                       ## List ##



# details = ["Harshal","Sudhir","Bhogal", 34]
# print(details[1])  # print string at index 1 from list

# numbers = [7,4,30,10,3,2]
# numbers.sort()     # sort function is used to sort the list
# numbers.reverse()  # reverse function is used to reverse numbers in list

                         
                         # List Slicing #
# print(numbers[:])  # Here [:] - Which find length of list
# print(numbers[0:2])
# print(numbers[::-1])
# print(numbers[::2])
# print(max(numbers))
# print(min(numbers))

# numbers.append(7) # append function used to add number at the last (i.e 7 no. is added to last index)
# numbers.insert(1,34) # insert function is used to add number in the list at given particular index
# numbers.remove(34) # Remove number in list
# numbers.pop()      # remove last number in list
# print(numbers)

                     # Tuple #
# tuple can not be change 

# Mutable - Can change 
# Immutable - Cannot change

# H = (2,4,5)
# a = (2,)
# print(H)

#                      # swapping #
# a = 20
# b = 30
# a,b = b,a  # swaping logic
# print(a,b)


#                      # Dictionary #
# #Dictionary in nothing but key values pairs

# d = {"Harshal":"pizza", "Saurabh":"burger","rohan":"Roti","Rocky":{"B":"Bred", "L":"Rice","D":"Roti"}}  # This is dictonary 
# print(d["Harshal"]) 
# print(d["Rocky"]) # Here value of Rocky is dictionary inside the dictionary 
# print(d["Rocky"]["B"]) # here we can make one query inside the dictionary 

# d["Ram"] = "Smart man" # here we can add new items in dictinary
# d["Ankit"] = "Hello"
                                        

# # del d["Ankit"] # del function is used to remove the item in dictionary
# d.clear()  By using clear function we can remove compenents into the list but not the whole list
# # print(d) 

# d2 = d.copy() # here we make copy of d an d2 point to d dictionary
# del d2["Saurabh"] # So if I remove Saurabh in d2..it's only remove from dictionary d2.. The copy of d will remain same
# print(d)

# print(d.get("Harshal"))  # It will rerutn the value of item
# d.update({"Harshal":"Thor"}) # By using update command we can update item in dictionary
# print(d)

# print(d.keys()) # keys command will return the keys in dictionary
# print(d.items()) # this command will print items in dictionary


                  # Dictionary Exercise #
# create dictionary and take input from the user and return the meaning of the wprd from dictionary

# Dict = {"Pyhton":"Programming language", "NLP":"Natural language processing","AI":"Artificial Intelligence"}
# user = input("Enter the word\n")
# print(Dict[user])


                  # Set #
# set retain unique values
# d = set()
# d.add(1)  # adding into the set
# d.add(1)
# print(d)

# s = set([1,2,3,4,5])
# # print(s)
# # print(type(s))

# s1 = s.union([6,7,8]) # Union function is used to combined two set
# print(s,s1)
# # s1 = s.intersection([1,2,3,4,5,6]) 
# # print(s,s1)
# s.remove(1)
# print(s)

             # Opetators #

# a=20
# b=4
# print(a>b)

# print((a>b)and(a!=b))
# print((a==b)or(a<b))


# a = [23,45,34]
# print(23 in a) # membership operator

# a =23
# b =35
# print(a is b)

                                          # If Else statetment #

# a = 12
# b = int(input("Entert the number\n"))

# if b>a:
#     print("Greater")
# elif a==b:
#     print("equal")
# else:
#     print("Lesser")

                        # If age of any person which is grater than 18 then they can drive like that #

# name = int(input("Enter your age\n"))

# if 0<name<=100:
#     if name>18:
#         print("You can dirve\n")
#     elif name==18:
#      print("we can't say that\n")
#     else:
#       print("you can't drive\n")
# else:
#     print("wrong agw\n")


            # Loops in python #

# list = [["Harshal",10],["Saurabh", 20],["Marie",5]] # here we make list of list and can print seperate list

# # for item in list: # here by using for loop we can print whole list
# #     print(item)

# for item in list: # in this for loop we are going to print list of list
#     print(item)

# list = [["Harshal",10],["Saurabh", 20],["Marie",5]]

# # for item,ingre in list:  # In this for loop we can print item with thier parameter e.g Harshal 10
# #     print(item,ingre)

# a = dict(list)   # here we can use dict function to print list
# for item,ingre in a.items():
#     print(item,ingre)




              # while loop #
# i=0
# while(i<10):
#     print(i)
#     i=i+1

               # Control satements :
# 1/Conditional branching/Decison making statement 
# if satement 
#if else satement
# if else if satement
# nested if else satement 

# num = 10
# if(num>0):
#     print("Hello Harshal\n")  # when we leave the space after the if satement this called as scope
#     print("Hey you are genius person\m")

 

          # else if ladder (nested if else satement)

# num = int(input("Enter the number\n"))

# if(num>=0):
#     if(num==0):
#         print("The number is zero\n")
#     elif num<0:
#         print("The number is negative\n")
# else:
#     print("The number is postive\n") 
     
        
        
           # short hand if statement #
# a = 5
# if a>4 : print("a is greater than 4\n")

# q =4
# r =6
# print("q") if(r>q) else print("r") # here we can write  short hand if else satement in which we have to write print satement first 
                                   # then we have to write if or else statement




                            # Loops in python #
# (Initalization , condition , incerement/dercrement )
# 1. While loop

# number = 1 
# while number<=5:
#     print("The number is \n")
#     number = number+1

# num =1
# evenNum = []
# while num<=10:
#     if(num%2)==0:
#        evenNum.append(num)
#        num+=1
# print("Event number are", evenNum)





       # For loop #

# a = int(input("Enter the number\n"))
# for i in range (0,a):
#        print(i)

# str = "Harshal"
# for s in str:
#        print(s,end='')

# list = ["Hello","Harshal","How are you"]
# for i in range(len(list)):
#        print(list[i], end=' ')



              # Star pattern #

# for i in range(1,5):
#        for j in range(i):
#               print("*",end ='')
#        print()



      # Break and Continue statement #

# Break Statement 
# hr = "Harshal"
# for i in hr:
#        if i =='h':
#               break
#        print(i,end = '')

# # Continue statement
# for i in range (0,10):
#        if i==5:
#               continue
#        print(i,end ='')

      
                       # Pyhton 2nd module  - Advance data type 

# Advance data type :
# Number , int , float, complex 
# Boolean : True,False
# Sequence data type

# eg =["list",34,"Harshal"]
# print(eg[2])
# print(len(eg))
# eg.append("Thor")
# print(eg)
# eg.insert(0,245)
# print(eg)
# eg.remove("list")
# print(eg)




