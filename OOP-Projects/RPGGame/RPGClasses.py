class Player:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.base_attack = 10
        self.gold = 40
        self.pots = 0
        self.weap = ["Rusty Sword"]
        self.curweap = ["Rusty Sword"]

class Pirate(Player):

    def __init__(self, hitpoints, energy):
        self.hp = hitpoints
        self.nrg = energy
        
        
class Time_Mage(Player):

    def __init__(self, hitpoints, mana):
        self.hp = hitpoints
        self.mana = mana
        
class Gunner(Player):

    def __init__(self, hitpoints, energy):
        self.hp = hitpoints
        self.nrg = energy