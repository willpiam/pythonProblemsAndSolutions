"""

author:willpiam
date:feb 21 2018
description:finds perimeter of rectangle based on user inputs



1. get length
2. get width
3. mult by 2 and add
4. output
"""
import sys

print ("I am a program that calculates the perimiter of a rectangle")
print ("what is the length?")
w = int(input("enter a number"))

sw = str(w)


print (sw + " is the width please tell us what the length is")

l = int(input("enter another number"))

sl = str(l)

print (sl + "is the length")

a = ((2*l)+(2*w))

sa = str(a)
print ("the parimeter of the rectangle is " +sa+" cm ")
