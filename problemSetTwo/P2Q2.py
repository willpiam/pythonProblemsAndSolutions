"""
Name: william 
File Name:P2Q2
Date: march 5th 2018
description:

  Ask the user for a number and print that many '*' characters
in a horizontal line.  You are going to have to override the 
default function of print().  Here's how to avoid the newline 
character from printing: print('*', end=''

"""

num = int(input("enter a number"))#gets number as int

for i in range(0,num):
    print ("*", end="")#this line prints * but doesnt make it a new line
    

