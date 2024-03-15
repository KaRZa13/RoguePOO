from rich import print
from display import Display
from player import *
from dice import Dice
from attack import Attack
from items import *
from inventory import *
from time import sleep

HALF = 50
THREE_QUARTERS = 75
QUARTER = 25

ATTACK_DICE = Dice(100)
ATT1 = Attack("Normal attack", 6, THREE_QUARTERS, 1.25, QUARTER, "Just a normal sword strike", ATTACK_DICE)
ATT2 = Attack("Big attack", 4, HALF, 2.25, HALF, "A big attack , 50/50 either you destroy the opponent or you just miss your attack", ATTACK_DICE)

CLASS_TYPES = [0, "Warrior", "Mage", "Thief", "Colossus"]

'''#############################################################   ITEMS   #############################################################'''

# SWORDS

common_sword = Weapons("Chocolate sword", 100, "Don't try to eat it, this is not real chocolate", 10, 70, "Common", 1)
uncommon_sword = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 20, 40, "Uncommon", 1.1)
rare_sword = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 50, 35, "Rare", 1.2)
epic_sword = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 100, 25, "Epic", 1.3)
legendary_sword = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 300, 15, "Legendary", 1.4)
mythic_sword = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 5, "Mythic", 1.5)

sword_inventory = ShopCategory()
sword_inventory.add_item(common_sword)
sword_inventory.add_item(uncommon_sword)
sword_inventory.add_item(rare_sword)
sword_inventory.add_item(epic_sword)
sword_inventory.add_item(legendary_sword)
sword_inventory.add_item(mythic_sword)

# KNIVES

common_knife = Weapons("Name", "Description", "Durability", "value", "drop chance", "Common", 1)
uncommon_knife = Weapons("Name", "Description", "Durability", "value", "drop chance", "Uncommon", 1.1)
rare_knife = Weapons("Name", "Description", "Durability", "value", "drop chance", "Rare", 1.2)
epic_knife = Weapons("Name", "Description", "Durability", "value", "drop chance", "Epic", 1.3)
legendary_knife = Weapons("Name", "Description", "Durability", "value", "drop chance", "Legendary", 1.4)
mythic_knife = Weapons("Name", "Description", "Durability", "value", "drop chance", "Mythic", 1.5)

knives_inventory = ShopCategory()
knives_inventory.add_item(common_knife)
knives_inventory.add_item(uncommon_knife)
knives_inventory.add_item(rare_knife)
knives_inventory.add_item(epic_knife)
knives_inventory.add_item(legendary_knife)
knives_inventory.add_item(mythic_knife)

# HAMMER

common_hammer = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 10, 70, "common", 1)
uncommon_hammer = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 20, 40, "Uncommon", 1.1)
rare_hammer = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 50, 35, "Rare", 1.2)
epic_hammer = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 100, 25, "Epic", 1.3)
legendary_hammer = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 300, 15, "Legendary", 1.4)
mythic_hammer = Weapons("Name", "Description", "Durability", "value", "drop chance", "Mythic", 1.5)

hammer_inventory = ShopCategory()
hammer_inventory.add_item(common_hammer)
hammer_inventory.add_item(uncommon_hammer)
hammer_inventory.add_item(rare_hammer)
hammer_inventory.add_item(epic_hammer)
hammer_inventory.add_item(legendary_hammer)
hammer_inventory.add_item(mythic_hammer)

# MAGE'S STICK

common_stick = Weapons("Name", "Description", "Durability", "value", "drop chance", "common", 1)
uncommon_stick = Weapons("Name", "Description", "Durability", "value", "drop chance", "Uncommon", 1.1)
rare_stick = Weapons("Name", "Description", "Durability", "value", "drop chance", "Rare", 1.2)
epic_stick = Weapons("Name", "Description", "Durability", "value", "drop chance", "Epic", 1.3)
legendary_stick = Weapons("Name", "Description", "Durability", "value", "drop chance", "Legendary", 1.4)
mythic_stick = Weapons("Big Stick of DOOM", 100, "It's still a piece of shit", 666, 10, "Mythic", 1.5)

stick_inventory = ShopCategory()
stick_inventory.add_item(common_stick)
stick_inventory.add_item(uncommon_stick)
stick_inventory.add_item(rare_stick)
stick_inventory.add_item(epic_stick)
stick_inventory.add_item(legendary_stick)
stick_inventory.add_item(mythic_stick)

# SHIELD 

