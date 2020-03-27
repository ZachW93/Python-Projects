weapons = {"Great Sword":40, "Zweilhander":10}
levels = [10, 30, 100, 500, 3000]

class Player:
    def __init__(self, name):
        
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.attack = 10
        self.gold = 40
        self.pots = 0
        self.weap = ["Rusty Sword"]
        self.curweap = ["Rusty Sword"]
        
        
    def attack(self):
        attack = self.base_attack
        if self.curweap == "Rusty Sword":
            attack += 5

        if self.curweap == "Great Sword":
            attack += 15
            
        if self.curweap == "Zweilhander":
            attack += 50

        return attack

#    def currentLevel(self):
#        lvl = len([x for x in levels if self.exp > x])
#        return lvl
#   

#class Pirate(Player):
#
#    def __init__(self, hitpoints, energy):
#        self.hp = hitpoints
#        self.nrg = energy
#        
#        
#class Time_Mage(Player):
#
#    pass
#        
#class Gunner(Player):
#
#    pass