from character import *
from inventory import *
from items import *

'''#############################################################   ITEMS   #############################################################'''

durability_weapons = [25, 50, 100, 200, 500, 666]
durability_armor = [25, 50, 100, 200, 500, 666]
damage_modifier = [1, 1.1, 1.2, 1.3, .4, 1.5]
armor_modifier = [1, 1.1, 1.2, 1.3, 1.4, 1.5]
value_weapons = [15, 30, 50, 100, 200, 500]
value_armor = [20, 35, 75, 150, 300, 600]
drop_chance = [50, 25, 17, 12, 5, 1]
rarity_names = {0: 'common', 1: 'uncommon', 2: 'rare', 3: 'epic', 4: 'legendary', 5: 'mythic'}

# SWORDS

common_sword = Weapons("Chocolate sword", "Don't try to eat it, this is not real chocolate... It's not even a real sword", durability_weapons[0], value_weapons[0], 70, "Common", damage_modifier[0], "Warrior")
uncommon_sword = Weapons("Simple sword", "Just a piece of forged iron", durability_weapons[1], value_weapons[1], 40, "Uncommon", damage_modifier[1], "Warrior")
rare_sword = Weapons("Knight sword", "Finally a good weapon", durability_weapons[2], value_weapons[2], 35, "Rare", damage_modifier[2], "Warrior")
epic_sword = Weapons("Claymore", "Big sword for big damage !", durability_weapons[3], value_weapons[3], 25, "Epic", damage_modifier[3], "Warrior")
legendary_sword = Weapons("Excalibur", "More than just a sword ", durability_weapons[4], value_weapons[4], 15, "Legendary", damage_modifier[4], "Warrior")
mythic_sword = Weapons("Big Sword of DOOM !", "This sword came from hell, forged buy an ancient demon, anyway... BIIIGGG damage", durability_weapons[5], value_weapons[5], 5, "Mythic", damage_modifier[5], "Warrior")

sword_inventory = Shop_Category()
sword_inventory.add_item(common_sword)
sword_inventory.add_item(uncommon_sword)
sword_inventory.add_item(rare_sword)
sword_inventory.add_item(epic_sword)
sword_inventory.add_item(legendary_sword)
sword_inventory.add_item(mythic_sword)

# KNIVES

common_knife = Weapons("The Opinel", "Perfect for cheese", durability_weapons[0], value_weapons[0], "drop chance", "Common", damage_modifier[0], "Thief")
uncommon_knife = Weapons("Kitchen knife", "Better than the opinel, it's perfect for big meat", durability_weapons[1], value_weapons[1], "drop chance", "Uncommon", damage_modifier[1], "Thief")
rare_knife = Weapons("Butcher knife", "Really big one", durability_weapons[2], value_weapons[2], "drop chance", "Rare", damage_modifier[2], "Thief")
epic_knife = Weapons("Hunting knife", "This knife is use for any kind of animals or living thing", durability_weapons[3], value_weapons[3], "drop chance", "Epic", damage_modifier[3], "Thief")
legendary_knife = Weapons("Buttlefly knife Fade FN Statrack", "Description", durability_weapons[4], value_weapons[4], "drop chance", "Legendary", damage_modifier[4], "Thief")
mythic_knife = Weapons("Big Knife of DOOM", "Exactly the same as the sword but it's a knife", durability_weapons[5], value_weapons[5], "drop chance", "Mythic", damage_modifier[5], "Thief")

knives_inventory = Shop_Category()
knives_inventory.add_item(common_knife)
knives_inventory.add_item(uncommon_knife)
knives_inventory.add_item(rare_knife)
knives_inventory.add_item(epic_knife)
knives_inventory.add_item(legendary_knife)
knives_inventory.add_item(mythic_knife)

# HAMMER

