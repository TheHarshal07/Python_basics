                             # Dictionary #

d = {"Harshal":"Thor","Rohan":"Marvel","Rohit":"Ant-man","Ajay":"Iron-man","MARVEL":{"Iron-man":"Tony","Thor":"Oden-putr"}} # Here we can maek dictionary inside the dictionary
print(d["Harshal"]) # Here we can print details of the Harshal

d["Ajay"] = "Spider"  # Here we can update the dictionary

d.update({"Rohan":"Hulk"}) 

print(d["MARVEL"]["Iron-man"])  # Here we can get item which inside the dictionary

print(d.keys()) # will return all keys in the dictionary

print(d.items()) # will return all items in dictionary

print(d.get("Rohit"))

del d["Ajay"]  # Here we can  remove item in dictonary
print(d)

d3 = d.copy() # We can create copy of the original dictionary
del d3["Rohan"]
print(d)






