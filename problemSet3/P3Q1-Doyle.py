"""
Date: 04042018
programer: william 
description: Write a program
which will decide if a number is even or odd, positive, negative or
"""
Snum = input("give me a number")

SnumEnd = Snum[-1]

#print (SnumEnd)#just for seeing whats happening

odd = ["9","7","5","3","1","0"]
finished = False

if (int(Snum) != 0):#check that its not zero
    for i in range (0,6):#there are 6 possable endings that mean its an odd number
        if (odd[i] == (SnumEnd)):#if the ending is one of the odd numbers
            print (Snum, " is odd")
            finished = True#informs another part of the code not to exicute we have found an answer
            break#"stop looping you maniac we found an answer" thats what this line says
        #print (i)#just for debugging
    if (finished == False):
        print (Snum, " is even")
    
else:#in this case it is zero
    print ("Zero is nither even nor odd")

#find out if negative

neg = Snum[0]#gets first charecter
#print (neg)#just for seeing whats going on

if (neg == "-"):#if first char is "-" its a negative number
    print ("its also a negative value!!!")
