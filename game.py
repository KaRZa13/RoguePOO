from rich import print
from display import Display
from character import *
from dice import Dice
from attack import Attack
from items import *
from inventory import *
from room import Room
from time import sleep
import random

HALF = 50
THREE_QUARTERS = 75
QUARTER = 25

ATTACK_DICE = Dice(100)
ATT1 = Attack("Normal attack", 6, THREE_QUARTERS, 1.25, QUARTER, "Just a normal sword strike", ATTACK_DICE)
ATT2 = Attack("Big attack", 4, HALF, 2.25, HALF, "A big attack , 50/50 either you destroy the opponent or you just miss your attack", ATTACK_DICE)

CLASS_TYPES = [0, "Warrior", "Mage", "Thief", "Colossus"]

'''#############################################################   ITEMS   #############################################################'''

DURABILITY_WEAPONS = [25, 50, 100, 200, 500, 666]
DURABILITY_ARMOR = []
DAMAGE_MODIFIER = [1, 1.1, 1.2, 1.3, 1.4, 1.5]
ARMOR_MODIFIER = []
VALUE_WEAPONS = []
RARITY_PROBABILITIES = [0.50, 0.25, 0.15, 0.07, 0.02, 0.01]
rarity_names = {0: 'common',1: 'uncommon',2: 'rare',3: 'epic',4: 'legendary',5: 'mythic'}

# SWORDS

common_sword = Weapons("Chocolate sword", "Don't try to eat it, this is not real chocolate... It's not even a real sword", DURABILITY_WEAPONS[0], 15, 70, "Common", DAMAGE_MODIFIER[0], "Warrior")
uncommon_sword = Weapons("Simple sword", "Just a piece of forged iron", DURABILITY_WEAPONS[1], 30, 40, "Uncommon", DAMAGE_MODIFIER[1], "Warrior")
rare_sword = Weapons("Knight sword", "Finally a good weapon", DURABILITY_WEAPONS[2], 75, 35, "Rare", DAMAGE_MODIFIER[2], "Warrior")
epic_sword = Weapons("Claymore", "Big sword for big damage !", DURABILITY_WEAPONS[3], 150, 25, "Epic", DAMAGE_MODIFIER[3], "Warrior")
legendary_sword = Weapons("Excalibur", "More than just a sword ", DURABILITY_WEAPONS[4], 500, 15, "Legendary", DAMAGE_MODIFIER[4], "Warrior")
mythic_sword = Weapons("Big Sword of DOOM !", "This sword came from hell, forged buy an ancient demon, anyway... BIIIGGG damage", DURABILITY_WEAPONS[5], 666, 5, "Mythic", DAMAGE_MODIFIER[5], "Warrior")

sword_inventory = Shop_Category()
sword_inventory.add_item(common_sword)
sword_inventory.add_item(uncommon_sword)
sword_inventory.add_item(rare_sword)
sword_inventory.add_item(epic_sword)
sword_inventory.add_item(legendary_sword)
sword_inventory.add_item(mythic_sword)

# KNIVES

common_knife = Weapons("The Opinel", "Perfect for cheese", DURABILITY_WEAPONS[0], "value", "drop chance", "Common", DAMAGE_MODIFIER[0], "Thief")
uncommon_knife = Weapons("Name", "Description", DURABILITY_WEAPONS[1], "value", "drop chance", "Uncommon", DAMAGE_MODIFIER[1], "Thief")
rare_knife = Weapons("Name", "Description", DURABILITY_WEAPONS[2], "value", "drop chance", "Rare", DAMAGE_MODIFIER[2], "Thief")
epic_knife = Weapons("Name", "Description", DURABILITY_WEAPONS[3], "value", "drop chance", "Epic", DAMAGE_MODIFIER[3], "Thief")
legendary_knife = Weapons("Name", "Description", DURABILITY_WEAPONS[4], "value", "drop chance", "Legendary", DAMAGE_MODIFIER[4], "Thief")
mythic_knife = Weapons("Big Knife of DOOM", DURABILITY_WEAPONS[5], "Durability", "value", "drop chance", "Mythic", DAMAGE_MODIFIER[5], "Thief")

knives_inventory = Shop_Category()
knives_inventory.add_item(common_knife)
knives_inventory.add_item(uncommon_knife)
knives_inventory.add_item(rare_knife)
knives_inventory.add_item(epic_knife)
knives_inventory.add_item(legendary_knife)
knives_inventory.add_item(mythic_knife)

