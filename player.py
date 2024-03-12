from dice import Dice

class Player:

    def __init__(self, name, base_hp, base_atk, dice):
        self.name = name
        self.max_hp = base_hp
        self.base_atk = base_atk
        self.hp = self.max_hp
        self.atk = self.base_atk
        self.dice = dice

    def __str__(self):
        return f"I am {self.name} I have {self.hp} hp and {self.atk} atk"
    
    def is_alive(self):
        return self.hp > 0
    
    def show_healthbar(self):
        print(
            f"[{'♥' * self.hp}{'♡' * (self.hp_max - self.hp)}] {self.hp}/{self.hp_max}hp"
        )

    def decrease_hp(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0
        self.show_healthbar()

    def increase_hp(self, amount):
        self.hp += amount

    def compute_damages(self, roll, target):
        return self.attack_value + roll
    
    def attack(self, target):
        if self.is_alive():
            print(
                f"{self.name} [red]attack[/red] with {damages} (att: {self.attack_value} + roll: {roll})"
            )
            target.defense(damages, self)