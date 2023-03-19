str = "How are you Harshal"
print(str[0:19]) # Here we cam print whole string where the string lenght is 18 but 19 is excluding

print(str[0:3]) # Here we can print first string - How

print(str[0:7:2]) # Here we can print 0 to 7 string and then skiping 1 charatcter

print(str[:]) # By using [:] we can print whole string

print(str[0::1]) # Here is also same [0:] - will print entire string after that [:1] - they skip one character 

print(str[::-1]) # Here we can print string in reverse order 


print(str.isalpha()) # Here we can check si the string is alfa numeric or not 
print(str.isalnum()) # Here we can check if string is alfa numeric or not 
print(str.capitalize()) # Here we make string capitalize 
print(str.upper()) # Here we can make string upper case
print(str.endswith("Harshal"))  # Here we can check if the last string is ending with or not 
print(str.find("are")) # Here we can find string at which postition
print(str.count("H")) # Here we can find the number of H in whole string