# HAMMER

common_hammer = Weapons("Name", "Description", DURABILITY_WEAPONS[0], "value", "drop chance", "Common", DAMAGE_MODIFIER[0], "Colossus")
uncommon_hammer = Weapons("Name", "Description", DURABILITY_WEAPONS[1], "value", "drop chance", "Uncommon", DAMAGE_MODIFIER[1], "Colossus")
rare_hammer = Weapons("Name", "Description", DURABILITY_WEAPONS[2], "value", "drop chance", "Rare", DAMAGE_MODIFIER[2], "Colossus")
epic_hammer = Weapons("Name", "Description", DURABILITY_WEAPONS[3], "value", "drop chance", "Epic", DAMAGE_MODIFIER[3], "Colossus")
legendary_hammer = Weapons("Name", "Description", DURABILITY_WEAPONS[4], "value", "drop chance", "Legendary", DAMAGE_MODIFIER[4], "Colossus")
mythic_hammer = Weapons("Big Hammer of DOOM !", "Description", DURABILITY_WEAPONS[5], "value", "drop chance", "Mythic", DAMAGE_MODIFIER[5], "Colossus")

hammer_inventory = Shop_Category()
hammer_inventory.add_item(common_hammer)
hammer_inventory.add_item(uncommon_hammer)
hammer_inventory.add_item(rare_hammer)
hammer_inventory.add_item(epic_hammer)
hammer_inventory.add_item(legendary_hammer)
hammer_inventory.add_item(mythic_hammer)

# MAGE'S STICK

common_stick = Weapons("Branch", "A piece of wood", DURABILITY_WEAPONS[0], "value", "drop chance", "Common", DAMAGE_MODIFIER[0], "Mage")
uncommon_stick = Weapons("Name", "Description", DURABILITY_WEAPONS[1], "value", "drop chance", "Uncommon", DAMAGE_MODIFIER[1], "Mage")
rare_stick = Weapons("Name", "Description", DURABILITY_WEAPONS[2], "value", "drop chance", "Rare", DAMAGE_MODIFIER[2], "Mage")
epic_stick = Weapons("Name", "Description", DURABILITY_WEAPONS[3], "value", "drop chance", "Epic", DAMAGE_MODIFIER[3], "Mage")
legendary_stick = Weapons("Name", "Description", DURABILITY_WEAPONS[4], "value", "drop chance", "Legendary", DAMAGE_MODIFIER[4], "Mage")
mythic_stick = Weapons("Big Stick of DOOM !", "It's still a piece of shit", DURABILITY_WEAPONS[5],  666, 10, "Mythic", DAMAGE_MODIFIER[5], "Mage")

stick_inventory = Shop_Category()
stick_inventory.add_item(common_stick)
stick_inventory.add_item(uncommon_stick)
stick_inventory.add_item(rare_stick)
stick_inventory.add_item(epic_stick)
stick_inventory.add_item(legendary_stick)
stick_inventory.add_item(mythic_stick)

# SHIELD 

common_shield = Armor("Name", "Description", "Durability", "value", "drop chance", "Common", 1.5, "Any")
uncommon_shield = Armor("Name", "Description", "Durability", "value", "drop chance", "UnCommon", 1.5, "Any")
rare_shield = Armor("Name", "Description", "Durability", "value", "drop chance", "Rare", 1.5, "Any")
epic_shield = Armor("Name", "Description", "Durability", "value", "drop chance", "Epic", 1.5, "Any")
legendary_shield = Armor("Name", "Description", "Durability", "value", "drop chance", "Legendary", 1.5, "Any")
mythic_shield = Armor("Name", "Description", "Durability", "value", "drop chance", "Mythic", 1.5, "Any")

shield_inventory = Shop_Category()
shield_inventory.add_item(common_shield)
shield_inventory.add_item(uncommon_shield)
shield_inventory.add_item(rare_shield)
shield_inventory.add_item(epic_shield)
shield_inventory.add_item(legendary_shield)
shield_inventory.add_item(mythic_shield)

# ARMOR HELMET

