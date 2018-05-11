"""


#header crap
"""
import codecs

def getOption():

    ans = str(input("Choose an option:"))
    good = False
    while (good == False):
        if (ans == "1") or (ans == "2"):
            good = True
        else:
            print ("the only acceptable answers are: 1 or 2")
            print (" ")
            print (" ")
            print (" ")
            ans = getOption()
    return ans

def firstLetter(var):
    return var[0].strip()

done = False

while (done == False):
    print ("(1) Decrypt")
    print ("(2) Encrypt")
    option = getOption()
    var = str(input("What do you want to say:"))
    if (option == "1"):
        var = codecs.encode(var, "rot_13")
    elif (option == "2"):
        var = codecs.decode(var, "rot_13")
    print (var)

    print (" ")
    print (" ")
    print (" ")
    con = str(input("Do you want to continue"))
    con = con.upper()

    if (firstLetter(con) == "Y"):
        done = False
        
    else:
        print ("#okay good bye")
        done = True
    
    
    

