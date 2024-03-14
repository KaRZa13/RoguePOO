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

commun_sword = Weapons("Chocolate sword", 100, "Don't try to eat it, this is not real chocolate", 10, 70, "Commun", 1)
uncommun_sword = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 20, 40, "Uncommun", 1.1)
rare_sword = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 50, 35, "Rare", 1.2)
epic_sword = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 100, 25, "Epic", 1.3)
legendary_sword = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 300, 15, "Legendary", 1.4)
mythic_sword = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 5, "Mythic", 1.5)

# KNIVES

commun_knife = Weapons("Name", "Description", "Durability", "value", "drop chance", "Commun", 1)
uncommun_knife = Weapons("Name", "Description", "Durability", "value", "drop chance", "Uncommun", 1.1)
rare_knife = Weapons("Name", "Description", "Durability", "value", "drop chance", "Rare", 1.2)
epic_knife = Weapons("Name", "Description", "Durability", "value", "drop chance", "Epic", 1.3)
legendary_knife = Weapons("Name", "Description", "Durability", "value", "drop chance", "Legendary", 1.4)
mythic_knife = Weapons("Name", "Description", "Durability", "value", "drop chance", "Mythic", 1.5)

# HAMMER

cummun_hammer = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 10, 70, "Commun", 1)
uncommun_hammer = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 20, 40, "Uncommun", 1.1)
rare_hammer = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 50, 35, "Rare", 1.2)
epic_hammer = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 100, 25, "Epic", 1.3)
legendary_hammer = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 300, 15, "Legendary", 1.4)
mythic_hammer = Weapons("Name", "Description", "Durability", "value", "drop chance", "Mythic", 1.5)

# MAGE'S STICK

commun_stick = Weapons("Name", "Description", "Durability", "value", "drop chance", "Commun", 1)
uncommun_stick = Weapons("Name", "Description", "Durability", "value", "drop chance", "Uncommun", 1.1)
rare_stick = Weapons("Name", "Description", "Durability", "value", "drop chance", "Rare", 1.2)
epic_stick = Weapons("Name", "Description", "Durability", "value", "drop chance", "Epic", 1.3)
legendary_stick = Weapons("Name", "Description", "Durability", "value", "drop chance", "Legendary", 1.4)
mythic_stick = Weapons("Big Stick of DOOM", 100, "It's still a piece of shit", 666, 10, "Mythic", 1.5)

# SHIELD 

commun_shield = Armor("Name", "Description", "Durability", "value", "drop chance", "Commun", 1.5)
uncommun_shield = Armor("Name", "Description", "Durability", "value", "drop chance", "Uncommun", 1.5)
rare_shield = Armor("Name", "Description", "Durability", "value", "drop chance", "Rare", 1.5)
epic_shield = Armor("Name", "Description", "Durability", "value", "drop chance", "Epic", 1.5)
legendary_shield = Armor("Name", "Description", "Durability", "value", "drop chance", "Legendary", 1.5)
mythic_shield = Armor("Name", "Description", "Durability", "value", "drop chance", "Mythic", 1.5)

# ARMOR HELMET

commun_helmet = Armor("Name", "Description", "Durability", "value", "drop chance", "Commun", 1.5)
uncommun_helmet = Armor("Name", "Description", "Durability", "value", "drop chance", "Uncommun", 1.5)
rare_helmet = Armor("Name", "Description", "Durability", "value", "drop chance", "Rare", 1.5)
epic_helmet = Armor("Name", "Description", "Durability", "value", "drop chance", "Epic", 1.5)
legendary_helmet = Armor("Name", "Description", "Durability", "value", "drop chance", "Legendary", 1.5)
mythic_helmet = Armor("Name", "Description", "Durability", "value", "drop chance", "Mythic", 1.5)

# ARMOR CHESTPLATE

commun_chestplate = Armor("Name", "Description", "Durability", "value", "drop chance", "Commun", 1.5)
uncommun_chestplate = Armor("Name", "Description", "Durability", "value", "drop chance", "Uncommun", 1.5)
rare_chestplate = Armor("Name", "Description", "Durability", "value", "drop chance", "Rare", 1.5)
epic_chestplate = Armor("Name", "Description", "Durability", "value", "drop chance", "Epic", 1.5)
legendary_chestplate = Armor("Name", "Description", "Durability", "value", "drop chance", "Legendary", 1.5)
mythic_chestplate = Armor("Name", "Description", "Durability", "value", "drop chance", "Mythic", 1.5)

# ARMOR LEGGINGS