common_helmet = Armor("Name", "Description", "Durability", "value", "drop chance", "Common", 1.5, "Any")
uncommon_helmet = Armor("Name", "Description", "Durability", "value", "drop chance", "UnCommon", 1.5, "Any")
rare_helmet = Armor("Name", "Description", "Durability", "value", "drop chance", "Rare", 1.5, "Any")
epic_helmet = Armor("Name", "Description", "Durability", "value", "drop chance", "Epic", 1.5, "Any")
legendary_helmet = Armor("Name", "Description", "Durability", "value", "drop chance", "Legendary", 1.5, "Any")
mythic_helmet = Armor("Name", "Description", "Durability", "value", "drop chance", "Mythic", 1.5, "Any")

helmet_inventory = Shop_Category()
helmet_inventory.add_item(common_helmet)
helmet_inventory.add_item(uncommon_helmet)
helmet_inventory.add_item(rare_helmet)
helmet_inventory.add_item(epic_helmet)
helmet_inventory.add_item(legendary_helmet)
helmet_inventory.add_item(mythic_helmet)

# ARMOR CHESTPLATE

common_chestplate = Armor("Name", "Description", "Durability", "value", "drop chance", "Common", 1.5, "Any")
uncommon_chestplate = Armor("Name", "Description", "Durability", "value", "drop chance", "UnCommon", 1.5, "Any")
rare_chestplate = Armor("Name", "Description", "Durability", "value", "drop chance", "Rare", 1.5, "Any")
epic_chestplate = Armor("Name", "Description", "Durability", "value", "drop chance", "Epic", 1.5, "Any")
legendary_chestplate = Armor("Name", "Description", "Durability", "value", "drop chance", "Legendary", 1.5, "Any")
mythic_chestplate = Armor("Name", "Description", "Durability", "value", "drop chance", "Mythic", 1.5, "Any")

chestplate_inventory = Shop_Category()
chestplate_inventory.add_item(common_chestplate)
chestplate_inventory.add_item(uncommon_chestplate)
chestplate_inventory.add_item(rare_chestplate)
chestplate_inventory.add_item(epic_chestplate)
chestplate_inventory.add_item(legendary_chestplate)
chestplate_inventory.add_item(mythic_chestplate)

# ARMOR LEGGINGS

common_leggings = Armor("Name", "Description", "Durability", "value", "drop chance", "Common", 1.5, "Any")
uncommon_leggings = Armor("Name", "Description", "Durability", "value", "drop chance", "Uncommon", 1.5, "Any")
rare_leggings = Armor("Name", "Description", "Durability", "value", "drop chance", "Rare", 1.5, "Any")
epic_leggings = Armor("Name", "Description", "Durability", "value", "drop chance", "Epic", 1.5, "Any")
legendary_leggings = Armor("Name", "Description", "Durability", "value", "drop chance", "Legendary", 1.5, "Any")
mythic_leggings = Armor("Name", "Description", "Durability", "value", "drop chance", "Mythic", 1.5, "Any")

leggings_inventory = Shop_Category()
leggings_inventory.add_item(common_leggings)
leggings_inventory.add_item(uncommon_leggings)
leggings_inventory.add_item(rare_leggings)
leggings_inventory.add_item(epic_leggings)
leggings_inventory.add_item(legendary_leggings)
leggings_inventory.add_item(mythic_leggings)

# ARMOR BOOTS

common_boots = Armor("Name", "Description", "Durability", "value", "drop chance", "Common", 1.5, "Any")
uncommon_boots = Armor("Name", "Description", "Durability", "value", "drop chance", "Uncommon", 1.5, "Any")
rare_boots = Armor("Name", "Description", "Durability", "value", "drop chance", "Rare", 1.5, "Any")
epic_boots = Armor("Name", "Description", "Durability", "value", "drop chance", "Epic", 1.5, "Any")
legendary_boots = Armor("Name", "Description", "Durability", "value", "drop chance", "Legendary", 1.5, "Any")
mythic_boots = Armor("Name", "Description", "Durability", "value", "drop chance", "Mythic", 1.5, "Any")

boots_inventory = Shop_Category()
boots_inventory.add_item(common_boots)
boots_inventory.add_item(uncommon_boots)
boots_inventory.add_item(rare_boots)
boots_inventory.add_item(epic_boots)
boots_inventory.add_item(legendary_boots)
boots_inventory.add_item(mythic_boots)

# POTIONS (HEALTH/MANA)

