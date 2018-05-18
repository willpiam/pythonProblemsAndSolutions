"""
start: 04052018
Programmer: William
P7Q1_game.py

I'm going to try using Object orianted programing

"""
import pybrary

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
        

    #getters

    #setters (all setters will also be responsable for updating external files)
    def set_typ(self):#updates type
        self.typ = input("PLEASE ENTER NEW CLASS HERE-->")

    def set_race(self):#change race
        self.race = input("PLEASE ENTER NEW RACE HERE-->")

    def set_strength(self):
        try:
            self.strength = int(input("ENTER NEW STRENGTH HERE-->"))
        except:
            print ("ERROR!")
            print ("Please only enter intergers for strength. Please try again")
            print ("")
            set_strength()

    def set_intel(self):
        try:
            self.intel = int(input("ENTER NEW intel HERE-->"))
        except:
            print ("ERROR!")
            print ("Please only enter intergers for intel. Please try again")
            print ("")
            set_intel()
    
    def set_wisdom(self):
        try:
            self.wisdom = int(input("ENTER NEW WISDOM HERE-->"))
        except:
            print ("ERROR!")
            print ("Please only enter intergers for wisdom. Please try again")
            print ("")
            set_wisdom()

    def add_to_pack(self, item):#i think the back should have an unlimited amount of these
        self.pack_list.append(item)

    

    #remove from pack and place in hand (check that hand is empty)

    #move from hand to pouch

    #move from hand to back

    #move from hand to belt

    #do the opposite of these things
    

    #other
    def update_file(self):
        pybrary.writeArray(self.name+".txt", [self.name, self.typ, self.race, str(self.strength), str(self.intel), str(self.wisdom), str(self.charisma), str(self.pack_list), self.back_slot, self.belt_slot, self.r_hand, self.l_hand])
        

    #print out stuff

    def __str__(self):
        return "person[name= "+self.name+", class= "+ self.typ+ ", race= "+ self.race +", strength= "+str( self.strength)+ " intellegence= "+ str(self.intel) +\
               ", wisdom = "+str(self.wisdom)+", charisma= "+ str(self.charisma) + ", pack_list=" +str(self.pack_list)+", back_slot= "+self.back_slot+", belt_slot="+\
               self.belt_slot+", r_hand= "+ self.r_hand+", l_hand= " +self.l_hand+"]"
        
        
        
class weapon(object):
    def __init__(self, name, damage = 1):#all weapns cause some damage (defult one)
        self.name = name
        self.damage = damage

    def __str__(self):
        return "weapon[name= "+self.name+", damage= "+str(self.damage)+"]"
"""
class sword(weapon):
    def __init__(self, 

"""
def make_from_file(fileName):
    array = pybrary.readFile(fileName)
    #print (array)
    player = person(array[0], array[1], array[2], array[3], array[4], array[5], array[6], array[7], array[8], array[9], array[10], array[11])
    return player

def main():
    player1 = person("William", "Programmer", "orc", 100, 100, 5, 7, ["paper","pen","iPad","pencil"], "sword", "phone")
    sword1 = weapon("sword")
    player1.add_to_pack("knifey")
    player1.update_file()#updates exturnal file
    #print (player1)
    #print (sword1)
    #print ("hello world!")
    will = make_from_file("William Doyle.txt")
    print (will)



if __name__ == "__main__":
    main()
