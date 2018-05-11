"""
date: 11042018
william 
file name p3q4-doyle.py
description:


"""

def getMass():#gets mass (in grams from user)
    mass = str(input("What is the mass of the letter in grams?  "))
    mass = checkInputIsValid(mass)
    return int(mass)

def checkInputIsValid(value):
    num = 0#makes sure var is an int
    string = ""
    try:
        num = int(value)
        string = value
    except ValueError:
        print ("please try again but remember... no decimals... only numerals")
        print ("value given is not an integer")
        string = getMass()
    return string

def findPrice(mass):
    price = 0.0
    mult50 = 0.0
    if (mass <= 30):
        price = 0.30
    elif (mass <= 50):
        price = 0.70
    elif (mass <= 100):
        price = 0.90
    elif (mass >100):
        mult50 = (mass-100)/50
        price = (0.90)+(0.20*mult50)
    
    return str(price)
   
print ("the price is:"+findPrice(getMass()))



"""
----------ISSUES I OVER CAME----------------
ISSUE: if user enterd non int program would make them redo it untill they gave an int
    however once program had int it would just return the original input
SOLUTION:
    explained issue to a friend (dispite the fact she does not understand ay of this)
    in explaining i realized how to solve my issue.

"""
