"""
Name: william
File Name:P2Q8Take2-
Date: march 8th 2018
description:
    Draw a triangle of * characters given the user input of how 
high the triangle is (number of rows)

NOTE: This is like p2q8 but ive ripped out all the unnessary "junk"
"""
height = int(input("what is the height of your triangle?"))#gets height of triangle from user

num = []#block determines how many stars go in each line and saves that number in a list called num
for i in range (0,height):
    num.append("")
    if (i>0):
        num[i] = num[i-1]+2
    else:#if i == 0
        num[i] = 1
        
stars = []#block makes all the stars
for i in range (0,height):
    stars.append("")
    for k in range (0,num[i]):
        stars[i] = stars[i]+"*"
        
numSpace = []#block makes a list of numbers.. each number represents how many stars should go in each line
for i in range (0,height):
    numSpace.append("")
    numSpace[i] = i
numSpace.reverse()#because block starts out in wrong order this line is used to "flip" it

space = []#block makes the indentation 
for i in range (0,height):
    space.append("")
    for k in range (0,numSpace[i]):
        space[i] = space[i]+" "
        
for i in range (0, height):#block prints triangle to screen and attaches indents to stars
    stars[i] = space[i]+stars[i]
    print (stars[i])
