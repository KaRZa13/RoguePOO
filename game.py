from rich import print
from display import Display
from dice import Dice
from attack import Attack
from room import Room
from time import sleep
from init import *
import random

HALF = 50
THREE_QUARTERS = 75
QUARTER = 25

ATTACK_DICE = Dice(100)
ATT1 = Attack("Normal attack", 6, THREE_QUARTERS, 1.25, QUARTER, "Just a normal sword strike", ATTACK_DICE)
ATT2 = Attack("Big attack", 4, HALF, 2.25, HALF, "A big attack , 50/50 either you destroy the opponent or you just miss your attack", ATTACK_DICE)

CLASS_TYPES = [0, "Warrior", "Mage", "Thief", "Colossus"]

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
            print(" - 1 : Yes")
            print(" - 2 : No")
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
        match choice:
            case 1:
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
        
            case 2:
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
            case 3:
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
            case 4:
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
            case 5:
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
            case 6:
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
            case 7:
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
            case 8:
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
            case 9:
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
            case 10:
                pass
            case 11:
                self.hub()
            case _:
                print("Wrong entry")
                return self.shop_categories_decision(choice)

    def replace_decision(self, choice):
        if choice == 1:
            '''Remplacer l'item'''
            pass
        else: 
            pass

    def buy_decision(self, item):
        if self.player.gold >= item.value:
            if self.player.char_class == item.item_class or item.item_class == "Any":
                if item not in self.player.inventory.items and item.item_class == "Any":
                    self.player.inventory.add_item(item)
                    self.player.gold -= item.value
                    self.shop_categories_decision()
                else:
                    self.display.already_have(item)
                    choice = int(input())
                    match choice:
                        case 1:
                            self.player.inventory.remove_item(item)
                        case 2:
                            pass
                        case _:
                            pass
            else:
               self.display.wrong_class(self.player.char_class)
               sleep(2)
               self.categories()
        else:
           self.display.cant_afford()
           sleep(2)
           self.categories()

    def generate_loot(self):
        rarity_probabilities = drop_chance
        items_dict = self.random_loot_category()
        rarity_roll = Dice(100).roll()  # Supposons que Dice(100) donne un entier aléatoire entre 1 et 1000
        rarity_cumulative_prob = 0

        # Déterminer la rareté en fonction des probabilités cumulatives
        for rarity, probability in enumerate(rarity_probabilities):
            rarity_cumulative_prob += probability
            if rarity_roll <= rarity_cumulative_prob * 100:  # Multiplier par 1000 pour ajuster l'échelle
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
        match roll:
            case 1:
                return weapons
            case 2:
                return armor
            case 3:
                return potions
        
    def create_chest(self):
        chest = Chest()
        chest.add_item(self.generate_loot())
        return chest

    def choose_class(self):
        name = input(" \n Choose your name : ")
        self.display.print_class()
        class_input = int(input(""))
        match class_input:
            case 1:
                self.player =  Warrior(name, 20, 0, 3, ATT1,ATT2)
                self.playercolor = "red"
            case 2:
                self.player = Mage(name, 20, 20, 3, ATT1,ATT2)
                self.playercolor = "blue"
            case 3:
                self.player = Thief(name, 20, 0, 3, ATT1,ATT2, 10)
                self.playercolor = "green"
            case 4:
                self.player = Colossus(name, 20, 0, 3, ATT1,ATT2)
                self.playercolor = "yellow1"
            case _:
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
