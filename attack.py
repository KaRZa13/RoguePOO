class Attack:

    def __init__(self, name, damages, crit_chances, crit_multiplier, miss_chances, description, dice) -> None:
        self.name = name
        self.damages = damages
        self.crit_chaces = crit_chances
        self.miss_chaces = miss_chances
        self.crit_multiplier = crit_multiplier
        self.description = description
        self.dice = dice

    def calculate_damages(self,player):
        mult = 1
        roll = self.dice.roll()
        for item in player.inventory.items:
            if item.type == "Weapon":
                mult = item.attack_modifier
        if roll > self.crit_chaces:
            return self.damages * self.crit_multiplier * mult
        elif roll < self.miss_chaces:
            return 0
        else:
            return self.damages * mult

    