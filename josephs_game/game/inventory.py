class Item:
    def __init__(self, id, name, description, interactions):
        self.id = id
        self.name = name
        self.description = description
        self.interactions = interactions


class Weapon(Item):
    def __init__(self, id, name, description, interactions, damage, speed):
        super().__init__(id, name, description, interactions)
        self.damage = damage
        self.speed = speed
        
    def attack(self, target):
        target.health -= self.damage
        print(f"{self.name} attacks {target.name} for {self.damage} damage")
    
class Armor(Item):
    def __init__(self, id, name, description, interactions, defense):
        super().__init__(id, name, description, interactions)
        self.defense = defense