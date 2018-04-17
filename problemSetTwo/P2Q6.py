"""
Name: william
File Name:P2Q6-
Date: march 6th 2018
description:
    Write a program that asks for a numeric range.  For all the numbers in that range, calculate and display the 
square, square root and cube of the number
"""
import math
num1 = int(input("enter the first number: "))#gets the number range
num2 = int(input("enter the second number: "))

numlist = []#invent my lists
sqrlist = []
rootlist = []
cublist = []

for i in range (0, num2-num1+1):

    #my math
    numlist.append(num1 + i )#the number
    sqrlist.append(math.pow(numlist[i],2))#power of 2
    rootlist.append(math.sqrt(numlist[i]))#the root
    cublist.append(math.pow(numlist[i],3))#power of 3
    
    
    

    print ("-------NUMBER "+str(i+1)+" -------")#my print outs
    print (numlist[i])
    print ("")

    print ("-------SQUARE "+str(i+1)+" -------")#title
    print (sqrlist[i])#content
    print ("")#spacing

    print ("--------RO0T "+str(i+1)+" --------")
    print (rootlist [i])
    print ("")

    print ("--------CUBE "+str(i+1)+" --------")
    print (cublist [i])
    print ("")
    print ("")#extra spacing at the end of the loop
    print ("")
    print ("")
    print ("")
    print ("")

    

    


