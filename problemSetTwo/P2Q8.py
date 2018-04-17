"""
Name: william 
File Name:P2Q8
Date: march 6th 2018
description:
    Draw a triangle of * characters given the user input of how 
high the triangle is (number of rows)

NOTE: GO TO BOTTOM FOR WORKING CODE.... CODE FOR BIG COMMENT IS LEFT IN TO
SHOW MY DEVELOPMENT / LEARNNG PROSESS
"""

height = int(input("what is the height of your triangle?"))

rows = []
dots = []
dotsLen = 0
temp = ""

for i in range (0,height+1):#okay dont touch this block it seems to work... it makes all the rows full of " " spaces so that later I can add the "*" and they wil be centered... I need to remember to delete that exact number of spaces
    rows.append("")#make the spot in the list 
    dots.append("")
    
    for k in range (0,height+1):#nested loop (makes the square without the internal triangle
        rows[i-1]= (rows[i-1]+" ")#add spaces (these spaces put the tip of the triangle in the center)
        if (len(dots[i-1]) < i-1):#makes the charecters that need to be inserted where some of the squares spaces are
               dots[i-1]= (dots[i-1]+"*")
    """    
    print (rows[i-1])#testing
    print (dots[i-1])#testing
    """
    
    #take the line of spaces
    #1. get the length of the line of dots
    #2.remover that many spaces from the line (of spaces)
    #3.cut the line in half (don't bother tagging on the other half of the line
    #tag on the dots

    #1
    dotsLen = len(dots[i-1])
    
    #2
    temp = rows[i-1]
    temp = temp[:-dotsLen]

    #rows[i-1] = temp

    #print (temp)

    #3
    temp = temp[:-(len(temp))//2]
   
    temp = temp + dots[i-1]

    #print (temp)
    
"""""
--------------------THE PROBLEM-------------------------------

HOW IT IS:

    *
    **
   ***
   -has odd and even numbers

   
HOW IT SHOULD BE:

     *
    ***
   *****
   -only has odd numbers
   -new line = old line + 2

   maybe write the new program below to show how I realized the issue with my code
"""""



#okay num now holds the number of stars in each line
#example: num[0] = 1 because the first line has one star in it
#num[1] = 3  because it holds 3 stars on the second line
#this was accomplished in the following block of code
num = []
for i in range (0,height):
    num.append("")
    if (i>0):
        num[i] = num[i-1]+2
    else:#if i == 0
        num[i] = 1
  #  print (num[i])

#now I need to create the actual lines of stars
stars = []
for i in range (0,height):
    stars.append("")
    for k in range (0,num[i]):
        stars[i] = stars[i]+"*"
 #   print (stars[i])

#now I need to determine how many spaces are in each line
numSpace = []#holds the number of spaces in each line

for i in range (0,height):
    numSpace.append("")
    numSpace[i] = i
    
numSpace.reverse()


#now make the spaces
space = []
for i in range (0,height):
    space.append("")
    for k in range (0,numSpace[i]):
        space[i] = space[i]+" "
 #   print (stars[i])
#now I need to glue numSpace[i] and stars[i]


for i in range (0, height):
    stars[i] = space[i]+stars[i]
    print (stars[i])
















