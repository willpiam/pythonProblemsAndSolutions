"""
Programmer: Willpiam
date:17042018
file name: P4Q2.py
description:

-------------the problem--------------
Define a function called hotel_cost with one argument nights as input. The hotel costs $179 per night. So, the 
function hotel_cost should return 179 * nights. Return the cost of the hotel cost.
Define a function called plane_ride_cost that takes a string, city, as input. The function should return a 
different price depending on the location. Below are the valid destinations and their corresponding round-trip 
prices. Return the cost of the trip.

"Toronto": 250

"Ottawa": 270

"Calgary": 400

"Vancouver": 525
Create a function called rental_car_cost with an argument called days. Calculate the cost of renting the car: 
Every day you rent the car costs $59. If you rent the car for 7 or more days, you get $100 off your total. 
Alternatively, if you rent the car for 3 or more days, you get $30 off your total. You 
cannot
 get both discounts. 
Return the cost of the rental car.
Define a function called trip_cost that takes two arguments, city and days. Have your function return the sum 
of calling the rental_car_cost(days), hotel_cost(days), and plane_ride_cost(city) functions.
Ask the user for which city they are going to and for how many days. Output the result in a nicely formatted 
manner


"""

def hotel_cost(nights):#to fix: needs to recover from non integers better
    cost = 0
    try:
        cost = 179*nights
    except ValueError:
        print ("Please only input integers. Its people like you that make my life hard.")
        #something should be done here to recover the program...
    return int(cost)

def plane_ride_cost(city):
    cost = 0
    try:
        city = city.upper()
        city = city[0]
        if (city == "T"):
            cost = 250
        elif (city == "O"):
            cost = 270
        elif (city == "C"):
            cost = 400
        elif (city == "V"):
            cost = 525
    except ValueError:
        print ("only toronto, ottawa, calgary, and vancover are acceptable inputs")
    return int(cost)

def rental_car_cost(days):
    iday = int(days)
    price = iday*59
    if (iday >= 7):
        price = price -100
    elif (iday >=3) and (iday < 7):
        price = price -30
    return int(price)

def trip_cost(days, city):
    carCost = rental_car_cost(days)
    hCost = hotel_cost(int(days))
    pCost = plane_ride_cost(city)
    price= hCost + pCost + carCost
    return price

def checkINT(value):#checks a value is a whole number
    whole = True
    
    try:
        val = int(value)
        whole = False
    except ValueError:
        whole = True
        print ("please enter a good value")
    return whole



x = True
while (x==True):
    days = input("How many days will you be gone.")
    print (" ")
    city = input("what city are you going to?")
    
    x = checkINT(days)
    print ("great")

price = trip_cost(days, city)

print ("$ ",price, " is what you can expect to pay")




