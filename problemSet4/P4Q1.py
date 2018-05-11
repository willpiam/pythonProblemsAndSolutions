"""
date: 13042018
programer name: William 
file name: P4Q1.py
description and a few notes:

    Create a pay computation program which takes two parameters (hours 
    and rate). In North America, must employers will pay time and half over 
    40 hours. Research time and half if you have never heard of it. Your 
    program should output the payment to the employee including overtime 
    (time and half over 40 hours)

okay so whats the pay equation:
    rate = whatever
    ratePlus = rate * 1.5
    pay = 0
    pay2 = 0
    if (time < 40):
        pay = time * rate
    elif (time > 40):
        pay = (time-40)*ratePlus #with special rate
        pay2 = pay + (40*rate)
    pay = pay+pay2

"""

def getRate():#when called prompts user for a rate of pay. returns rate as a str
    print ("Good user! Please enter a payment rate!")
    rate = input("Do so here:")
    spacing()
    rate = chkFloat(rate, "r")
    return rate

def getHours():
    print ("Hello once more! Be a dear and enter an amount of hours")
    hours = input("Do so here:")
    spacing()
    hours = chkFloat(hours, "h")
    return hours

def spacing():#prints a single line of space
    print (" ")

def chkFloat(stg, frm):
    fType = 0.0
    try:
        fType = float(stg)
    except ValueError:
        print ("FFS! Don't give me anything that doesn't work as a float!! MOFO!!")
        if (frm == "r"):
            fType = getRate()
        elif (frm == "h"):
            fType = getHours()
        
    return fType

def isOver40(hours):
    b = True
    if (hours >= 40):
        b = b
    elif (hours < 40):
        b = False
    return b

def payCal(rate, hours):
    fortyPlus = isOver40(hours)
    pay = 0
    pay2 = 0
    hours2 = 0
    if (fortyPlus == True):
        pay = rate*40
        hours2 = hours-40
        nRate = rate*1.5
        pay2=nRate*hours2
        pay = pay + pay2
    elif (fortyPlus == False):
        pay = rate*hours
    return pay
    
        

rate = getRate()
hours = getHours()

print (payCal(rate,hours))