common_shield = Armor("Name", "Description", "Durability", "value", "drop chance", "Commun", 1.5)
uncommon_shield = Armor("Name", "Description", "Durability", "value", "drop chance", "Uncommun", 1.5)
rare_shield = Armor("Name", "Description", "Durability", "value", "drop chance", "Rare", 1.5)
epic_shield = Armor("Name", "Description", "Durability", "value", "drop chance", "Epic", 1.5)
legendary_shield = Armor("Name", "Description", "Durability", "value", "drop chance", "Legendary", 1.5)
mythic_shield = Armor("Name", "Description", "Durability", "value", "drop chance", "Mythic", 1.5)

shield_inventory = ShopCategory()
shield_inventory.add_item(common_shield)
shield_inventory.add_item(uncommon_shield)
shield_inventory.add_item(rare_shield)
shield_inventory.add_item(epic_shield)
shield_inventory.add_item(legendary_shield)
shield_inventory.add_item(mythic_shield)

# ARMOR HELMET

common_helmet = Armor("Name", "Description", "Durability", "value", "drop chance", "Commun", 1.5)
uncommon_helmet = Armor("Name", "Description", "Durability", "value", "drop chance", "Uncommun", 1.5)
rare_helmet = Armor("Name", "Description", "Durability", "value", "drop chance", "Rare", 1.5)
epic_helmet = Armor("Name", "Description", "Durability", "value", "drop chance", "Epic", 1.5)
legendary_helmet = Armor("Name", "Description", "Durability", "value", "drop chance", "Legendary", 1.5)
mythic_helmet = Armor("Name", "Description", "Durability", "value", "drop chance", "Mythic", 1.5)

helmet_inventory = ShopCategory()
helmet_inventory.add_item(common_helmet)
helmet_inventory.add_item(uncommon_helmet)
helmet_inventory.add_item(rare_helmet)
helmet_inventory.add_item(epic_helmet)
helmet_inventory.add_item(legendary_helmet)
helmet_inventory.add_item(mythic_helmet)

# ARMOR CHESTPLATE

common_chestplate = Armor("Name", "Description", "Durability", "value", "drop chance", "Commun", 1.5)
uncommon_chestplate = Armor("Name", "Description", "Durability", "value", "drop chance", "Uncommun", 1.5)
rare_chestplate = Armor("Name", "Description", "Durability", "value", "drop chance", "Rare", 1.5)
epic_chestplate = Armor("Name", "Description", "Durability", "value", "drop chance", "Epic", 1.5)
legendary_chestplate = Armor("Name", "Description", "Durability", "value", "drop chance", "Legendary", 1.5)
mythic_chestplate = Armor("Name", "Description", "Durability", "value", "drop chance", "Mythic", 1.5)

chestplate_inventory = ShopCategory()
chestplate_inventory.add_item(common_chestplate)
chestplate_inventory.add_item(uncommon_chestplate)
chestplate_inventory.add_item(rare_chestplate)
chestplate_inventory.add_item(epic_chestplate)
chestplate_inventory.add_item(legendary_chestplate)
chestplate_inventory.add_item(mythic_chestplate)

# ARMOR LEGGINGS

common_leggings = Armor("Name", "Description", "Durability", "value", "drop chance", "Commun", 1.5)
uncommon_leggings = Armor("Name", "Description", "Durability", "value", "drop chance", "Uncommun", 1.5)
rare_leggings = Armor("Name", "Description", "Durability", "value", "drop chance", "Rare", 1.5)
epic_leggings = Armor("Name", "Description", "Durability", "value", "drop chance", "Epic", 1.5)
legendary_leggings = Armor("Name", "Description", "Durability", "value", "drop chance", "Legendary", 1.5)
mythic_leggings = Armor("Name", "Description", "Durability", "value", "drop chance", "Mythic", 1.5)

leggings_inventory = ShopCategory()
leggings_inventory.add_item(common_leggings)
leggings_inventory.add_item(uncommon_leggings)
leggings_inventory.add_item(rare_leggings)
leggings_inventory.add_item(epic_leggings)
leggings_inventory.add_item(legendary_leggings)
leggings_inventory.add_item(mythic_leggings)
# ARMOR BOOTS

