"""
start: 04052018
Programmer: William
P7Q1_game.py

I'm going to try using Object orianted programing
1.
Be divided into functions
2.
Use appropriate data structures (lists) and appropriate internal documentation
3.
Be text menu driven (simplified using capital letters or numbers). 
4.
Ask separately for the character's first name, then last name
5.
Randomly generate a class and race
6.
Generate a random number between 5 - 20 per stat. 
a.
Character Stats: Strength, Intelligence, Wisdom, Charisma
7.
Randomly generate a weapon for the character's 'Back Slot' and 'Belt Slot'
8.
Randomly generate an item (Miscellaneous item, Magical item) per hand
9.
Randomly generate 8 items (Miscellaneous items, Magical potions, Loot, Stuff that keeps you alive, Magical 
items) for the pack.
10.
Allow the user to read from the file called character.txt to display the previous character
11.
Allow the user to create a new character and write to the file character.t

"""
import pybrary
import random

class person(object):
    def __init__(self, name, typ, race, strength, intel, wisdom, charisma, pack_list, back_slot = "Empty", belt_slot = "EMPTY", r_hand = "EMPTY", l_hand = "EMPTY" ):
        self.name = name #makes objects name
        self.typ = typ #type used instead of class because class is a reserved word
        self.race = race
        self.strength = strength
        self.intel = intel
        self.wisdom = wisdom
        self.charisma = charisma
        self.pack_list = pack_list
        self.back_slot = back_slot
        self.belt_slot = belt_slot
        self.r_hand = r_hand
        self.l_hand = l_hand
           

    #other
    def update_file(self):
        pybrary.writeArray(self.name+".txt", [self.name, self.typ, self.race, str(self.strength), str(self.intel), str(self.wisdom), str(self.charisma), str(self.pack_list), self.back_slot, self.belt_slot, self.r_hand, self.l_hand])
        

    #print out stuff

    def __str__(self):
        return "person[name= "+self.name+", class= "+ self.typ+ ", race= "+ self.race +", strength= "+str( self.strength)+ " intellegence= "+ str(self.intel) +\
               ", wisdom = "+str(self.wisdom)+", charisma= "+ str(self.charisma) + ", pack_list=" +str(self.pack_list)+", back_slot= "+self.back_slot+", belt_slot="+\
               self.belt_slot+", r_hand= "+ self.r_hand+", l_hand= " +self.l_hand+"]"
        
        
        

def make_from_file(fileName):
    array = pybrary.readFile(fileName)
    #print (array)
    player = person(array[0], array[1], array[2], array[3], array[4], array[5], array[6], array[7], array[8], array[9], array[10], array[11])
    return player

def get_first_name():
    return input("ENTER CHARECTERS FIRST NAME-->")
def get_last_name():
    return input("ENTER CHARECTERS LAST NAME-->")
def ran_wep():
    #makes random weapon
    num = random.randint(0,8)
    wep = ""
    if num == 0:
        wep = "SMALL SWORD"
    elif num == 1:
        wep = "MEDIUM SWORD"
    elif num == 2:
        wep = "LARGE SWORD"
    elif num == 3:
        wep = "SMALL AXE"
    elif num == 4:
        wep = "MEDIUM AXE"
    elif num == 5:
        wep == "LARGE AXE"
    elif num == 6:
        wep = "CROSSBOW"
    elif num == 7:
        wep = "SHORT BOW"
    elif num == 8:
        wep = "LONG BOW"
    else:
        print ("something went wrong in ran_wep")
    return wep
def ran_class():
    num = random.randint(0,4)
    typ = ""
    if num == 0:
        typ = "FIGHTER"
    elif num == 1:
        typ = "WIZARD"
    elif num == 2:
        typ = "THIEF"
    elif num == 3:
        typ = "HEALER"
    elif num == 4:
        typ = "RANGER"
    else:
        print ("SOMETHING WENT WRONG IN RAN_CLASS")
    return typ
def ran_race():
    num = random.randint(0,4)
    race = ""
    if num == 0:
        race = "HUMAN"
    elif num == 1:
        race = "ELF"
    elif num == 2:
        race = "DWARF"
    elif num == 3:
        race = "HALFLING"
    elif num == 4:
        race = "GNOME"
    else:
        print ("SOMETHING WENT WRONG IN RAN_race")
    return race
def ran_strength():
    return random.randint(5, 20)
def ran_intel():
    return random.randint(5,20)
def ran_wise():
    return random.randint(5, 20)
def ran_charis():
    return random.randint(5, 20)
        
        
        
 #name, typ, race, strength, intel, wisdom, charisma, pack_list, back_slot = "Empty", belt_slot = "EMPTY", r_hand = "EMPTY", l_hand = "EMPTY" )               

def main():
    name = get_first_name()
    name = name+" "+get_last_name()
    typ = ran_class()
    race = ran_race()
    strength = ran_strength()
    intel = ran_intel()
    wise = ran_wise()
    charisma = ran_charis()
    pack = ["stuff", "goes", "here"]
    back = ran_wep()
    belt = ran_wep()
    r = "item goes here"
    l = "item goes here"
    
    player1 = person(name, typ, race, strength, intel, wise, charisma, pack, back, belt, r, l)
    print (player1)
    player1.update_file()



if __name__ == "__main__":
    main()
