"""
author: willpiam
date: feb 28th 2018
description: converts faherenhight to celcious
"""
import math

sF = input("enter a temperature in farenhight")#gets fharenhight as a string

fF = float(sF)# makes float version

fC = ((5/9)*(fF - 32.0)) #converts to celcious

sC = str(fC)

print ("your temprature in a proper measuring unit is :"+ sC)
