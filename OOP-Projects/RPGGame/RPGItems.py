# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 17:33:14 2020

@author: Clayton
"""

class EquipableItems ():
    def __init__(self,name):
        self.name = name
    
class ConsumableItems ():
    def __init__(self,name):
        self.name = name


class Potions(ConsumableItems):
    def __init__(self, stats):
        self.stats = stats
    def usePot():
        
        

class Weapons(EquipableItems):
    def __init__(self, stats):
        self.stats = stats
    def equip():
        self.stats
    def unequip():
        self.stats
        
        
        