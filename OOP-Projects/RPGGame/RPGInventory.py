import os
from RPGClasses import Player

def inventory(player):
    
    playerhere = True;
    
    while playerhere == True:

        os.system('clear')
        print("what do you want to do?")
        print("1.) Equip Weapon")
        print("b.) go back")
        option = input(">>> ")
        if option == "1":
            equip(player)
        elif option == 'b':
            playerhere = False

def equip(PlayerIG):
        os.system('clear')
        print("What do you want to equip?")
        for weapon in PlayerIG.weap:
            print(weapon)
        print("b to go back")
        option = input(">>> ")
        if option == PlayerIG.curweap:
            print("You already have that weapon equipped")
            option = input(" ")
            equip()
        elif option == "b":
            inventory()
        elif option in PlayerIG.weap:
            PlayerIG.curweap = option
            print("You have equipped %s." % option)
            option = input(" ")
            equip()
        else:
            print("You don't have %s in your inventory" % option)