from player import *
from dice import Dice
from attack import Attack
from items import *
from display import Display
from rich import print

HALF = 50
THREE_QUARTERS = 75
QUARTER = 25
CLASS_TYPES = {1 : "Warrior", 2 : "Mage", 3 : "Thief", 4 : "Colossus"}

ATTACK_DICE = Dice(100)
ATT1 = Attack("Normal attack", 6, THREE_QUARTERS, 1.25, QUARTER, "Just a normal sword strike", ATTACK_DICE)
ATT2 = Attack("Big attack", 4, HALF, 2.25, HALF, "A big attack , 50/50 either you destroy the opponent or you just miss your attack", ATTACK_DICE)



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

cummun_hammer = Weapons()
uncommun_hammer = Weapons()
rare_hammer = Weapons()
epic_hammer = Weapons()
legendary_hammer = Weapons()
mythic_hammer = Weapons()

# MAGE'S STICK

commun_stick = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Commun", 1.5)
uncommun_stick = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Uncommun", 1.5)
rare_stick = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Rare", 1.5)
epic_stick = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Epic", 1.5)
legendary_stick = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Legendary", 1.5)
mythic_stick = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Mythic", 1.5)

# ARMOR HELMET

commun_helmet = Armor()
uncommun_helmet = Armor()
rare_helmet = Armor()
epic_helmet = Armor()
legendary_helmet = Armor()
mythic_helmet = Armor()

# ARMOR CHESTPLATE

commun_chestplate = Armor()
uncommun_chestplate = Armor()
rare_chestplate = Armor()
epic_chestplate = Armor()
legendary_chestplate = Armor()
mythic_chestplate = Armor()

# ARMOR LEGGINGS

commun_leggings = Armor()
uncommun_leggings = Armor()
rare_leggings = Armor()
epic_leggings = Armor()
legendary_leggings = Armor()
mythic_leggings = Armor()

# ARMOR BOOTS

commun_boots = Armor()
uncommun_boots = Armor()
rare_boots = Armor()
epic_boots = Armor()
legendary_boots = Armor()
mythic_boots = Armor()

# POTIONS

health_potion = Potion()
mana_potion = Potion()


display = Display()

display.clear_console()
display.title()

display.menu()

player = Warrior("Etienne", 100, 50, ATT1, ATT2)

print(str(player))
player.inventory.add_item(epée)
print(player.inventory.display_inventory())
print(player.gold)
player.sell_item(epée)
print(player.inventory.display_inventory())
print(player.gold)