commun_leggings = Armor("Name", "Description", "Durability", "value", "drop chance", "Commun", 1.5)
uncommun_leggings = Armor("Name", "Description", "Durability", "value", "drop chance", "Uncommun", 1.5)
rare_leggings = Armor("Name", "Description", "Durability", "value", "drop chance", "Rare", 1.5)
epic_leggings = Armor("Name", "Description", "Durability", "value", "drop chance", "Epic", 1.5)
legendary_leggings = Armor("Name", "Description", "Durability", "value", "drop chance", "Legendary", 1.5)
mythic_leggings = Armor("Name", "Description", "Durability", "value", "drop chance", "Mythic", 1.5)

# ARMOR BOOTS

commun_boots = Armor("Name", "Description", "Durability", "value", "drop chance", "Commun", 1.5)
uncommun_boots = Armor("Name", "Description", "Durability", "value", "drop chance", "Uncommun", 1.5)
rare_boots = Armor("Name", "Description", "Durability", "value", "drop chance", "Rare", 1.5)
epic_boots = Armor("Name", "Description", "Durability", "value", "drop chance", "Epic", 1.5)
legendary_boots = Armor("Name", "Description", "Durability", "value", "drop chance", "Legendary", 1.5)
mythic_boots = Armor("Name", "Description", "Durability", "value", "drop chance", "Mythic", 1.5)

# POTIONS (HEALTH/MANA)

commun_health_potion = Potion("Basic potion", 
                              "Just a little potion", 
                              1, 
                              666, 
                              10, 
                              1, 
                              "Commun", "Health"
                              )
uncommun_health_potion = Potion("Big potion", 
                                "Not just a little potion", 
                                1, 
                                666, 
                                10, 
                                1, 
                                "Uncommun", 
                                "Health"
                                )
rare_health_potion = Potion("Really big potion", 
                            "Looks like a beer but it's not", 
                            1, 
                            666, 
                            10, 
                            1, 
                            "Rare", 
                            "Health"
                            )
epic_health_potion = Potion("Huge potion", 
                            "Too much for a potion", 
                            1, 
                            666, 
                            10, 
                            1, 
                            "Epic", 
                            "Health"
                            )
legendary_health_potion = Potion("Guargantuan potion", 
                                 "This is stupidly big", 
                                 1, 
                                 666, 
                                 10, 
                                 1, 
                                 "Legendary", 
                                 "Health"
                                 )
mythic_health_potion = Potion("DAAAAAMMMMMNNNN potion", 
                              "I can't even quantify this thing", 
                              1, 
                              666, 
                              10, 
                              1, 
                              "Mythic", 
                              "Health"
                              )

commun_mana_potion = Potion("Basic mana potion", "Same stuff but for mana", 1, 666, 10, 1.5,"Commun",  "Mana")
uncommun_mana_potion = Potion("Big mana potion", "You're using too much spells", 1, 666, 10, 1.5,"Uncommun", "Mana")
rare_mana_potion = Potion("Really big mana potion", "A really big one", 1, 666, 10, 1.5,"Rare", "Mana")
epic_mana_potion = Potion("Huge mana potion", "You don't even have this amount of mana, why ?", 1, 666, 10, 1.5,"Epic", "Mana")
legendary_mana_potion = Potion("Guargantuan mana potion", "Are you stupid ?", 1, 666, 10, 1.5, "Legendary", "Mana")
mythic_mana_potion = Potion("DAAAAAMMMMMNNNN mana potion", "You're definitely insane", 1, 666, 10, 1.5, "Mythic", "Mana")

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
        
    def hub(self):
        self.display.clear_console()
        self.display.title()
        self.display.village()


    def choose_class(self):

        name = input(" \n Choose your name : ")

        self.display.printclass()

        class_input = int(input(""))


        if class_input == 1:
            self.player =  Warrior(name, 20, 3, ATT1,ATT2)
            self.display.printchar(name,CLASS_TYPES[class_input])
        elif class_input == 2:
            self.player = Mage(name, 20, 3, ATT1,ATT2)
            self.display.printchar(name,CLASS_TYPES[class_input])
        elif class_input == 3:
            self.player = Thief(name, 20, 3, ATT1,ATT2)
            self.display.printchar(name,CLASS_TYPES[class_input])
        elif class_input == 4:
            self.player = Colossus(name, 20, 3, ATT1,ATT2)
            self.display.printchar(name,CLASS_TYPES[class_input])
        else:
            print("Entrée invalide. Veuillez choisir un numéro entre 1 et 4.")
            return self.choose_class()