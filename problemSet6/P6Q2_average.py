"""
programer: Willpiam
Date:03052018
description:

simple program asks for 4 numbers or "class averages" and finds the average of
of the list containing the data.

written to the tune of nirvana

message:
    In the IDLE I alone am god.

"""

import pybrary #always usefull
import time #for memes



def getNums(times):
    array = []
    time.sleep(0.07)
    print ("All averages must only be numbers. Decimals ARE okay.")
    time.sleep(0.1765)
    for i in range (0, times):
        if (i == 0):
            array.append(str(input("Please enter a grade average")))
        else:
            array.append(str(input("Please enter another grade average")))
    return array

def avg(array):
    try:
        nums = []
        for i in range (0,len(array)):
            nums.append(int(array[i]))
        num = sum(nums)#handy little trick...
        avag = num / len(nums)
        return avag
    except:
        print ("Something went wrong in avg or pybrary.avg")
        
array = getNums(4)#gets 4 nums
average = avg(array)#may add avg function to pybrary
print ("The avarage is: "+str(average)+"%")

