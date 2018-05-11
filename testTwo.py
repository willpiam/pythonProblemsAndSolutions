"""
programer: William 
Date: 18042018
filename: testTwo.py
description: Program will take user input (a number) and print out a list of all
its devisors.  if there are no devisors it will inform the user that the input number
is prim. As of yet I have no clue how im going to do this...

hey! I figured it out!

"""
def getInput():#gets input (int) will not break if given bad input
    done = False
    while (done == False):#by having the try and except in a while true loop i don't need to call any other functions to restart. Keep it stupid simple
        try:
            num = input("Please enter a number:")#gets input
            intNum = int(num)#checks input is int
            done = True#we can now leave the while loo[
        except ValueError:#bad iput
            print ("Don't try and hurt me.  I'm trying to help you find prime numbers. Don't you want to find prime numbers? Right. So please only input integers.")
    return intNum#will only return value when it knows the value is good
            

def checkINT(value):#checks a value is a whole number
    whole = True
    
    
    val = int(value)
    if (value == val):#it turns out the int(value) action can cut of all decimals
        val = val #think i have to do something
    else:
        whole = False
    
    
    return whole

    


def printDivs(num):
    Prime = True
    hold = 0.0
    for i in range (2, num):
        hold = num/i#better than doing the math within the if statment
        if (checkINT(hold) == True):
            print (i)
            Prime = False
    if (Prime == True):
        print ("You entered a prime number")
            
        
#print (checkINT(1.5))  
    
    
num = getInput()
if (num <= 1):
    print ("Number is not worth checking. Please enter a positive value greater than 1")#used to say (when handed in)this is not a prime number. Its not even either
else:


    printDivs(num)