common_hammer = Weapons("Name", "Description", durability_weapons[0], value_weapons[0], "drop chance", "Common", damage_modifier[0], "Colossus")
uncommon_hammer = Weapons("Name", "Description", durability_weapons[1], value_weapons[1], "drop chance", "Uncommon", damage_modifier[1], "Colossus")
rare_hammer = Weapons("Name", "Description", durability_weapons[2], value_weapons[2], "drop chance", "Rare", damage_modifier[2], "Colossus")
epic_hammer = Weapons("Name", "Description", durability_weapons[3], value_weapons[3], "drop chance", "Epic", damage_modifier[3], "Colossus")
legendary_hammer = Weapons("Name", "Description", durability_weapons[4], value_weapons[4], "drop chance", "Legendary", damage_modifier[4], "Colossus")
mythic_hammer = Weapons("Big Hammer of DOOM !", "Description", durability_weapons[5], value_weapons[5], "drop chance", "Mythic", damage_modifier[5], "Colossus")

hammer_inventory = Shop_Category()
hammer_inventory.add_item(common_hammer)
hammer_inventory.add_item(uncommon_hammer)
hammer_inventory.add_item(rare_hammer)
hammer_inventory.add_item(epic_hammer)
hammer_inventory.add_item(legendary_hammer)
hammer_inventory.add_item(mythic_hammer)

# MAGE'S STICK

common_stick = Weapons("Branch", "A piece of wood", durability_weapons[0], value_weapons[0], "drop chance", "Common", damage_modifier[0], "Mage")
uncommon_stick = Weapons("Name", "Description", durability_weapons[1], value_weapons[1], "drop chance", "Uncommon", damage_modifier[1], "Mage")
rare_stick = Weapons("Name", "Description", durability_weapons[2],  value_weapons[2], "drop chance", "Rare", damage_modifier[2], "Mage")
epic_stick = Weapons("Name", "Description", durability_weapons[3],  value_weapons[3], "drop chance", "Epic", damage_modifier[3], "Mage")
legendary_stick = Weapons("Name", "Description", durability_weapons[4],  value_weapons[4], "drop chance", "Legendary", damage_modifier[4], "Mage")
mythic_stick = Weapons("Big Stick of DOOM !", "It's still a piece of shit", durability_weapons[5],   value_weapons[5], 10, "Mythic", damage_modifier[5], "Mage")

stick_inventory = Shop_Category()
stick_inventory.add_item(common_stick)
stick_inventory.add_item(uncommon_stick)
stick_inventory.add_item(rare_stick)
stick_inventory.add_item(epic_stick)
stick_inventory.add_item(legendary_stick)
stick_inventory.add_item(mythic_stick)

# SHIELD 

common_shield = Armor("Name", "Description", durability_armor[0], value_armor[0], "drop chance", "Common", armor_modifier[0], "Any")
uncommon_shield = Armor("Name", "Description", durability_armor[1], value_armor[1], "drop chance", "Uncommon", armor_modifier[1], "Any")
rare_shield = Armor("Name", "Description", durability_armor[2], value_armor[2], "drop chance", "Rare", armor_modifier[2], "Any")
epic_shield = Armor("Name", "Description", durability_armor[3], value_armor[3], "drop chance", "Epic", armor_modifier[3], "Any")
legendary_shield = Armor("Name", "Description", durability_armor[4], value_armor[4], "drop chance", "Legendary", armor_modifier[4], "Any")
mythic_shield = Armor("Name", "Description", durability_armor[5], value_armor[5], "drop chance", "Mythic", armor_modifier[5], "Any")

shield_inventory = Shop_Category()
shield_inventory.add_item(common_shield)
shield_inventory.add_item(uncommon_shield)
shield_inventory.add_item(rare_shield)
shield_inventory.add_item(epic_shield)
shield_inventory.add_item(legendary_shield)
shield_inventory.add_item(mythic_shield)

# ARMOR HELMET

common_helmet = Armor("Common helmet", "Description", durability_armor[0], value_armor[0], "drop chance", "Common", armor_modifier[0], "Any")
uncommon_helmet = Armor("Uncommon helmet", "Description", durability_armor[1], value_armor[1], "drop chance", "Uncommon", armor_modifier[1], "Any")
rare_helmet = Armor("Rare helmet", "Description", durability_armor[2], value_armor[2], "drop chance", "Rare", armor_modifier[2], "Any")
epic_helmet = Armor("Epic helmet", "Description", durability_armor[3], value_armor[3], "drop chance", "Epic", armor_modifier[3], "Any")
legendary_helmet = Armor("Legendary helmet", "Description", durability_armor[4], value_armor[4], "drop chance", "Legendary", armor_modifier[4], "Any")
mythic_helmet = Armor("Mythic helmet", "Description", durability_armor[5], value_armor[5], "drop chance", "Mythic", armor_modifier[5], "Any")

