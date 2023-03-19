#Python Exp 8:
    #Aim - 
        # WAP pyhton pogram to import following types of modules
        # 1. User define modules
        # 2. Inbuilt modules

from pkgutil import ImpImporter
import usermodule
a = usermodule.jarvis("Harshal","Bhogal")

import usermodule
p=usermodule.pro["Marvel"]
print(p)

# Inbuilt module
import math
print(math.sqrt(100))
print(math.factorial(3))

import os
os.makedirs("H:\\Hars")
os.listdir()  # It will give list of all anf directory

import random
print(random.random()) # It will give random value
print(random.seed())

import statistics
print(statistics.mean([2,5,6,3]))
print(statistics.mode([3,6,3,6])) # calculate the mode (central tendency) of the given numbers

import time
print(time.ctime())
print(time.time()) # It will show number of seconds pass in epoch




 
# x = "Hello"[0]
# x.up
# print(x)
