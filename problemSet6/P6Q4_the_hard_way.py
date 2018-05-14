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
    print (count)
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
    array = ["job", "string", "batman","book", "book","book", "book", "knife", "superman", "keyboard", "keys", "door", "wall", "paper"]
    print ("your unformatted array looks like this:", array)
    print ("")
    print ("")
    print ("""Would you like to:
                CODE    DESCRIPTION
                1----   print the array
                2----   count the number of times your value is listed
                3----   reverse the array
                4----   look for the first instance of a disired value
                5----   insert a value into a specific spot in the array""")
    
    #then add if statments!
    done = False
    while (done == False):
        cod = input("enter code here ---->")
        if (cod == "1"):
            printer(array)
           
        elif (cod == "2"):
            word = input("Enter a string you want to count:")
            counter(array, word)
            
        elif (cod == "3"):
            reverse(array)
            
        elif (cod == "4"):
            word = input("Enter a string you want to index:")
            print (index(array, word))
           
        elif (cod == "5"):
            word = input("Enter a string you want to insert:")
            try:
                num = int(input("Please enter the location you want to insert your string"))
            except:
                print ("You gave bad input Please try again")
                return False
            insert(array, word, num)
            

        keep = input("enter \"y\" to continue... anything else to exit")
        if (keep == "y") or (keep == "Y"):
            done = False
        else:
            done = True

        #then check if this is all the user wants to do. if it is then done = true
        #and they we can return true on this whole function and get out of here
    return True
    
    
    
    
job = False
while (job == False):
    job = menu()
    

"""
array = ["job", "string", "book", "book","book", "book", "knife", "superman", "keyboard", "keys", "door", "wall", "paper"]
printer(array)
print(counter(array, "book"))
reverse(array)
print(index(array, "book"))
insert(array, "james bond" ,4)
"""
