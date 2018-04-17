"""
author:willpiam
date:feb 21 2018
description:finds area of rectangle based on user inputs

"""
import sys

print ("I am a program that calculates the area of a rectangle")
print ("what is the length?")
w = int(input("enter a number"))#gets width and saves as an int

sw = str(w)


print (sw + " is the width please tell us what the length is")

l = int(input("enter another number"))#gets length as int

sl = str(l)#makes it a string

print (sl + "is the length")

a = l*w#area = length times width

sa = str(a)#converts to string
print ("the area of the rectangle is " +sa+" cm squared")
