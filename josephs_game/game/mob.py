class Mob:
    def __init__(self, name, health, damage, defense, speed):
        self.name = name
        self.health = health
        self.damage = damage
        self.defense = defense
        self.speed = speed
        
    def attack(self, target):
        target.health -= self.attack
        print(f"{self.name} attacks {target.name} for {self.damage} damage")