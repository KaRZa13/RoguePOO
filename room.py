from dice import Dice
from character import Enemy, Boss
from init import *

BOSS_TYPES = ["Demon", "Drake"]
ENEMY_TYPES = ["Skeleton", "Zombie", "Goblin"]

class Room:
    def __init__(self, game):
        self.entity = None
        self.event = None
        self.enemy = None
        self.dice = Dice(100)
        self.game = game

    def random_event(self):
        roll = self.dice.roll()
        if roll <= 10:
            self.event = "chest"
            self.entity = self.game.create_chest()
        if roll > 12:
            self.event = "enemy"
            roll2 = self.dice.roll()
            if roll2 <= 33:
                self.entity = Enemy(ENEMY_TYPES[0], 20, 3, all_attacks["attack1"], all_attacks["attack2"], 70)
                self.enemy = "skeleton"
            if roll2 > 33 or roll2 <= 66:
                self.entity = Enemy(ENEMY_TYPES[1], 15, 5, all_attacks["attack1"], all_attacks["attack2"], 60)
                self.enemy = "zombie"
            if roll2 > 66:
                self.entity = Enemy(ENEMY_TYPES[2], 25, 3, all_attacks["attack1"], all_attacks["attack2"], 65)
                self.enemy = "goblin"
        else : 
            self.event = "chest"
            self.entity = self.game.create_chest()
    
    def reset_entities(self):
        self.entity = None

    def boss(self):
        self.event = "boss"
        roll = self.dice.roll()
        if roll <= 49:
            self.entity = Boss(BOSS_TYPES[0], 50, 10, all_attacks["attack1"], all_attacks["attack2"], 100)
        else:
            self.entity = Boss(BOSS_TYPES[1], 55, 9, all_attacks["attack1"], all_attacks["attack2"], 100)
