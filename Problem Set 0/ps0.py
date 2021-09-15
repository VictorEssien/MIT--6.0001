# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 2:45:15 2021
@author: Victor
"""

""" Problem Set 0"""
import math
import numpy as np

x = input("Enter number x: ")
y = input("Enter number y: ")
x = int(x)
y = int(y)
print("")
print("x**y = ",x**y)
math.log(x,2) #log can take in two arguments; one is the input, the other is the base - in this case; base 2




#Just as an aside
#You could also rewrite the above in Python as:
print("The log of 2 base two is: ", math.log2(2))
print("")

#You could also use numpy to find the log:
print("The log of 2 base two is: ", np.log2(2))
print("")

#The log functions however, return the output as floats, so you could convert to integer
print("The log of 2 base two (in integer) is: ", int(math.log2(2)))
