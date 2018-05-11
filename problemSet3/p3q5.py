"""
programmer: william 
date: 12042018
file name: p3q5.py
description:


"""
import random



def getlen():#gets length
    lng = input("Please enter the track length")
    lng = checkLen(lng)#checks length variable is an actual int and is greater than or equal to 50
    return lng


def checkLen(STRING_lng):
    
    try:
        lng = int(STRING_lng)
        if (lng >= 20):
            lng = lng
        else:
            print ("length of race must be 20 or bigger")
            lng = getlen()
    except ValueError:
        print ("Please don't include any non-numeral charecters. Please remember to only input integers")
        lng = getlen()
    return int(lng)

def race(track):#where track is the user provided length of the track
    cycleCount = 0
    rDis = 0
    winner = "?"
    tDis = 0
    for i in range (0,track):
        #make the rabit move according to what cycle it is
        rDis = rDis + rabit(track, i)
        #make the turtel move according to what cycle it is
        tDis = tDis + turt()

        #check to see if they have finished the race
        if (done(rDis,tDis,track) == True):
            if (rDis > tDis):
                winner = "rabit"
                break
            elif (rDis < tDis):
                winner = "turtel"
                break
        print(" ")
        input("press enter to see the next step")
        print(" ")
        visuals(winner, rDis, tDis)
    Winner(winner)#chicken dinner
    
def Winner(winner):
    print ("And the winner is:" , winner)
    
def visuals(winner, r, t):
    print ("T" , end="")
    for i in range (0,t):
        print ("-" , end= "")
    print (" ")
    print ("R" , end="")
    for i in range (0, r):
        print ("-" , end= "")
    print (" ")
    
    

def done(r,t,tr):
    if (r >= tr) or (t >= tr):
        return True
    else:
        return False
        
def rabit(track, count):#figures out how many moves the rabit makes this cycle
    hops = 0
    if (track  >= 100) and (count < 3):
        hops = hops + 5
    elif (track <100):#short race rabit hops quickly
        hops = hops + 7
    elif (track >= 100) and (count > 3):
        hops = hops + 3
    elif (track > 100) and (track < 300) and (count < 10):
        hops = hops + 8
    elif (track > 100) and (track < 300) and (count > 10):
        hops = hops +2
    else:
        hops = hops + random.randrange(0,10)
    return hops
        
def turt():
    return 3
        

race(int(getlen()))



