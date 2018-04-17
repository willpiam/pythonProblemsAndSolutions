"""
Name: william 
File Name:P2Q7
Date: march 6th 2018
description:
    if there are 10 animals in a lab and enough food for 1000 animals, and
    every hour the number of animals’ doubles and enough food for
    another 4000 animals is added, determine when the population exceeds its
    food supply
"""

# my approch
# calculate the number of animals every hour
# calculate the number of food every hour (unit will be the AFU standing for animal feeding unit)
# then ill check to see if there is to many animals for the food
# if is enough food ill do the next hour

import math

anml = 10#start num of animals
food = 1000#start amount of food
count = 0#start at zero because adding one is the first thing we do

#equation is anml = 10*(math.pow(2,count))
#and food = 1000 + (4000*count)

while (anml <= food):#this is where the actaul work is done
    count = count +1
    food = 1000 + (4000*count)
    anml = 10*(math.pow(2,count))

print ("num of animals: " + str(anml))#outputing
print ("can feed: " +str(food))
print ("hours passed: " +str(count))

