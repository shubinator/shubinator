#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 16:35:36 2021

@author: shubhamchohda
"""

# The goal of this programming exercise is to make sure your python and numpy installations are correct, 
# to get you more comfortable with using Spyder, and to begin using simple elements of Python. 
# Standard elements of a program include the ability to print out results (using the print operation), 
# the ability to read input from a user at the console (for example using the input function),
# and the ability to store values in a variable, 
# so that the program can access that value as needed.
import numpy

x= int(input("Please Enter  Number X:"))
y = int(input("Please Enter  Number Y:  "))
result = x**y
print(result)
print(numpy.log2(x))
