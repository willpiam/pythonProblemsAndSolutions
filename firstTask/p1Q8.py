"""
author:willpiam
date:feb 21 2018
description: divides amount of money into quarters dimes, nickels, and pennies

"""
num = int(input("give me a number less than or equal to 99"))

quarters = num // 25

print ("---------1/4--------")
print (quarters)

left = num - (quarters*25)

#print (left)

print ("-------------dimes-------------")
dimes = left // 10

print (dimes)

left = left -(dimes*10)

#print (left)

print ("---------------nickels--------------")

nickels = left // 5

print (nickels)

left = left - (nickels*5)

print ("-------------------pennies-------------------")
print (left)



