"""
programmer: Willpiam
Date: 23042018
file name: P4Q3.py
Description:

Island Dice.
  In the Island Dice Roll game, the player begins with a score of 1500 shells.  The player is 
prompted for the number of shells to risk and a second prompt asks the player to choose either high or low.  
The player rolls two dice and the outcome is compared to the player’s choice of high or low.

If the dice total is
between 2 and 6 inclusive, then it is considered low.------------op 1

A total between 8 and 12 inclusive is high.---------------op 2

A total of 7 is 
neither high nor low, and the player loses the shells at risk.------------op 3

If the player has called correctly, the shells at risk 
are doubled and returned to the total shells.  For a wrong call, the player loses the shells at risk. It is up to you 
to decide where to use functions in this progra


"""
import random
def game(score):#one round of the score
    print (" ")
    print (" ")
    print (" ")
    print ("------------new round-------------")
    print (" ")
    print (" ")
    risk = how_many(score)#gets how many they want to risk but won't let them risk more than what they have
    hORl = high_or_low()
    dice = role()
    temp = dice
    print ("your first role was ", dice)
    dice = dice + role()
    temp = dice - temp
    print ("Your second role was", temp)
    print ("total: ", dice)
    #print ("dice =", dice)
    cat = what_cat(dice)#cat is for catagorie
    score = action(cat, risk, hORl, score)#increases score based on what catagorie the
    return score 

def action(cat, risk, state, pre):
    if (cat == "One") and (state == "L") :
        risk = risk*2
    elif (cat == "One") and (state == "H") :
        risk = 0 #you lose! You get nothing! Good day sir I said GOOD DAY!
    elif (cat == "Two") and (state == "L"):
        risk=0
    elif (cat == "Two") and (state == "H"):
        risk = risk * 2
    elif (cat == "Three"):
        risk = risk-2*risk #you lose
    return risk+pre
        
    
def what_cat(num):#sorts what happens based on the rolles.----------code good ------ i think
    cat = "Idfk"
    if (num <= 6) and (num >=2):
        #print ("option 1")
        cat = "One"
    elif (num <=8) and (num >= 12):
        #print ("opion 2")
        cat = "Two"
    elif (num == 7):
        #print ("option 3")
        cat = "Three"
    return cat


def how_many(lmt):#code good
    print ("how may shells do you want to put up to risk")
    print ("you may not bet more than ", lmt," shells")
    try:
        risk = int(input("please enter your bet here-------->"))#input needs to be an intager
        if (risk > lmt): #they are trying to bet more than they have
            print ("please don't enter more than ", lmt, " you will have to re do this input section")
            print (" ")
            print (" ")
            print (" ")
            print (" ")
            risk = how_many(lmt)
    except ValueError:#they entered a non int
        print (" are you stupid or something? enter an intager!")
        print (" ")
        print (" ")
        print ("Try again")
        print (" ")
        print (" ")
        risk = how_many(lmt)

    #print ("About to return risk as ", str(risk))
    return risk



def high_or_low():#code good
    breaker = "kusdgivug" #im going to use this varable to do some sketch ass code...just watch this
    try:
        print ("High or low... what's it gunna be yo?")
        print ("----------please type either 'high' or 'low'")
        state = input("input on this line---->")
        state = state.upper()#makes upper case
        state = state[0] #drops all but first letter... this way the user only has to kinda get the answer right to keep going
        if(state == "H") or (state == "L"):
            #its all good you got good input.. you should be proud
            breaker = "xdtfyuijnoknjiuvyrxecyvuhb"
        else:#this is where the really sketch code comes in
            
            breaker = int(breaker)#( ͡° ͜ʖ ͡°)

    except ValueError:
        print ("What kinda sh*t are you trying to pull?  Look its simple.. high or low..")
        print ("try again")
        print (" ")
        print (" ")
        print (" ")
        print (" ")
        
        state = high_or_low()
    
        
    

    #print ("about to return---->", state)
    return state


def role():#code good 
    dice = random.randint(1,6)
    #print (dice)
    return dice

notAtZero = True #they havent lost all their money yet
score = 1500

while (notAtZero == True):
    
    score = game(score)
    if (score == 0):
        print ("game over. You lose all your shells")
        notAtZero = False
        break
    
    print ("your new score is", str(score))
    
    cashOut = input("do you want to cash out?")
    if (cashOut[0] == "Y") or (cashOut[0] == "y"):
        print ("Okay.. you cash out with ", score)
        notAtZero = False
        break
    else:
        notAtZero = True
        print ("lets keep going then!")
    
    



