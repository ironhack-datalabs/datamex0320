import random
​
# Soldier
​
​
class Soldier:
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength
    def attack (self):

        return self.strength
    def receiveDamage(self,thedamage):
        self.health=self.health-thedamage
​
vikingArmy.append(int(viking))

​
# Viking
​
​
class Viking(Soldier):
    def __init__(self,name, health, strength):
        self.name=name
        self.health=health
        self.strength=strength
    def receiveDamage (self,thedamage):
        self.health=self.health-thedamage
        if self.health >= 1:
            return str(self.name) + " has received " + str(thedamage) + " points of damage"
        elif self.health == 0:
            return str(self.name) + " has died in act of combat"
    def battleCry(self):
        return "Odin Owns You All!"
​
​
​

​
# Saxon
​
​
class Saxon(Soldier):
    def __init__(self,health, strength):
        self.health=health
        self.strength=strength
    def receiveDamage (self,thedamage):
        self.health=self.health-thedamage
        if self.health >= 1:
            return "A Saxon has received " + str(thedamage) + " points of damage"
        elif self.health == 0:
            return "A Saxon has died in combat"

​
# War
​
​
class War():
    def __init__(self):
        vikingArmy=0
        saxonArmy=0

        def addViking(self,viking):
            vikingArmy+=viking
        def addSaxon(self,saxon):
            saxonArmy+=saxon
        def vikingAttack(self):
            saxran=random.choice(saxonArmy)
            saxran1=Saxon(saxran)
            strenvik=Viking()
            strenvik.strength()
            saxran1.receiveDamage(strenvik.strength())

​
​

​
​
​
​

​

Collapse
