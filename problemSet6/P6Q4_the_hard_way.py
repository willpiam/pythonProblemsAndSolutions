"""
programer: William
date: may 9th 2018
fileName: P6Q4_the_hard_way.py
description:

Although Python provides us with many list methods (ex list.count()), it is good practice and very instructive to
think about how they are implemented. Implement a Python
function
without
 using any of the list methods
that work like the following list methods.
Create a program that you can select from a menu with the following:
a.
Print
(print the list in a nicely formatted way to the screen)
b.
Count
(count the number of times the chosen “value” is in the list)
c.
Reverse
(prints the list in reverse)
d.
Index
(returns the lowest index [location] which the chosen “value” is in the list)
e.
Insert
(inserts a value to the list in a selected location)
"""
def printer(array):#prints the list nicly
    for i in range (0, len(array)):
        num = i +1
        print (str(num)+"------"+array[i])

def counter(array, var):#counts instances of given value
    count = 0
    for i in range(0, len(array)):
        if (array[i] == var):
            count = count + 1
    return count

def reverse(array):#flips the array
    new = []
    
    for i in range (0,len(array)):#create an array with empty values
        new.append("")

    for i in range (0, len(array)):#write first thing in array to the last place in new (and so on)
        new[len(array)-(i+1)] = array[i]
    print (new)
        
def index(array, val):#returns the place in the list where val is first incountered
    for i in range (0, len(array)):
        if (array[i] == val):
            return i

def insert(array, val, loc):
    """
-------OTHER WAY--------
1.  app empty spot to array
create temp var (temp)
loop untill the users desired slot is avalable:
    put second last val into last (then fill second last with third last)
insert users val into desired location

"""
    array.append("")

    for i in range (len(array)-1, loc, -1):#if this doesn't work try len(array)-1
        array[i] = array[i-1]
    
    array[loc] = val
    print (array)

def menu():
    print ("Step 1".center(20, "-"))
    print ("1. Create your own array")
    print ("2. Use the premade array")

    val = input("enter the option code here ----->")
    val = val.strip()

    if (val != "1") and (val != "2"):
        print ("You donut! Only enter \"1\" or \"2\"")
        print ("")
        print ("Please try again...".upper())
        print ("")
        return False#will try again
    
    
job = False
while (job == False):
    job = menu()
    
menu()
array = ["job", "string", "book", "book","book", "book", "knife", "superman", "keyboard", "keys", "door", "wall", "paper"]
printer(array)
print(counter(array, "book"))
reverse(array)
print(index(array, "book"))
insert(array, "james bond" ,4)
