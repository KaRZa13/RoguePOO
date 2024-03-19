from rich import print
from inventory import Inventory

class Character:

    def __init__(self, name, base_hp, base_mana, armor, attack1, attack2, gold=0):
        self.name = name
        self.max_hp = base_hp
        self.hp = self.max_hp
        self.max_mana = base_mana
        self.mana = self.max_mana
        self.armor = armor
        self.gold = gold
        self.attack1 = attack1
        self.attack2 = attack2
        self.inventory = Inventory()


    def __str__(self):
        return f"I am {self.name} I have {self.hp} hp and my attacks are {self.attack1.name} and {self.attack2.name}"
    
    def is_alive(self):
        return self.hp > 0
    
    def show_healthbar(self):
        print(f"[{'♥' * self.hp}{'♡' * (self.hp_max - self.hp)}] {self.hp}/{self.hp_max}hp")

    def decrease_hp(self, amount):
        self.hp -= amount - self.armor
        if self.hp < 0:
            self.hp = 0
        self.show_healthbar()

    def attack(self, target, amount):
        print(f"{target.name} has been attacked by {self.name} and took {amount} damages !")
        target.decrease_hp(amount)
        
    def increase_hp(self, amount):
        self.hp += amount

    def choose_attack(self):
        print(f"Choose between your attacks : \n \n \
        1.  [red]{self.attack1.name}[/red] : [blue]{self.attack1.description}[/blue] \n \n \
        2.  [red]{self.attack2.name}[/red] : [blue]{self.attack2.description}[/blue]")
        choice = int(input())
        if choice == 1 :
            return self.attack1
        else:
            return self.attack2 
    
    def sell_item(self, item):
        self.inventory.items.remove(item)
        self.gold += item.value

class Warrior(Character):
    def __init__(self, name, base_hp, base_mana, armor, attack1, attack2, gold=0):
        super().__init__(name, base_hp, base_mana, armor, attack1, attack2, gold=0)
        self.char_class = "Warrior"

    def attack(self, target, amount):
        return super().attack(target, amount) + 3
    
class Mage(Character):
    def __init__(self, name, base_hp, base_mana, armor, attack1, attack2, gold=0):
        super().__init__(name, base_hp, base_mana, armor, attack1, attack2, gold=0)
        self.char_class = "Mage"

    pass

class Thief(Character):
    def __init__(self, name, base_hp, base_mana, armor, attack1, attack2, gold=0):
        super().__init__(name, base_hp, base_mana, armor, attack1, attack2, gold=50)
        self.char_class = "Thief"

    def attack(self, target, amount):
        return super().attack(target, amount) + target.armor
    
class Colossus(Character):
    def __init__(self, name, base_hp, base_mana, armor, attack1, attack2, gold=0):
        super().__init__(name, base_hp, base_mana, armor, attack1, attack2, gold=0)
        self.char_class = "Colossus"

    def decrease_hp(self, amount):
        return super().decrease_hp(amount - 3)
    
class Enemy(Character):
    def __init__(self, name, base_hp, base_mana, armor, attack1, attack2, drop_chances, gold=0):
        super().__init__(name, base_hp, base_mana, armor, attack1, attack2, gold)
        self.drop_chances = drop_chances

class Boss(Character):
    def __init__(self, name, base_hp, base_mana, armor, attack1, attack2, gold=0):
        super().__init__(name, base_hp, base_mana, armor, attack1, attack2, gold)
    