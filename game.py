from rich import print
from display import Display
from room import Room
from time import sleep
from init import *
import random


class Game:
    def __init__(self):
        self.player = None
        self.playercolor = None
        self.enemies = []
        self.display = Display()
        self.room = Room(self)
        self.hub_deci = None
        self.boss_spawned = False

    def start(self):
        self.display.clear_console()
        self.display.title()
        self.display.menu()
        if self.player == None:
            self.choose_class()

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
                self.player = Thief(name, 2000, 0, 3, ATT1,ATT2, gold=50)
                self.playercolor = "green"
            case 4:
                self.player = Colossus(name, 20, 0, 3, ATT1,ATT2)
                self.playercolor = "yellow1"
            case _:
                print("Wrong entry, choose a number between 1 and 4.")
                sleep(3)
                return self.start()

    def hub(self):
        self.display.clear_console()
        self.display.title()
        self.display.village()
        print(f"[{self.playercolor}]{self.player.name}[/{self.playercolor}] : {self.player.hp}/{self.player.max_hp} ❤️ - {self.player.gold} 🪙 \n \n ")
        self.display.print_hub()
        hub_choice = int(input(""))
        self.hub_decision(hub_choice)

    def hub_decision(self, choice):
        match choice:
            case 1:
                self.hub_deci = 1
                self.inventory()
            case 2:
                self.hub_deci = 2
                self.shop_categories()
            case 3:
                self.hub_deci = 3
                self.infinite()
            case 4:
                self.hub_deci = 4
                self.display.clear_console()
                self.display.title()
                self.display.dungeon()
                self.display.difficulty()
                difficulty_choice = int(input(""))
                self.dungeon(difficulty_choice)
            case _:
                return self.hub()

    def inventory(self):
        self.display.clear_console()
        self.display.title()
        self.display.inventory()
        print(f"[{self.playercolor}]{self.player.name}[/{self.playercolor}] : {self.player.hp}/{self.player.max_hp} ❤️ - {self.player.gold} 🪙 \n \n ")
        self.player.inventory.display_inventory()
        self.display.quit_inventory()
        inventory_choice = int(input(""))
        self.inventory_decision(inventory_choice)

    def inventory_decision(self, choice):
        match choice:
            case 1:
                self.hub()
            case 2:
                self.hub_decision(1)
            case _:
                print("Wrong entry, can you read ?")
                sleep(3)
                self.hub_decision(1)

    def shop_categories(self):
        self.display.clear_console()
        self.display.title()
        self.display.shop()
        print(f"[{self.playercolor}]{self.player.name}[/{self.playercolor}] : {self.player.hp}/{self.player.max_hp} ❤️ - {self.player.gold} 🪙 \n \n ")
        self.display.shop_categories()
        category_choice = int(input(""))
        self.shop_categories_decision(category_choice)

    def shop_categories_decision(self, choice):
        match choice:
            case 1:
                self.display.clear_console()
                self.display.title()
                self.display.swords()

                sword_inventory.display_inventory()
                self.display.nevermind()
                buy_choice = int(input(""))
                match buy_choice:
                    case buy_choice if 1 <= buy_choice <= 6:
                        self.buy_decision(sword_inventory.items[(buy_choice - 1)])
                    case 7:
                        self.shop_categories()
                    case _:
                        print("Wrong entry (automatically returning to the shop)")
                        sleep(3)
                        self.shop_categories()
        
            case 2:
                self.display.clear_console()
                self.display.title()
                self.display.knives()

                knives_inventory.display_inventory()
                self.display.nevermind()
                buy_choice = int(input(""))
                match buy_choice:
                    case buy_choice if 1 <= buy_choice <= 6:
                        self.buy_decision(knives_inventory.items[(buy_choice - 1)])
                    case 7:
                        self.shop_categories()
                    case _:
                        print("Wrong entry (automatically returning to the shop)")
                        sleep(3)
                        self.shop_categories()
            case 3:
                self.display.clear_console()
                self.display.title()
                self.display.hammers()

                hammer_inventory.display_inventory()
                self.display.nevermind()
                buy_choice = int(input(""))
                match buy_choice:
                    case buy_choice if 1 <= buy_choice <= 6:
                        self.buy_decision(hammer_inventory.items[(buy_choice - 1)])
                    case 7:
                        self.shop_categories()
                    case _:
                        print("Wrong entry (automatically returning to the shop)")
                        sleep(3)
                        self.shop_categories()
            case 4:
                self.display.clear_console()
                self.display.title()
                self.display.sticks()

                stick_inventory.display_inventory()
                self.display.nevermind()
                buy_choice = int(input(""))
                match buy_choice:
                    case buy_choice if 1 <= buy_choice <= 6:
                        self.buy_decision(stick_inventory.items[(buy_choice - 1)])
                    case 7:
                        self.shop_categories()
                    case _:
                        print("Wrong entry (automatically returning to the shop)")
                        sleep(3)
                        self.shop_categories()
            case 5:
                self.display.clear_console()
                self.display.title()
                self.display.shields()

                shield_inventory.display_inventory()
                self.display.nevermind()
                buy_choice = int(input(""))
                match buy_choice:
                    case buy_choice if 1 <= buy_choice <= 6:
                        self.buy_decision(shield_inventory.items[(buy_choice - 1)])
                    case 7:
                        self.shop_categories()
                    case _:
                        print("Wrong entry (automatically returning to the shop)")
                        sleep(3)
                        self.shop_categories()
            case 6:
                self.display.clear_console()
                self.display.title()
                self.display.helmets()

                helmet_inventory.display_inventory()
                self.display.nevermind()
                buy_choice = int(input(""))
                match buy_choice:
                    case buy_choice if 1 <= buy_choice <= 6:
                        self.buy_decision(helmet_inventory.items[(buy_choice - 1)])
                    case 7:
                        self.shop_categories()
                    case _:
                        print("Wrong entry (automatically returning to the shop)")
                        sleep(3)
                        self.shop_categories()
            case 7:
                self.display.clear_console()
                self.display.title()
                self.display.chestplates()

                chestplate_inventory.display_inventory()
                self.display.nevermind()
                buy_choice = int(input(""))
                match buy_choice:
                    case buy_choice if 1 <= buy_choice <= 6:
                        self.buy_decision(chestplate_inventory.items[(buy_choice - 1)])
                    case 7:
                        self.shop_categories()
                    case _:
                        print("Wrong entry (automatically returning to the shop)")
                        sleep(3)
                        self.shop_categories()
            case 8:
                self.display.clear_console()
                self.display.title()
                self.display.leggings()

                leggings_inventory.display_inventory()
                self.display.nevermind()
                buy_choice = int(input(""))
                match buy_choice:
                    case buy_choice if 1 <= buy_choice <= 6:
                        self.buy_decision(leggings_inventory.items[(buy_choice - 1)])
                    case 7:
                        self.shop_categories()
                    case _:
                        print("Wrong entry (automatically returning to the shop)")
                        sleep(3)
                        self.shop_categories()
            case 9:
                self.display.clear_console()
                self.display.title()
                self.display.boots()

                boots_inventory.display_inventory()
                self.display.nevermind()
                buy_choice = int(input(""))
                match buy_choice:
                    case buy_choice if 1 <= buy_choice <= 6:
                        self.buy_decision(boots_inventory.items[(buy_choice - 1)])
                    case 7:
                        self.shop_categories()
                    case _:
                        print("Wrong entry (automatically returning to the shop)")
                        sleep(3)
                        self.shop_categories()
            case 10:
                self.display.clear_console()
                self.display.title()
                self.display.boots()

                health_pot_inventory.display_inventory()
                self.display.nevermind()
                buy_choice = int(input(""))
                match buy_choice:
                    case buy_choice if 1 <= buy_choice <= 6:
                        self.buy_decision(health_pot_inventory.items[(buy_choice - 1)])
                    case 7:
                        self.shop_categories()
                    case _:
                        print("Wrong entry (automatically returning to the shop)")
                        sleep(3)
                        self.shop_categories()
            case 11:
                self.hub()
            case _:
                print("Wrong entry (automatically returning to the shop)")
                sleep(3)
                self.shop_categories()

    def buy_decision(self, item):
        if self.player.gold >= item.value:
            if self.player.char_class == item.item_class or item.item_class == "Any":
                if len(self.player.inventory.items) == 0:
                    self.player.inventory.add_item(item)
                    self.player.gold -= item.value
                    self.shop_categories()
                else:
                    for i in self.player.inventory.items:
                        if i.item_type == item.item_type and not item.item_class == "Any":
                            self.replace_decision(item)
                        elif i.item_type != item.item_type or item.item_class == "Any": 
                            self.player.inventory.add_item(item)
                            self.player.gold -= item.value
                            self.shop_categories()
            else:
               self.display.wrong_class(self.player.char_class)
               sleep(2)
               self.shop_categories()
        else:
           self.display.cant_afford()
           sleep(2)
           self.shop_categories()

    def replace_decision(self, new_item):
        added = False
        for item in self.player.inventory.items:
            if new_item.item_type == None:
                self.player.inventory.add_item(new_item)
                self.shop_categories()
            elif new_item.item_type == item.item_type:
                added = True
                self.display.already_have(item)
                choice = int(input())
                if choice == 1:
                    self.player.inventory.remove_item(item)
                    self.player.inventory.add_item(new_item)
                    self.shop_categories()
                else:
                    self.shop_categories()
        if added == False:
            if new_item.item_class == self.player.char_class or new_item.item_class == "Any":
                self.player.inventory.add_item(new_item)
                self.shop_categories()
            else:
                self.display.wrong_class
                sleep(2)
                self.shop_categories()

        if added == False:
            self.player.inventory.add_item(new_item)
            self.shop_categories()

    def new_adventure(self):
        self.display.clear_console()
        self.display.castle()
        sleep(4)
        self.display.clear_console()
        self.display.room()

    def new_room(self):
        self.room.random_event()

    def create_room(self):
        print(f"[{self.playercolor}]{self.player.name}[/{self.playercolor}] : {self.player.hp}/{self.player.max_hp} ❤️")
        if self.boss_spawned == False:
            self.room.random_event()
            if self.room.event == "chest":
                self.display.chest()
                self.display.open_chest()
                chest_choice = int(input())
                self.chest_decision(chest_choice)
            if self.room.event == "enemy":
                self.fight()
        else:
            self.room.boss()
            self.fight()

    def fight(self):
        running = True
        while running :
            match self.room.enemy:
                case "skeleton":
                    self.display.clear_console()
                    self.display.skeleton()
                    print("You're facing a skeleton, what are you going to do ?")
                case "zombie":
                    self.display.clear_console()
                    self.display.zombie()
                    print("You're facing a zombie, what are you going to do ?")
                case "goblin":
                    self.display.clear_console()
                    self.display.goblin()
                    print("You're facing a goblin, what are you going to do ?")
                case "drake":
                    self.display.clear_console()
                    self.display.drake()
                    print("You're facing a huge drake, what are you going to do ?")
                case "demon":
                    self.display.clear_console()
                    self.display.demon()
                    print("You're facing an old demon, what are you going to do ?")
            print(f"[red]{self.room.entity.name}[/red] : {self.room.entity.hp}/{self.room.entity.max_hp} ❤️ \n")
            print(f"[{self.playercolor}]{self.player.name}[/{self.playercolor}] : {self.player.hp}/{self.player.max_hp} ❤️")
            self.display.which_attack(self.player.attack1, self.player.attack2)
            choice = int(input(""))
            match choice:
                case 1:
                    self.player.attack(self.room.entity,self.player.attack1.calculate_damages(self.player))
                case 2:
                    self.player.attack(self.room.entity,self.player.attack2.calculate_damages(self.player))
                case 3:
                    pot_inv = Inventory()
                    for item in self.player.inventory.items:
                        if item.type == "Potion":
                            pot_inv.add_item(item)
                        if len(pot_inv.items) != 0:
                            pot_inv.display_inventory()
                            pot_choice = int(input())
                            print(f"{pot_inv.items[pot_choice - 1].health_amount}")
                            self.player.increase_hp(pot_inv.items[pot_choice - 1].health_amount)
                            self.player.inventory.items.remove(pot_inv.items[pot_choice - 1])
                        else:
                            print("You don't have any potions (choose an attack)")
                            sleep(2)
                            self.fight()
                            return 0
                case _:
                    print("Wrong entry")
                    sleep(2)
                    self.fight()
            if self.room.entity.is_alive():
                self.room.entity.attack(self.player,self.room.entity.random_attack())
            if not self.player.is_alive() or not self.room.entity.is_alive():
                running = False
        if self.player.is_alive():
            self.display.clear_console()
            print(f"[red]{self.room.entity.name}[/red] : {self.room.entity.hp}/{self.room.entity.max_hp} ❤️ \n")
            print(f"[{self.playercolor}]{self.player.name}[/{self.playercolor}] : {self.player.hp}/{self.player.max_hp} ❤️")
            if self.hub_deci == 3:
                self.finished_fight_infinite()
            if self.hub_deci == 4:
                self.finished_fight_dungeon()
        if not self.player.is_alive():
            print("You have been defeated, what a shame ! (returning to the village)")
            sleep(3)
            self.player.hp = self.player.max_hp
            self.hub()

    def finished_fight_infinite(self):
        drop = self.enemy_dropped()
        self.player.gold += 10
        if drop == None:
            print("You defeated the enemy !")
            sleep(3)
            self.next_room_infinite()
        else:
            print(f"The enemy dropped a {drop.name} do you want to take it ?(It will replace your current one if you have one)")
            print(" - 1 Yes")
            print(" - 2 No")
            choice = int(input(""))
            match choice:
                case 1:
                    self.replace_loot_decision(drop)
                    self.next_room_infinite()
                case 2:
                    self.next_room_infinite()

    def finished_fight_dungeon(self):
        drop = self.enemy_dropped()
        self.player.gold += 10
        if drop == None:
            print("You defeated the enemy !")
            sleep(3)
            self.next_room_dungeon()
        else:
            print(f"The enemy dropped a {drop.name} do you want to take it ?(It will replace your current one if you have one)")
            print(" - 1 Yes")
            print(" - 2 No")
            choice = int(input(""))
            match choice:
                case 1:
                    self.replace_loot_decision(drop)
                    self.next_room_dungeon()
                case 2:
                    self.next_room_dungeon()

    def enemy_dropped(self):
        dice = Dice(100)
        roll = dice.roll()
        if roll > self.room.entity.drop_chances:
            return self.generate_loot()

    def create_chest(self):
        chest = Chest()
        chest.add_item(self.generate_loot())
        return chest

    def chest_decision(self, choice):
        match choice:
            case 1:
                print(f"This chest contain a {self.room.entity.items[0].name} Do you want to take it (and sell your equipped one ?)")
                print("1 - Yes")
                print("2 - No")
                replace_choice = int(input())
                match replace_choice:
                    case 1:
                        self.replace_loot_decision(self.room.entity.items[0])
                    case 2:
                        if self.hub_deci == 3:
                            self.next_room_infinite()
                        if self.hub_deci == 4:
                            self.next_room_dungeon()
                    case _:
                        if self.hub_deci == 3:
                            self.next_room_infinite()
                        if self.hub_deci == 4:
                            self.next_room_dungeon()
            case 2:
                if self.hub_deci == 3:
                    self.next_room_infinite()
                if self.hub_deci == 4:
                    self.next_room_dungeon()
            case _:
                if self.hub_deci == 3:
                    self.next_room_infinite()
                if self.hub_deci == 4:
                    self.next_room_dungeon()

    def generate_loot(self):
        rarity_probabilities = drop_chance
        items_dict = self.random_loot_category()
        rarity_roll = Dice(100).roll()  # Supposons que Dice(100) donne un entier aléatoire entre 1 et 1000
        rarity_cumulative_prob = 0

        # Déterminer la rareté en fonction des probabilités cumulatives
        for rarityi, probability in enumerate(rarity_probabilities):
            rarity_cumulative_prob += probability
            if rarity_roll <= rarity_cumulative_prob * 100:  # Multiplier par 1000 pour ajuster l'échelle
                break

        # Choisir un item aléatoire en fonction de la rareté
        rarity_name = rarity[rarityi]
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

    def replace_loot_decision(self, new_item):
        added = False
        for item in self.player.inventory.items:
            if new_item.item_type == None:
                if self.hub_deci == 3:
                    self.player.inventory.add_item(new_item)
                    self.next_room_infinite()
                if self.hub_deci == 4:
                    self.player.inventory.add_item(new_item)
                    self.next_room_dungeon()
            elif new_item.item_type == item.item_type:
                if new_item.item_class == self.player.char_class or new_item.item_class == "Any":
                    if self.hub_deci == 3:
                        added = True
                        self.player.inventory.remove_item(item)
                        self.player.inventory.add_item(new_item)
                        self.next_room_infinite()
                    if self.hub_deci == 4:
                        added = True
                        self.player.inventory.remove_item(item)
                        self.player.inventory.add_item(new_item)
                        self.next_room_dungeon()
                else:
                    if self.hub_deci == 3:
                        print("Wrong class for this item , returning to the choice")
                        self.next_room_infinite()
                    if self.hub_deci == 4:
                        print("Wrong class for this item , returning to the choice")
                        self.next_room_dungeon()
        if added == False:
            if new_item.item_class == self.player.char_class or new_item.item_class == "Any":
                if self.hub_deci == 3:
                    self.player.inventory.add_item(new_item)
                    self.next_room_infinite()
                if self.hub_deci == 4:
                    self.player.inventory.add_item(new_item)
                    self.next_room_dungeon()
            else:
                if self.hub_deci == 3:
                    self.display.wrong_class
                    sleep(2)
                    self.next_room_infinite()
                if self.hub_deci == 4:
                    self.display.wrong_class
                    sleep(2)
                    self.next_room_dungeon()

    def next_room_infinite(self):
        self.display.next_room_infinite()
        choice = int(input())
        match choice:
            case 1:
                self.player.hp = self.player.max_hp
                self.hub()
            case 2:
                self.display.clear_console()
                self.display.door()
                sleep(4)
                self.display.clear_console()
                self.create_room()
            case _:
                print("Wrong entry")
                sleep(2)
                return self.new_room()
            
    def next_room_dungeon(self):
        self.display.next_room_dungeon()
        choice = int(input())
        match choice:
            case 1:
                self.display.clear_console()
                self.display.door()
                sleep(4)
                self.display.clear_console()
                self.create_room()
            case 2:
                self.display.clear_console()
                self.display.door()
                sleep(4)
                self.display.clear_console()
                self.create_room()
            case _:
                self.display.clear_console()
                self.display.door()
                sleep(4)
                self.display.clear_console()
                self.create_room()

    def dungeon(self, choice):
        match choice:
            case 1:
                self.new_adventure()
                sleep(5)
                self.display.clear_console()
                self.display.room()
                sleep(5)
                while self.player.is_alive():
                    for _ in range(4):
                        self.create_room()
                    self.boss_spawned = True
                    self.create_room()
            case 2:
                self.new_adventure()
                sleep(5)
                self.display.clear_console()
                self.display.room()
                sleep(5)
                while self.player.is_alive():
                    for _ in range(9):
                        self.create_room()
                    self.boss_spawned = True
                    self.create_room()
            case 3:
                self.new_adventure()
                sleep(5)
                self.display.clear_console()
                self.display.room()
                sleep(5)
                while self.player.is_alive():
                    for _ in range(24):
                        self.create_room()
                    self.boss_spawned = True
                    self.create_room()
            case 4:
                self.new_adventure()
                sleep(5)
                self.display.clear_console()
                self.display.room()
                sleep(5)
                while self.player.is_alive():
                    for _ in range(49):
                        self.create_room()
                    self.boss_spawned = True
                    self.create_room()
            case _:
                return self.hub()

    def infinite(self):
        self.display.clear_console()
        self.display.title()
        self.display.infinite()
        sleep(3)
        self.display.clear_console()
        self.new_adventure()
        sleep(4)
        self.create_room()