common_boots = Armor("Name", "Description", "Durability", "value", "drop chance", "Commun", 1.5)
uncommon_boots = Armor("Name", "Description", "Durability", "value", "drop chance", "Uncommun", 1.5)
rare_boots = Armor("Name", "Description", "Durability", "value", "drop chance", "Rare", 1.5)
epic_boots = Armor("Name", "Description", "Durability", "value", "drop chance", "Epic", 1.5)
legendary_boots = Armor("Name", "Description", "Durability", "value", "drop chance", "Legendary", 1.5)
mythic_boots = Armor("Name", "Description", "Durability", "value", "drop chance", "Mythic", 1.5)

boots_inventory = ShopCategory()
boots_inventory.add_item(common_boots)
boots_inventory.add_item(uncommon_boots)
boots_inventory.add_item(rare_boots)
boots_inventory.add_item(epic_boots)
boots_inventory.add_item(legendary_boots)
boots_inventory.add_item(mythic_boots)

# POTIONS (HEALTH/MANA)

common_health_potion = Potion("Basic potion", "Just a little potion", 1, 666, 10, 1, "Commun", "Health")
uncommon_health_potion = Potion("Big potion", "Not just a little potion", 1, 666, 10, 1, "Uncommun", "Health")
rare_health_potion = Potion("Really big potion", "Looks like a beer but it's not", 1, 666, 10, 1, "Rare", "Health")
epic_health_potion = Potion("Huge potion", "Too much for a potion", 1, 666, 10, 1, "Epic", "Health")
legendary_health_potion = Potion("Guargantuan potion", "This is stupidly big", 1, 666, 10, 1, "Legendary", "Health")
mythic_health_potion = Potion("DAAAAAMMMMMNNNN potion", "I can't even quantify this thing", 1, 666, 10, 1, "Mythic", "Health")

health_pot_inventory = ShopCategory()
health_pot_inventory.add_item(common_health_potion)
health_pot_inventory.add_item(uncommon_health_potion)
health_pot_inventory.add_item(rare_health_potion)
health_pot_inventory.add_item(epic_health_potion)
health_pot_inventory.add_item(legendary_health_potion)
health_pot_inventory.add_item(mythic_health_potion)

common_mana_potion = Potion("Basic mana potion", "Same stuff but for mana", 1, 666, 10, 1.5,"Commun",  "Mana")
uncommon_mana_potion = Potion("Big mana potion", "You're using too much spells", 1, 666, 10, 1.5,"Uncommun", "Mana")
rare_mana_potion = Potion("Really big mana potion", "Do you eat mana ?", 1, 666, 10, 1.5,"Rare", "Mana")
epic_mana_potion = Potion("Huge mana potion", "You don't even have this amount of mana, why ?", 1, 666, 10, 1.5,"Epic", "Mana")
legendary_mana_potion = Potion("Guargantuan mana potion", "Are you stupid ?", 1, 666, 10, 1.5, "Legendary", "Mana")
mythic_mana_potion = Potion("DAAAAAMMMMMNNNN mana potion", "You're definitely insane", 1, 666, 10, 1.5, "Mythic", "Mana")

mana_pot_inventory = ShopCategory()
mana_pot_inventory.add_item(common_mana_potion)
mana_pot_inventory.add_item(uncommon_mana_potion)
mana_pot_inventory.add_item(rare_mana_potion)
mana_pot_inventory.add_item(epic_mana_potion)
mana_pot_inventory.add_item(legendary_mana_potion)
mana_pot_inventory.add_item(mythic_mana_potion)

