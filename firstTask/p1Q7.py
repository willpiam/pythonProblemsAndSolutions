"""
author:willpiam
date:feb 21 2018
description: divides numbers into hundrads, tens, and ones

"""
num = str(input("give me a 3 digit number"))

ones = num[-1:]

print (ones)

tens = num[-2:]
#print (tens)
tens = tens[:-1]
print (tens+"0")

hundrads = num[:1]
print (hundrads+"00")

