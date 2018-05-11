"""
date: 08052018 (DDMMYYYY)
programer: Willpiam
fileName: P6Q3_traffic_doyle.py
description:

Traffic survey.
  A detector on a road sends a signal every second to a computer. The computer stores the data 
like so: 1=no vehicle, 2=vehicle, 0=end of survey. Given a series of these data elements, calculate the length of
the survey, the number of vehicles, longest interval with no vehicles, average # of vehicles per minute.  
Your 
program will have to generate the data set.
  Please make sure that the data set is at least 3 minutes long.

Notes:

seconds = int(round(time.time()))
"""
import time
import pybrary
import random

def make_data():#makes data set for the rest of the program
    goes = 0
    array = []
    while (goes < 60*3):#keep doing this untill the time is up
        array.append(random.randint(1,2))
        goes = goes +1
        var = random.randint(0,60)
        if (var == 5) or (var == 7):#just a thig that makes the array length a little less predictable
            goes = goes - 1
            
    array.append(0)
    #print (array)
    return array


def sur_len(array):#returns the length of the survay
    length = len(array)-1#subtract one because the zero isn't really part of the survay
    return length

def num_vec(array):#num of vechels calculator
    num = 0
    for i  in range (0, sur_len(array)):
        if (array[i] == 2):
            num = num+1
    return num

def long_no_vec(array):#longest interval with no vechels
    mmax = 0
    cmax = 0
    for i in range (0,len(array)):
        if (array[i] == 1):
            cmax = cmax +1
        else:
            if (cmax > mmax):#                       could be edited to take a second varable which would hold a value to search for (varable would replace 1)
                mmax = cmax
                cmax = 0
            else:
                cmax = 0
    return mmax
    

def avg_vec_min(array):
    #count instances of the number 2 appering
    #len(array) -1 is the number of seconds
    #avg = count / (seconds/60)

    count = 0.0
    for i in range (0, len(array)):
        if (array[i] == 2):
            count = count +1
    var = float(len(array)/60)
    avg = count / var
    return avg

"""
calculate the length of
the survey, the number of vehicles, longest interval with no vehicles, average # of vehicles per minute.  
"""
array = make_data()
total = num_vec(array)
print ("---------------------------Results--------------------------")
print (" ")
print ("Survey Length---------------------------->", str(len(array)-1))
print ("Number of vehicles----------------------->", str(total))
print ("Longest Interval with no vehicles-------->", str(long_no_vec(array)))
print ("average Number of vechicles per minute--->", str(avg_vec_min(array)))



