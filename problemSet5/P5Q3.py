"""
Date: 30042018
programer: Willpiam
description: Morse code. Convert given text into Morse code
file name: P5Q3.py
"""

def morse_from_eng(var):
    var = var.upper()
    var = var.replace("A", ".-")
    var = var.replace("B", "-...")
    var = var.replace("C", "-.-.")
    var = var.replace("D", "-..")
    var = var.replace("E", ".")
    var = var.replace("F", "..-.")
    var = var.replace("G", "--.")
    var = var.replace("I", "..")
    var = var.replace("H", "....")
    var = var.replace("J", ".---")
    var = var.replace("K", "-.-")
    var = var.replace("L", ".-..")
    var = var.replace("M", "--")
    var = var.replace("N", "-.")
    var = var.replace("O", "---")
    var = var.replace("P", ".--.")
    var = var.replace("Q", "--.-")
    var = var.replace("R", ".-.")
    var = var.replace("S", "...")
    var = var.replace("T", "-")
    var = var.replace("U", "..-")
    var = var.replace("V", "...-")
    var = var.replace("W", ".--")
    var = var.replace("X", "-..-")
    var = var.replace("Y", "-.--")
    var = var.replace("Z", "--..")
    var = var.replace("1", ".----")
    var = var.replace("2", "..---")
    var = var.replace("3", "...--")
    var = var.replace("4", "....-")
    var = var.replace("5", ".....")
    var = var.replace("6", "-....")
    var = var.replace("7", "--...")
    var = var.replace("8", "---..")
    var = var.replace("9", "----.")
    var = var.replace("0", "-----")    
    return var

print (morse_from_eng("christina"))
