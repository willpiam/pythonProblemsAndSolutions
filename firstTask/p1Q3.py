"""
author:willpiam
date:feb 21 2018
description:finds area of a triangle based on user inputs

"""
import sys

print ("I am a program that calculates the area of a triangle")
print ("what is the height?")
w = int(input("enter a number"))

sw = str(w)


print (sw + " is the height please tell us what the base is")

l = int(input("enter another number"))

sl = str(l)

print (sl + "is the base")

a = (l*w)/2

sa = str(a)
print ("the area of the rectangle is " +sa+" cm squared")
