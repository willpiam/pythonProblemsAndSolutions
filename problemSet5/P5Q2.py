"""
date:30042018
programmer: William
filename: P5Q2.py
description: Replace all sequences of blanks in a user inputted string with a 
single blank

help from: stackoverflow
"""
import re
#get raw user input
string = input("Please enter a phrase here:")
string = re.sub(" +", " ", string)
print (string)
