from rich import print
from inventory import Inventory

class Character:

    def __init__(self, name, base_hp, armor, attack1, attack2, gold=0):
        self.name = name
        self.max_hp = base_hp
        self.hp = self.max_hp
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
        self.hp -= amount
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