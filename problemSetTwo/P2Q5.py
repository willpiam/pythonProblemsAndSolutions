"""
Name: william
File Name:P2Q5-
Date: march 6th 2018
description:
    Write a password checker. Your password checker will first ask for a password, then repetitively ask the user to 
repeat the password until the user types the original password. It must acknowledge that the right password 
was provided. 
Do not
 use an IF statement
 """
import time#used for stilish delay

answer = None #var answer becomes the users guess at the password they just created

word = input("enter a password: ")#gets password as word

while (word != answer):#I have to avoid using if statments... luckely im a super hacker
    print ("")
    answer = input("please enter the password: ")



for i in range (0,10):#makes it look like the program is thinking
    time.sleep(0.1)
    print (">")

print ("******Password Correct******")#nice styling to make it look more top secret
print ("Access Granted")


    