common_health_potion = Potion("Basic potion", "Just a little potion", 1, 10, 40, 10, 0, "Common", "Health")
uncommon_health_potion = Potion("Big potion", "Not just a little potion", 1, 20, 30, 25, 0, "Uncommon", "Health")
rare_health_potion = Potion("Really big potion", "Looks like a beer but it's not", 1, 50, 20, 50, 0, "Rare", "Health")
epic_health_potion = Potion("Huge potion", "Too much for a potion", 1, 75, 10, 75, 0, "Epic", "Health")
legendary_health_potion = Potion("Guargantuan potion", "This is stupidly big", 1, 100, 5, 100, 0, "Legendary", "Health")
mythic_health_potion = Potion("DAAAAAMMMMMNNNN potion", "I can't even quantify this thing", 1, 200, 1, 200, 0, "Mythic", "Health")

health_pot_inventory = Shop_Category()
health_pot_inventory.add_item(common_health_potion)
health_pot_inventory.add_item(uncommon_health_potion)
health_pot_inventory.add_item(rare_health_potion)
health_pot_inventory.add_item(epic_health_potion)
health_pot_inventory.add_item(legendary_health_potion)
health_pot_inventory.add_item(mythic_health_potion)

common_mana_potion = Potion("Basic mana potion", "Same stuff but for mana", 1, 10, 40, 0, 10,"Common",  "Mana")
uncommon_mana_potion = Potion("Big mana potion", "You're using too much spells", 1, 20, 30, 0, 25,"Uncommon", "Mana")
rare_mana_potion = Potion("Really big mana potion", "Do you eat mana ?", 1, 50, 20, 0, 50,"Rare", "Mana")
epic_mana_potion = Potion("Huge mana potion", "You don't even have this amount of mana, why ?", 1, 75, 10, 0, 75,"Epic", "Mana")
legendary_mana_potion = Potion("Guargantuan mana potion", "Are you stupid ?", 1, 100, 5, 1.5, 100, "Legendary", "Mana")
mythic_mana_potion = Potion("DAAAAAMMMMMNNNN mana potion", "You're definitely insane", 1, 200, 1, 0, 200, "Mythic", "Mana")

mana_pot_inventory = Shop_Category()
mana_pot_inventory.add_item(common_mana_potion)
mana_pot_inventory.add_item(uncommon_mana_potion)
mana_pot_inventory.add_item(rare_mana_potion)
mana_pot_inventory.add_item(epic_mana_potion)
mana_pot_inventory.add_item(legendary_mana_potion)
mana_pot_inventory.add_item(mythic_mana_potion)

weapons = {
    "common": [common_sword, common_knife, common_hammer, common_stick],
    "uncommon": [uncommon_sword, uncommon_knife, uncommon_hammer, uncommon_stick],
    "rare": [rare_sword, rare_knife, rare_hammer, rare_stick],
    "epic": [epic_sword, epic_knife, epic_hammer, epic_stick],
    "legendary": [legendary_sword, legendary_knife, legendary_hammer, legendary_stick],
    "mythic": [mythic_sword, mythic_knife, mythic_hammer, mythic_stick]
}

armor = {
    "common": [common_shield, common_helmet, common_chestplate, common_leggings, common_boots],
    "uncommon": [uncommon_shield, uncommon_helmet, uncommon_chestplate, uncommon_leggings, uncommon_boots],
    "rare": [rare_shield, rare_helmet, rare_chestplate, rare_leggings, rare_boots],
    "epic": [epic_shield, epic_helmet, epic_chestplate, epic_leggings, epic_boots],
    "legendary": [legendary_shield, legendary_helmet, legendary_chestplate, legendary_leggings, legendary_boots],
    "mythic": [mythic_shield, mythic_helmet, mythic_chestplate, mythic_leggings, mythic_boots]
}

potions = {
    "common": [common_health_potion, common_mana_potion],
    "uncommon": [uncommon_health_potion, uncommon_mana_potion],
    "rare": [rare_health_potion, rare_mana_potion],
    "epic": [epic_health_potion, epic_mana_potion],
    "legendary": [legendary_health_potion, legendary_mana_potion],
    "mythic": [mythic_health_potion, mythic_mana_potion]
}

