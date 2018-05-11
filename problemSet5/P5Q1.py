"""
date: 25042018
programer: William
description:

convert a date in the form MMDDYYYY into MONTH DAY YE


"""



def sortMonth(number):#figures out the name of the month based on the number of the monuth
    try:
        mon = " "#creates mon var to hold the month
        num = int(number)
        if (num == 1):
            mon = "January"
        elif (num == 2):
            mon = "Febuary"
        elif (num == 3):
            mon = "march"
        elif (num == 4):
            mon = "April"
        elif (num == 5):
            mon = "May"
        elif (num == 6):
            mon = "June"
        elif (num == 7):
            mon = "July"
        elif (num == 8):
            mon = "August"
        elif (num == 9):
            mon = "September"
        elif (num == 10):
            mon = "October"
        elif (num == 11):
            mon = "November"
        elif (num == 12):
            mon = "December"
    except:
        print ("something went wrong in the sortMonth function.")
    return mon
        

def getDate():
    array = []
    date = str(input("please enter the date (MMDDYYYY):"))
    month = date[:2]#gets car in spot zero and one
    #print (month)
    day = date[2:4]
    #print (day)
    year = date[-4:]
    #print (year)
    array.append(month)
    array.append(day)
    array.append(year)

    if (int(month) <0):
        print ("you gave bad input. Please try again")
        array = getDate()
    elif(int(month) >= 13):
        print ("you gave bad input. Please try again")
        array = getDate()
    elif (int(day) <= 0):
        print ("you gave bad input. Please try again")
        array = getDate()
    return array



array = getDate()
month = array[0]
day = array[1]
year = array[2]

month = sortMonth(month)

print (month," ",day," ",year)
