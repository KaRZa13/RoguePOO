from dice import Dice

class Attack:

    def __init__(self, name, damages, crit_chances, crit_multiplier, miss_chances, description, dice) -> None:
        self.name = name
        self.damages = damages
        self.crit_chaces = crit_chances
        self.miss_chaces = miss_chances
        self.crit_multiplier = crit_multiplier
        self.description = description
        self.dice = dice

    def calculate_damages(self):
        roll = self.dice.roll()
        if roll > self.crit_chaces:
            return self.damages * self.crit_multiplier, "Incredible attack !"
        elif roll < self.miss_chaces:
            return 0, "Attack missed the target"
        else:
            return self.damages, "Good one !"

    