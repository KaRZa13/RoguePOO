from rich import print
from display import Display
from player import *
from dice import Dice
from attack import Attack
from items import *

HALF = 50
THREE_QUARTERS = 75
QUARTER = 25

ATTACK_DICE = Dice(100)
ATT1 = Attack("Normal attack", 6, THREE_QUARTERS, 1.25, QUARTER, "Just a normal sword strike", ATTACK_DICE)
ATT2 = Attack("Big attack", 4, HALF, 2.25, HALF, "A big attack , 50/50 either you destroy the opponent or you just miss your attack", ATTACK_DICE)

CLASS_TYPES = [0, "Warrior", "Mage", "Thief", "Colossus"]

'''#############################################################   ITEMS   #############################################################'''

# SWORDS

commun_sword = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Commun", 1.5)
uncommun_sword = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Uncommun", 1.5)
rare_sword = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Rare", 1.5)
epic_sword = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Epic", 1.5)
legendary_sword = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Legendary", 1.5)
mythic_sword = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Mythic", 1.5)

# KNIVES

commun_knife = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Commun", 1.5)
uncommun_knife = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Uncommun", 1.5)
rare_knife = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Rare", 1.5)
epic_knife = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Epic", 1.5)
legendary_knife = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Legendary", 1.5)
mythic_knife = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Mythic", 1.5)

# HAMMER

cummun_hammer = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Commun", 1.5)
uncommun_hammer = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Commun", 1.5)
rare_hammer = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Commun", 1.5)
epic_hammer = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Commun", 1.5)
legendary_hammer = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Commun", 1.5)
mythic_hammer = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Commun", 1.5)

# MAGE'S STICK

commun_stick = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Commun", 1.5)
uncommun_stick = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Uncommun", 1.5)
rare_stick = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Rare", 1.5)
epic_stick = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Epic", 1.5)
legendary_stick = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Legendary", 1.5)
mythic_stick = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Mythic", 1.5)

# ARMOR HELMET

commun_helmet = Armor("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Commun", 1.5)
uncommun_helmet = Armor("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Commun", 1.5)
rare_helmet = Armor("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Commun", 1.5)
epic_helmet = Armor("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Commun", 1.5)
legendary_helmet = Armor("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Commun", 1.5)
mythic_helmet = Armor("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Commun", 1.5)

# ARMOR CHESTPLATE

commun_chestplate = Armor("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Commun", 1.5)
uncommun_chestplate = Armor("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Commun", 1.5)
rare_chestplate = Armor("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Commun", 1.5)
epic_chestplate = Armor("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Commun", 1.5)
legendary_chestplate = Armor("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Commun", 1.5)
mythic_chestplate = Armor("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Commun", 1.5)

# ARMOR LEGGINGS

commun_leggings = Armor("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Commun", 1.5)
uncommun_leggings = Armor("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Commun", 1.5)
rare_leggings = Armor("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Commun", 1.5)
epic_leggings = Armor("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Commun", 1.5)
legendary_leggings = Armor("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Commun", 1.5)
mythic_leggings = Armor("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Commun", 1.5)

# ARMOR BOOTS

commun_boots = Armor("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Commun", 1.5)
uncommun_boots = Armor("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Commun", 1.5)
rare_boots = Armor("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Commun", 1.5)
epic_boots = Armor("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Commun", 1.5)
legendary_boots = Armor("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Commun", 1.5)
mythic_boots = Armor("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Commun", 1.5)

# POTIONS

health_potion = Potion("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Commun", 1.5,2)
mana_potion = Potion("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Commun", 1.5,2)

class Game:
    def __init__(self):
        self.player = None
        self.enemies = []
        self.display = Display()

    def start(self):
        self.display.clear_console()
        self.display.title()
        self.display.menu()
        if self.player == None:
            self.player = self.choose_class()


    def choose_class(self):

        name = input(" \n Choose your name : ")

        self.display.printclass()

        class_input = int(input(""))


        if class_input == 1:
            self.player =  Warrior(name, 20, 3, ATT1,ATT2)
        elif class_input == 2:
            self.player = Mage(name, 20, 3, ATT1,ATT2)
        elif class_input == 3:
            self.player = Thief(name, 20, 3, ATT1,ATT2)
        elif class_input == 4:
            self.player = Colossus(name, 20, 3, ATT1,ATT2)
        else:
            print("Entrée invalide. Veuillez choisir un numéro entre 1 et 4.")
            return self.choose_class()
        
        self.display.printchar(name,CLASS_TYPES[class_input])