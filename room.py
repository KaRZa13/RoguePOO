from dice import Dice
from character import Enemy, Boss
from attack import Attack

BOSS_TYPES = ["Demon", "Drake"]
ENEMY_TYPES = ["Skeleton", "Zombie", "Goblin"]
ATTACK_DICE = Dice(100)
HALF = 50
THREE_QUARTERS = 75
QUARTER = 25
ATT1 = Attack("Normal attack", 6, THREE_QUARTERS, 1.25, QUARTER, "Just a normal sword strike", ATTACK_DICE)
ATT2 = Attack("Big attack", 4, HALF, 2.25, HALF, "A big attack , 50/50 either you destroy the opponent or you just miss your attack", ATTACK_DICE)


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
                self.entity = Enemy(ENEMY_TYPES[0], 20, 0, 3, ATT1, ATT2, 70)
                self.enemy = "skeleton"
            if roll2 > 33 or roll2 <= 66:
                self.entity = Enemy(ENEMY_TYPES[1], 15, 0, 5, ATT1, ATT2, 60)
                self.enemy = "zombie"
            if roll2 > 66:
                self.entity = Enemy(ENEMY_TYPES[2], 25, 0, 3, ATT1, ATT2, 65)
                self.enemy = "goblin"
        else : 
            self.event = "chest"
            self.entity = self.game.create_chest()
    
    def reset_entities(self):
        self.entity = None

    def boss(self):
        roll = self.dice.roll()
        self.event = "boss"
        if roll <= 49:
            self.entity = Boss(BOSS_TYPES[0], 50, 0, 10, ATT1, ATT2, 100)
        else:
            self.entity = Boss(BOSS_TYPES[1], 55, 0, 9, ATT1, ATT2, 100)
