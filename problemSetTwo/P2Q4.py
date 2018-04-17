"""
Name: william
File Name:P2Q4-
Date: march 5th 2018
description:
    Your teacher needs help calculating the class average.  Your application
    will ask how many students are in the class, and it will then accept that
    many number of grades, and calculate the class average
"""


num = int(input("how many people are in your class"))#gets user input

grades = []#declares a list

cGrades = int(1)#declares a varable with a value of 1 (the value is just a place holder)

for i in range (0, num):#loop gets each grade and adds it to the list
    cGrade = int(input("enter grade " + str(i+1)))#the str(i+1) has the +1 part so the user sees numbers starting at 1 instead of zero
    grades.append(cGrade)

"""
for i in range (0, num):#for debugging purposses
                 print (grades[i])
"""                
#time to find the average

gSum = 0#grades sum

for i in range (0, num):
    gSum = gSum + grades[i]
    #print (gSum)#just for testing

avg = gSum / num

print ("")
print ("-----The average-----")
print (avg)
