"""
WE GUNNA USE FUNCTIONS LIKE REALLLLL MEN
WILLIAM 
04042018
description: determines if a year is a leep year or not
"""



#functions and other stuff

def one(year):#funcion
    if (int(year) % 4 == 0):
        two(year)
    else:
        five()

def two(year):
    if (int(year) % 100 == 0):
        three(year)
    else:
        four()

def three(year):
    if (int(year) % 400 == 0):
        four()
    else:
        five()

def four():#call when we know its a leep year
    print ("its a leap year")

def five():#call when we know its not a leep year
    print ("its not a leap year")


def poorInput(stng):
    itgr = 0 
    try:
        itgr = int(stng)
    except:
        print ("please only enter integers")
        print ("TRY AGAIN")
        print (" ")
        itgr = main()
    return str(itgr)

#-------------top code--------
def main():
    year = input("enter a year")
    year = poorInput(year)
    one(year)
    return year

main()

"""
Ive lernt to do something with thi problem set im just not sure how im actaully doing
between poorInput and main something is happening.  Its looping untill it gets a good answer.
This is weird and I want to get better at pulling off this "trick"

"""