class Game:
    def __init__(self):
        self.player = None
        self.playercolor = None
        self.enemies = []
        self.display = Display()

    def start(self):
        self.display.clear_console()
        self.display.title()
        self.display.menu()
        if self.player == None:
            self.choose_class()
        
    def hub(self):
        self.display.clear_console()
        self.display.title()
        self.display.village()
        print(f"[{self.playercolor}]{self.player.name}[/{self.playercolor}] : {self.player.hp}/{self.player.max_hp} [red]HP[/red] - {self.player.gold} [yellow]Gold[/yellow] \n \n ")
        self.display.printhub()
        hub_choice = int(input(""))
        self.hubdecision(hub_choice)

    def hubdecision(self,choice):
        if choice == 1:
            self.inventory()
        if choice == 2:
            self.categories()

    def inventorydecision(self,choice):
        if choice == 1:
            self.hub()
        if choice == 2:
            self.hubdecision(1)
    
    def categories(self):
        self.display.clear_console()
        self.display.title()
        self.display.shop()
        print(f"[{self.playercolor}]{self.player.name}[/{self.playercolor}] : {self.player.hp}/{self.player.max_hp} [red]HP[/red] - {self.player.gold} [yellow]Gold[/yellow] \n \n ")
        self.display.shopcategories()
        category_choice = int(input(""))
        self.shopcategoriesdecision(category_choice)

    def inventory(self):
        self.display.clear_console()
        self.display.title()
        self.display.inventory()
        print(f"[{self.playercolor}]{self.player.name}[/{self.playercolor}] : {self.player.hp}/{self.player.max_hp} [red]HP[/red] - {self.player.gold} [yellow]Gold[/yellow] \n \n ")
        self.player.inventory.display_inventory()
        self.display.quitinventory()
        inventory_choice = int(input(""))
        self.inventorydecision(inventory_choice)


    def shopcategoriesdecision(self,choice):
        if choice == 1:
            self.display.clear_console()
            self.display.title()
            self.display.swords()

            sword_inventory.display_inventory()
            buy_choice = int(input(""))
            if buy_choice == 7:
                self.categories()
            else:
                self.buydecision(sword_inventory.items[(buy_choice - 1)])

        if choice == 2:
            self.display.clear_console()
            self.display.title()
            self.display.knives()

            knives_inventory.display_inventory()
            buy_choice = int(input(""))
            if buy_choice == 7:
                self.categories()
            else:
                self.buydecision(knives_inventory.items[(buy_choice - 1)])
        if choice == 3:
            self.display.clear_console()
            self.display.title()
            self.display.hammers()

            hammer_inventory.display_inventory()
            buy_choice = int(input(""))
            if buy_choice == 7:
                self.categories()
            else:
                self.buydecision(hammer_inventory.items[(buy_choice - 1)])
        if choice == 4:
            self.display.clear_console()
            self.display.title()
            self.display.sticks()

            stick_inventory.display_inventory()
            buy_choice = int(input(""))
            if buy_choice == 7:
                self.categories()
            else:
                self.buydecision(stick_inventory.items[(buy_choice - 1)])
        if choice == 5:
            self.display.clear_console()
            self.display.title()
            self.display.shields()

            shield_inventory.display_inventory()
            buy_choice = int(input(""))
            if buy_choice == 7:
                self.categories()
            else:
                self.buydecision(shield_inventory.items[(buy_choice - 1)])
        if choice == 6:
            self.display.clear_console()
            self.display.title()
            self.display.helmets()

            helmet_inventory.display_inventory()
            buy_choice = int(input(""))
            if buy_choice == 7:
                self.categories()
            else:
                self.buydecision(helmet_inventory.items[(buy_choice - 1)])
        if choice == 7:
            self.display.clear_console()
            self.display.title()
            self.display.chestplates()

            chestplate_inventory.display_inventory()
            buy_choice = int(input(""))
            if buy_choice == 7:
                self.categories()
            else:
                self.buydecision(chestplate_inventory.items[(buy_choice - 1)])
        if choice == 8:
            self.display.clear_console()
            self.display.title()
            self.display.leggings()

            leggings_inventory.display_inventory()
            buy_choice = int(input(""))
            if buy_choice == 7:
                self.categories()
            else:
                self.buydecision(leggings_inventory.items[(buy_choice - 1)])
        if choice == 9:
            self.display.clear_console()
            self.display.title()
            self.display.boots()

            boots_inventory.display_inventory()
            buy_choice = int(input(""))
            if buy_choice == 7:
                self.categories()
            else:
                self.buydecision(boots_inventory.items[(buy_choice - 1)])
        if choice == 10:
            pass
        if choice == 11:
            self.hub()

    def buydecision(self, item):
        if self.player.gold >= item.value:
            self.player.inventory.add_item(item)
            self.player.gold -= item.value
            self.inventory()
        else:
            self.display.cantafford()
            sleep(2)
            self.categories()


    def choose_class(self):

        name = input(" \n Choose your name : ")

        self.display.printclass()

        class_input = int(input(""))


        if class_input == 1:
            self.player =  Warrior(name, 20, 0, 3, ATT1,ATT2)
            self.playercolor = "red"
        elif class_input == 2:
            self.player = Mage(name, 20, 20, 3, ATT1,ATT2)
            self.playercolor = "blue"
        elif class_input == 3:
            self.player = Thief(name, 20, 0, 3, ATT1,ATT2, 10)
            self.playercolor = "green"
        elif class_input == 4:
            self.player = Colossus(name, 20, 0, 3, ATT1,ATT2)
            self.playercolor = "yellow"
        else:
            print("Entrée invalide. Veuillez choisir un numéro entre 1 et 4.")
            return self.choose_class()