from inventory import Inventory
from dice import Dice
from character import Character,Enemy
from attack import Attack

ENEMY_TYPES = ["Squeletton", "Zombie", "Golem"]
ATTACK_DICE = Dice(100)
HALF = 50
THREE_QUARTERS = 75
QUARTER = 25
ATT1 = Attack("Normal attack", 6, THREE_QUARTERS, 1.25, QUARTER, "Just a normal sword strike", ATTACK_DICE)
ATT2 = Attack("Big attack", 4, HALF, 2.25, HALF, "A big attack , 50/50 either you destroy the opponent or you just miss your attack", ATTACK_DICE)


class Room:
    def __init__(self):
        self.entities = []
        self.event = None
        self.dice = Dice(100)

    def random_event(self):
        roll = self.dice.roll()
        if roll < 10:
            self.event = "Chest"
        if roll > 12:
            self.event = "Enemy"
            roll2 = self.dice.roll()
            if roll2 < 33:
                self.entities.append(Enemy(ENEMY_TYPES(0), 20, 0, 3, ATT1, ATT2,0,7))
            if roll2 < 66 and roll2 > 33:
                self.entities.append(Enemy(ENEMY_TYPES(1), 15, 0, 5, ATT1, ATT2,0,5))
            if roll > 66:
                self.entities.append(Enemy(ENEMY_TYPES(2), 25, 0, 3, ATT1, ATT2,0,6))
        else : 
            self.event = "Truc de ouf 2/100 chances"