helmet_inventory = Shop_Category()
helmet_inventory.add_item(common_helmet)
helmet_inventory.add_item(uncommon_helmet)
helmet_inventory.add_item(rare_helmet)
helmet_inventory.add_item(epic_helmet)
helmet_inventory.add_item(legendary_helmet)
helmet_inventory.add_item(mythic_helmet)

# ARMOR CHESTPLATE

common_chestplate = Armor("Common chestplate", "Description", durability_armor[0], value_armor[0], "drop chance", "Common", armor_modifier[0], "Any")
uncommon_chestplate = Armor("Uncommon chestplate", "Description", durability_armor[1], value_armor[1], "drop chance", "Uncommon", armor_modifier[1], "Any")
rare_chestplate = Armor("Rare chestplate", "Description", durability_armor[2], value_armor[2], "drop chance", "Rare", armor_modifier[2], "Any")
epic_chestplate = Armor("Epic chestplate", "Description", durability_armor[3], value_armor[3], "drop chance", "Epic", armor_modifier[3], "Any")
legendary_chestplate = Armor("Legendary chestplate", "Description", durability_armor[4], value_armor[4], "drop chance", "Legendary", armor_modifier[4], "Any")
mythic_chestplate = Armor("Mythic helmet", "Description", durability_armor[5], value_armor[5], "drop chance", "Mythic", armor_modifier[5], "Any")

chestplate_inventory = Shop_Category()
chestplate_inventory.add_item(common_chestplate)
chestplate_inventory.add_item(uncommon_chestplate)
chestplate_inventory.add_item(rare_chestplate)
chestplate_inventory.add_item(epic_chestplate)
chestplate_inventory.add_item(legendary_chestplate)
chestplate_inventory.add_item(mythic_chestplate)

# ARMOR LEGGINGS

common_leggings = Armor("Common leggings", "Description", durability_armor[0], value_armor[0], "drop chance", "Common", armor_modifier[0], "Any")
uncommon_leggings = Armor("Uncommon leggings", "Description", durability_armor[1], value_armor[1], "drop chance", "Uncommon", armor_modifier[1], "Any")
rare_leggings = Armor("Rare leggings", "Description", durability_armor[2], value_armor[2], "drop chance", "Rare", armor_modifier[2], "Any")
epic_leggings = Armor("Epic leggings", "Description", durability_armor[3], value_armor[3], "drop chance", "Epic", armor_modifier[3], "Any")
legendary_leggings = Armor("Legendary leggings", "Description", durability_armor[4], value_armor[4], "drop chance", "Legendary", armor_modifier[4], "Any")
mythic_leggings = Armor("Mythic leggings", "Description", durability_armor[5], value_armor[5], "drop chance", "Mythic", armor_modifier[5], "Any")

leggings_inventory = Shop_Category()
leggings_inventory.add_item(common_leggings)
leggings_inventory.add_item(uncommon_leggings)
leggings_inventory.add_item(rare_leggings)
leggings_inventory.add_item(epic_leggings)
leggings_inventory.add_item(legendary_leggings)
leggings_inventory.add_item(mythic_leggings)

# ARMOR BOOTS

common_boots = Armor("Common boots", "Description", durability_armor[0], value_armor[0], "drop chance", "Common", armor_modifier[0], "Any")
uncommon_boots = Armor("Uncommon boots", "Description", durability_armor[1], value_armor[1], "drop chance", "Uncommon", armor_modifier[1], "Any")
rare_boots = Armor("Rare boots", "Description", durability_armor[2], value_armor[2], "drop chance", "Rare", armor_modifier[2], "Any")
epic_boots = Armor("Epic boots", "Description", durability_armor[3], value_armor[3], "drop chance", "Epic", armor_modifier[3], "Any")
legendary_boots = Armor("Legendary boots", "Description", durability_armor[4], value_armor[4], "drop chance", "Legendary", armor_modifier[4], "Any")
mythic_boots = Armor("Mythic boots", "Description", durability_armor[5], value_armor[5], "drop chance", "Mythic", armor_modifier[5], "Any")

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