class Game:
    def __init__(self):
        self.player = None
        self.playercolor = None
        self.enemies = []
        self.display = Display()
        self.room = Room(self)

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
        print(f"[{self.playercolor}]{self.player.name}[/{self.playercolor}] : {self.player.hp}/{self.player.max_hp} [red]HP[/red] - {self.player.gold} [yellow1]Gold[/yellow1] \n \n ")
        self.display.print_hub()
        hub_choice = int(input(""))
        self.hub_decision(hub_choice)

    def room(self):
        self.display.clear_console()
        self.display.title()
        self.display.infinite()
        print(f"[{self.playercolor}]{self.player.name}[/{self.playercolor}] : {self.player.hp}/{self.player.max_hp} [red]HP[/red]")
        self.new_room()
        if self.room.event == "chest":
            self.display.chest()
            self.display.open_chest()
            chest_choice = int(input())
            self.chest_decision(chest_choice)
            
    def chest_decision(self,choice):
        if choice == 1:
            print("This chest contain a : "+str(self.room.entity.self.items[1])+" Do you want to take it and sell your equipped one ?")
            print("1 - Yes")
            print("2 - No")
            replace_choice = int(input())
            if replace_choice == 1 :
                self.replace_decision(1)
            if replace_choice == 2 :
                self.replace_decision(2)
        if choice == 2:
            pass
        

    def hub_decision(self,choice):
        match choice:
            case 1:
                self.inventory()
            case 2:
                self.categories()
            case 3:
                self.room()
            case 4:
                self.display.clear_console()
                self.display.title()
                self.display.dungeon()
                self.display.difficulty()
                difficulty_choice = int(input(""))
                self.dungeon(difficulty_choice)
            case _:
                return self.hub()

    def inventory_decision(self,choice):
        if choice == 1:
            self.hub()
        if choice == 2:
            self.hub_decision(1)
    
    def categories(self):
        self.display.clear_console()
        self.display.title()
        self.display.shop()
        print(f"[{self.playercolor}]{self.player.name}[/{self.playercolor}] : {self.player.hp}/{self.player.max_hp} [red]HP[/red] - {self.player.gold} [yellow1]Gold[/yellow1] \n \n ")
        self.display.shop_categories()
        category_choice = int(input(""))
        self.shop_categories_decision(category_choice)

    def inventory(self):
        self.display.clear_console()
        self.display.title()
        self.display.inventory()
        print(f"[{self.playercolor}]{self.player.name}[/{self.playercolor}] : {self.player.hp}/{self.player.max_hp} [red]HP[/red] - {self.player.gold} [yellow1]Gold[/yellow1] \n \n ")
        self.player.inventory.display_inventory()
        self.display.quit_inventory()
        inventory_choice = int(input(""))
        self.inventory_decision(inventory_choice)

    def shop_categories_decision(self,choice):
        if choice == 1:
            self.display.clear_console()
            self.display.title()
            self.display.swords()

            sword_inventory.display_inventory()
            self.display.nevermind()
            buy_choice = int(input(""))
            if buy_choice == 7:
                self.categories()
            else:
                self.buy_decision(sword_inventory.items[(buy_choice - 1)])

        if choice == 2:
            self.display.clear_console()
            self.display.title()
            self.display.knives()

            knives_inventory.display_inventory()
            self.display.nevermind()
            buy_choice = int(input(""))
            if buy_choice == 7:
                self.categories()
            else:
                self.buy_decision(knives_inventory.items[(buy_choice - 1)])
        if choice == 3:
            self.display.clear_console()
            self.display.title()
            self.display.hammers()

            hammer_inventory.display_inventory()
            self.display.nevermind()
            buy_choice = int(input(""))
            if buy_choice == 7:
                self.categories()
            else:
                self.buy_decision(hammer_inventory.items[(buy_choice - 1)])
        if choice == 4:
            self.display.clear_console()
            self.display.title()
            self.display.sticks()

            stick_inventory.display_inventory()
            self.display.nevermind()
            buy_choice = int(input(""))
            if buy_choice == 7:
                self.categories()
            else:
                self.buy_decision(stick_inventory.items[(buy_choice - 1)])
        if choice == 5:
            self.display.clear_console()
            self.display.title()
            self.display.shields()

            shield_inventory.display_inventory()
            self.display.nevermind()
            buy_choice = int(input(""))
            if buy_choice == 7:
                self.categories()
            else:
                self.buy_decision(shield_inventory.items[(buy_choice - 1)])
        if choice == 6:
            self.display.clear_console()
            self.display.title()
            self.display.helmets()

            helmet_inventory.display_inventory()
            self.display.nevermind()
            buy_choice = int(input(""))
            if buy_choice == 7:
                self.categories()
            else:
                self.buy_decision(helmet_inventory.items[(buy_choice - 1)])
        if choice == 7:
            self.display.clear_console()
            self.display.title()
            self.display.chestplates()

            chestplate_inventory.display_inventory()
            self.display.nevermind()
            buy_choice = int(input(""))
            if buy_choice == 7:
                self.categories()
            else:
                self.buy_decision(chestplate_inventory.items[(buy_choice - 1)])
        if choice == 8:
            self.display.clear_console()
            self.display.title()
            self.display.leggings()

            leggings_inventory.display_inventory()
            self.display.nevermind()
            buy_choice = int(input(""))
            if buy_choice == 7:
                self.categories()
            else:
                self.buy_decision(leggings_inventory.items[(buy_choice - 1)])
        if choice == 9:
            self.display.clear_console()
            self.display.title()
            self.display.boots()

            boots_inventory.display_inventory()
            self.display.nevermind()
            buy_choice = int(input(""))
            if buy_choice == 7:
                self.categories()
            else:
                self.buy_decision(boots_inventory.items[(buy_choice - 1)])
        if choice == 10:
            pass
        if choice == 11:
            self.hub()

    def replace_decision(self, choice):
        if choice == 1:
            '''Remplacer l'item'''
            pass
        else: 
            self.current_area

    def buy_decision(self, item):
        if self.player.gold >= item.value:
            if self.player.char_class == item.item_class or item.item_class == "Any":
                    if item not in self.player.inventory.items and item.item_class == "Any":
                        self.player.inventory.add_item(item)
                        self.player.gold -= item.value
                        self.inventory()
                    else:
                        self.display.alreadyhave(item)
                        replace = int(input())
                        self.replace_decision(replace)

            else:
                self.display.wrong_class(self.player.char_class)
                sleep(2)
                self.categories()
        else:
            self.display.cantafford()
            sleep(2)
            self.categories()

    def generate_loot(self):
        rarity_probabilities = RARITY_PROBABILITIES
        items_dict = self.random_loot_category()
        rarity_roll = Dice(1000).roll()  # Supposons que Dice(1000) donne un entier aléatoire entre 1 et 1000
        rarity_cumulative_prob = 0

        # Déterminer la rareté en fonction des probabilités cumulatives
        for rarity, probability in enumerate(rarity_probabilities):
            rarity_cumulative_prob += probability
            if rarity_roll <= rarity_cumulative_prob * 1000:  # Multiplier par 1000 pour ajuster l'échelle
                break

        # Choisir un item aléatoire en fonction de la rareté
        rarity_name = rarity_names[rarity]
        item_list = items_dict.get(rarity_name, [])
        item_count = len(item_list)
        if item_count > 0:
            selected_item = random.choice(item_list)
            return selected_item
        else:
            return None

    @staticmethod    
    def random_loot_category():
        dice = Dice(3)
        roll = dice.roll()
        if roll == 1:
            return weapons
        if roll == 2:
            return armor
        if roll == 3:
            return potions
        
    def create_chest(self):
        chest = Chest()
        chest.add_item(self.generate_loot())
        return chest


    def choose_class(self):

        name = input(" \n Choose your name : ")

        self.display.print_class()

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
            self.playercolor = "yellow1"
        else:
            print("Entrée invalide. Veuillez choisir un numéro entre 1 et 4.")
            return self.choose_class()
        
    def new_adventure(self):
        self.display.clear_console()
        self.display.castle()
        print("You arrived in front of a huge abandonned castle")

    def new_room(self):
        self.room.random_event()

    def dungeon(self, choice):
        match choice:
            case 1:
                self.new_adventure()
                sleep(5)
                while self.player.is_alive():
                    for _ in range(4):
                        pass

            case 2:
                self.new_adventure()
                sleep(5)
                while self.player.is_alive():
                    for _ in range(9):
                        pass

            case 3:
                self.new_adventure()
                sleep(5)
                while self.player.is_alive():
                    for _ in range(24):
                        pass
                        
            case 4:
                self.new_adventure()
                sleep(5)
                while self.player.is_alive():
                    for _ in range(49):
                        pass

            case _:
                return self.hub()
        