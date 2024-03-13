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


player = Warrior("Etienne", 100, 50, ATT1, ATT2)
epée = Weapons("Big Sword of DOOM", 100, "This sword came from your mom's pussy", 666, 10, "Mythic", 1.5)



display = Display()

display.clear_console()
display.title()

display.menu()


print(str(player))
player.inventory.add_item(epée)
print(player.inventory.display_inventory())
print(player.gold)
player.sell_item(epée)
print(player.inventory.display_inventory())
print(player.gold)




