from character import *
from inventory import *
from items import *

'''#############################################################   ITEMS   #############################################################'''

durability_weapons = [25, 50, 100, 200, 500, 666]
durability_armor = [25, 50, 100, 200, 500, 666]
durability_potion = 1
damage_modifier = [1, 1.1, 1.2, 1.3, .4, 1.5]
armor_modifier = [1, 1.1, 1.2, 1.3, 1.4, 1.5]
health_amount = []
mana_amount = []
value_weapons = [15, 30, 50, 100, 200, 500]
value_armor = [20, 35, 75, 150, 300, 600]
value_potions = [10, 20, 50, 75, 100, 200]

drop_chance = [50, 25, 17, 12, 5, 1]
rarity = ["Common", "Uncommon", "Rare", "Epic", "Legendary", "Mythic"]

# SWORDS

common_sword = Weapons("Chocolate sword", 
                       "Don't try to eat it, this is not real chocolate... It's not even a real sword", 
                       durability_weapons[0], 
                       value_weapons[0], 
                       70, 
                       rarity[0], 
                       damage_modifier[0], 
                       "Warrior", 
                       "Weapon",
                       "Sword")

uncommon_sword = Weapons("Simple sword", 
                         "Just a piece of forged iron", 
                         durability_weapons[1], 
                         value_weapons[1], 
                         40, 
                         rarity[1], 
                         damage_modifier[1], 
                         "Warrior", 
                         "Weapon",
                         "Sword")

rare_sword = Weapons("Knight sword", 
                     "Finally a good weapon", 
                     durability_weapons[2], 
                     value_weapons[2], 
                     35, 
                     rarity[2], 
                     damage_modifier[2], 
                     "Warrior", 
                     "Weapon",
                     "Sword")

epic_sword = Weapons("Claymore", 
                     "Big sword for big damage !", 
                     durability_weapons[3], 
                     value_weapons[3], 
                     25, 
                     rarity[3], 
                     damage_modifier[3], 
                     "Warrior", 
                     "Weapon",
                     "Sword")

legendary_sword = Weapons("Excalibur", 
                          "More than just a sword ", 
                          durability_weapons[4], 
                          value_weapons[4], 
                          15, rarity[4], 
                          damage_modifier[4], 
                          "Warrior", 
                          "Weapon",
                          "Sword")

mythic_sword = Weapons("Big Sword of DOOM !", 
                       "This sword came from hell, forged buy an ancient demon, anyway... BIIIGGG damage", 
                       durability_weapons[5], 
                       value_weapons[5], 
                       5, 
                       rarity[5], 
                       damage_modifier[5], 
                       "Warrior", 
                       "Weapon",
                       "Sword")

sword_inventory = Shop_Category()
sword_inventory.add_item(common_sword)
sword_inventory.add_item(uncommon_sword)
sword_inventory.add_item(rare_sword)
sword_inventory.add_item(epic_sword)
sword_inventory.add_item(legendary_sword)
sword_inventory.add_item(mythic_sword)

# KNIVES

common_knife = Weapons("The Opinel", 
                       "Perfect for cheese", 
                       durability_weapons[0], 
                       value_weapons[0], 
                       "drop chance", 
                       rarity[0], 
                       damage_modifier[0], 
                       "Thief", 
                       "Weapon",
                       "Knife")

uncommon_knife = Weapons("Kitchen knife", 
                         "Better than the opinel, it's perfect for big meat", 
                         durability_weapons[1], 
                         value_weapons[1], 
                         "drop chance", 
                         rarity[1], 
                         damage_modifier[1], 
                         "Thief", 
                         "Weapon",
                         "Knife")

rare_knife = Weapons("Butcher knife", 
                     "Really big one", 
                     durability_weapons[2], 
                     value_weapons[2], 
                     "drop chance", 
                     rarity[2], 
                     damage_modifier[2], 
                     "Thief", 
                     "Weapon",
                     "Knife")

epic_knife = Weapons("Hunting knife", 
                     "This knife is use for any kind of animals or living thing", 
                     durability_weapons[3], 
                     value_weapons[3], 
                     "drop chance", 
                     rarity[3], 
                     damage_modifier[3], 
                     "Thief", 
                     "Weapon",
                     "Knife")

legendary_knife = Weapons("Buttlefly knife Fade FN Statrack", 
                          "100% Fade this is worth a few minimal wages", 
                          durability_weapons[4], 
                          value_weapons[4], 
                          "drop chance", 
                          rarity[4], 
                          damage_modifier[4], 
                          "Thief", 
                          "Weapon",
                          "Knife")

mythic_knife = Weapons("Big Knife of DOOM", 
                       "Exactly the same as the sword but it's a knife", 
                       durability_weapons[5], 
                       value_weapons[5], 
                       "drop chance", 
                       rarity[5], 
                       damage_modifier[5], 
                       "Thief", 
                       "Weapon",
                       "Knife")

knives_inventory = Shop_Category()
knives_inventory.add_item(common_knife)
knives_inventory.add_item(uncommon_knife)
knives_inventory.add_item(rare_knife)
knives_inventory.add_item(epic_knife)
knives_inventory.add_item(legendary_knife)
knives_inventory.add_item(mythic_knife)

# HAMMER

common_hammer = Weapons("Toy hammer", 
                        "Have you ever been a child ?", 
                        durability_weapons[0], 
                        value_weapons[0], 
                        "drop chance", 
                        rarity[0], 
                        damage_modifier[0], 
                        "Colossus", 
                        "Weapon",
                        "Hammer")

uncommon_hammer = Weapons("DIY Hammer", 
                          "It's meant for nails but it works on zombies too", 
                          durability_weapons[1], 
                          value_weapons[1], 
                          "drop chance", 
                          rarity[1], 
                          damage_modifier[1], 
                          "Colossus", 
                          "Weapon",
                          "Hammer")

rare_hammer = Weapons("Torbjörn hammer", 
                      "You want to repair your turret , right ?", 
                      durability_weapons[2], 
                      value_weapons[2], 
                      "drop chance", 
                      rarity[2], 
                      damage_modifier[2], 
                      "Colossus", 
                      "Weapon",
                      "Hammer")

epic_hammer = Weapons("War hammer 40000", 
                      "Not the game bro", 
                      durability_weapons[3], 
                      value_weapons[3], 
                      "drop chance", 
                      rarity[3], 
                      damage_modifier[3], 
                      "Colossus", 
                      "Weapon",
                      "Hammer")

legendary_hammer = Weapons("Mjöllnir", 
                           "It's a pretty cool hammer tho", 
                           durability_weapons[4], 
                           value_weapons[4], 
                           "drop chance", 
                           rarity[4], 
                           damage_modifier[4], 
                           "Colossus", 
                           "Weapon",
                           "Hammer")

mythic_hammer = Weapons("Big Hammer of DOOM !", 
                        "You know the Burj Khalifa ? This hammer if BIGGER", 
                        durability_weapons[5], 
                        value_weapons[5], 
                        "drop chance", 
                        rarity[5], 
                        damage_modifier[5], 
                        "Colossus", 
                        "Weapon",
                        "Hammer")

hammer_inventory = Shop_Category()
hammer_inventory.add_item(common_hammer)
hammer_inventory.add_item(uncommon_hammer)
hammer_inventory.add_item(rare_hammer)
hammer_inventory.add_item(epic_hammer)
hammer_inventory.add_item(legendary_hammer)
hammer_inventory.add_item(mythic_hammer)

# MAGE'S STICK

common_stick = Weapons("Thorn", 
                       "More efficient than you think mostly in MMA", 
                       durability_weapons[0], 
                       value_weapons[0], 
                       "drop chance", 
                       rarity[0], 
                       damage_modifier[0], 
                       "Mage", 
                       "Weapon",
                       "Stick")

uncommon_stick = Weapons("Branch", 
                         "A piece of wood", 
                         durability_weapons[1], 
                         value_weapons[1], 
                         "drop chance", 
                         rarity[1], 
                         damage_modifier[1], 
                         "Mage", 
                         "Weapon",
                         "Stick")

rare_stick = Weapons("Makeup stick", 
                     "You have to be well made-up to be a mage", 
                     durability_weapons[2], 
                     value_weapons[2], 
                     "drop chance", 
                     rarity[2], 
                     damage_modifier[2], 
                     "Mage", 
                     "Weapon",
                     "Stick")

epic_stick = Weapons("The Baguette", 
                     "Oui oui baguette", 
                     durability_weapons[3], 
                      value_weapons[3], 
                     "drop chance", 
                     rarity[3], 
                     damage_modifier[3], 
                     "Mage", 
                     "Weapon",
                     "Stick")

legendary_stick = Weapons("Elderberry wand", 
                          "Let the magic begin", 
                          durability_weapons[4], 
                          value_weapons[4], 
                          "drop chance", 
                          rarity[4], 
                          damage_modifier[4], 
                          "Mage", 
                          "Weapon",
                          "Stick")

mythic_stick = Weapons("Big Stick of DOOM !", 
                       "It's still a piece of shit", 
                       durability_weapons[5], 
                       value_weapons[5], 
                       "drop chance", 
                       rarity[5], 
                       damage_modifier[5], 
                       "Mage", 
                       "Weapon",
                       "Stick")

stick_inventory = Shop_Category()
stick_inventory.add_item(common_stick)
stick_inventory.add_item(uncommon_stick)
stick_inventory.add_item(rare_stick)
stick_inventory.add_item(epic_stick)
stick_inventory.add_item(legendary_stick)
stick_inventory.add_item(mythic_stick)

# SHIELD 

common_shield = Armor("Cardboard shield", 
                      "Yes , I was a child too ...", 
                      durability_armor[0], 
                      value_armor[0], 
                      "drop chance", 
                      rarity[0], 
                      armor_modifier[0], 
                      "Any", 
                      "Armor",
                      "Shield")

uncommon_shield = Armor("Name", 
                      "Description", 
                      durability_armor[1], 
                      value_armor[1], 
                      "drop chance", 
                      rarity[1], 
                      armor_modifier[1], 
                      "Any", 
                      "Armor",
                      "Shield")

rare_shield = Armor("Name", 
                      "Description", 
                      durability_armor[2], 
                      value_armor[2], 
                      "drop chance", 
                      rarity[2], 
                      armor_modifier[2], 
                      "Any", 
                      "Armor",
                      "Shield")

epic_shield = Armor("Name", 
                      "Description", 
                      durability_armor[3], 
                      value_armor[3], 
                      "drop chance", 
                      rarity[3], 
                      armor_modifier[3], 
                      "Any", 
                      "Armor",
                      "Shield")

legendary_shield = Armor("Reinhardt shield", 
                      "It's pretty big , no ?", 
                      durability_armor[4], 
                      value_armor[4], 
                      "drop chance", 
                      rarity[4], 
                      armor_modifier[4], 
                      "Any", 
                      "Armor",
                      "Shield")

mythic_shield = Armor("Big shield of DOOM !", 
                      "What are you doing with this in your hands ?", 
                      durability_armor[5], 
                      value_armor[5], 
                      "drop chance", 
                      rarity[5], 
                      armor_modifier[5], 
                      "Any", 
                      "Armor",
                      "Shield")

shield_inventory = Shop_Category()
shield_inventory.add_item(common_shield)
shield_inventory.add_item(uncommon_shield)
shield_inventory.add_item(rare_shield)
shield_inventory.add_item(epic_shield)
shield_inventory.add_item(legendary_shield)
shield_inventory.add_item(mythic_shield)

# ARMOR HELMET

common_helmet = Armor("Common helmet", 
                      "Description", 
                      durability_armor[0], 
                      value_armor[0], 
                      "drop chance", 
                      rarity[0], 
                      armor_modifier[0], 
                      "Any", 
                      "Armor",
                      "Shield")

uncommon_helmet = Armor("Uncommon helmet", 
                      "Description", 
                      durability_armor[1], 
                      value_armor[1], 
                      "drop chance", 
                      rarity[1], 
                      armor_modifier[1], 
                      "Any", 
                      "Armor",
                      "Helmet")

rare_helmet = Armor("Rare helmet", 
                      "Description", 
                      durability_armor[2], 
                      value_armor[2], 
                      "drop chance", 
                      rarity[2], 
                      armor_modifier[2], 
                      "Any", 
                      "Armor",
                      "Helmet")

epic_helmet = Armor("Epic helmet", 
                      "Description", 
                      durability_armor[3], 
                      value_armor[3], 
                      "drop chance", 
                      rarity[3], 
                      armor_modifier[3], 
                      "Any", 
                      "Armor",
                      "Helmet")

legendary_helmet = Armor("Legendary helmet", 
                      "Description", 
                      durability_armor[4], 
                      value_armor[4], 
                      "drop chance", 
                      rarity[4], 
                      armor_modifier[4], 
                      "Any", 
                      "Armor",
                      "Helmet")

mythic_helmet = Armor("Mythic helmet", 
                      "Description", 
                      durability_armor[5], 
                      value_armor[5], 
                      "drop chance", 
                      rarity[5], 
                      armor_modifier[5], 
                      "Any", 
                      "Armor",
                      "Helmet")

helmet_inventory = Shop_Category()
helmet_inventory.add_item(common_helmet)
helmet_inventory.add_item(uncommon_helmet)
helmet_inventory.add_item(rare_helmet)
helmet_inventory.add_item(epic_helmet)
helmet_inventory.add_item(legendary_helmet)
helmet_inventory.add_item(mythic_helmet)

# ARMOR CHESTPLATE

common_chestplate = Armor("Common chestplate", 
                          "Description", 
                          durability_armor[0], 
                          value_armor[0], 
                          "drop chance", 
                          rarity[0], 
                          armor_modifier[0], 
                          "Any", 
                          "Armor",
                          "Chestplate")

uncommon_chestplate = Armor("Uncommon chestplate", 
                          "Description", 
                          durability_armor[1], 
                          value_armor[1], 
                          "drop chance", 
                          rarity[1], 
                          armor_modifier[1], 
                          "Any", 
                          "Armor",
                          "Chestplate")

rare_chestplate = Armor("Rare chestplate", 
                          "Description", 
                          durability_armor[2], 
                          value_armor[2], 
                          "drop chance", 
                          rarity[2], 
                          armor_modifier[2], 
                          "Any", 
                          "Armor",
                          "Chestplate")

epic_chestplate = Armor("Epic chestplate", 
                          "Description", 
                          durability_armor[3], 
                          value_armor[3], 
                          "drop chance", 
                          rarity[3], 
                          armor_modifier[3], 
                          "Any", 
                          "Armor",
                          "Chestplate")

legendary_chestplate = Armor("Legendary chestplate", 
                          "Description", 
                          durability_armor[4], 
                          value_armor[4], 
                          "drop chance", 
                          rarity[4], 
                          armor_modifier[4], 
                          "Any", 
                          "Armor",
                          "Chestplate")

mythic_chestplate = Armor("Mythic helmet", 
                          "Description", 
                          durability_armor[5], 
                          value_armor[5], 
                          "drop chance", 
                          rarity[5], 
                          armor_modifier[5], 
                          "Any", 
                          "Armor",
                          "Chestplate")

chestplate_inventory = Shop_Category()
chestplate_inventory.add_item(common_chestplate)
chestplate_inventory.add_item(uncommon_chestplate)
chestplate_inventory.add_item(rare_chestplate)
chestplate_inventory.add_item(epic_chestplate)
chestplate_inventory.add_item(legendary_chestplate)
chestplate_inventory.add_item(mythic_chestplate)

# ARMOR LEGGINGS

common_leggings = Armor("Common leggings", 
                        "Description", 
                        durability_armor[0], 
                        value_armor[0], 
                        "drop chance", 
                        rarity[0], 
                        armor_modifier[0], 
                        "Any", 
                        "Armor",
                        "Leggings")

uncommon_leggings = Armor("Uncommon leggings", 
                        "Description", 
                        durability_armor[1], 
                        value_armor[1], 
                        "drop chance", 
                        rarity[1], 
                        armor_modifier[1], 
                        "Any", 
                        "Armor",
                        "Leggings")

rare_leggings = Armor("Rare leggings", 
                        "Description", 
                        durability_armor[2], 
                        value_armor[2], 
                        "drop chance", 
                        rarity[2], 
                        armor_modifier[2], 
                        "Any", 
                        "Armor",
                        "Leggings")

epic_leggings = Armor("Epic leggings", 
                        "Description", 
                        durability_armor[3], 
                        value_armor[3], 
                        "drop chance", 
                        rarity[3], 
                        armor_modifier[3], 
                        "Any", 
                        "Armor",
                        "Leggings")

legendary_leggings = Armor("Legendary leggings", 
                        "Description", 
                        durability_armor[4], 
                        value_armor[4], 
                        "drop chance", 
                        rarity[4], 
                        armor_modifier[4], 
                        "Any", 
                        "Armor",
                        "Leggings")

mythic_leggings = Armor("Mythic leggings", 
                        "Description", 
                        durability_armor[5], 
                        value_armor[5], 
                        "drop chance", 
                        rarity[5], 
                        armor_modifier[5], 
                        "Any", 
                        "Armor",
                        "Leggings")

leggings_inventory = Shop_Category()
leggings_inventory.add_item(common_leggings)
leggings_inventory.add_item(uncommon_leggings)
leggings_inventory.add_item(rare_leggings)
leggings_inventory.add_item(epic_leggings)
leggings_inventory.add_item(legendary_leggings)
leggings_inventory.add_item(mythic_leggings)

# ARMOR BOOTS

common_boots = Armor("Common boots", 
                     "Description", 
                     durability_armor[0], 
                     value_armor[0], 
                     "drop chance", 
                     rarity[0], 
                     armor_modifier[0], 
                     "Any", 
                     "Armor",
                     "Boots")

uncommon_boots = Armor("Uncommon boots", 
                     "Description", 
                     durability_armor[1], 
                     value_armor[1], 
                     "drop chance", 
                     rarity[1], 
                     armor_modifier[1], 
                     "Any", 
                     "Armor",
                     "Boots")

rare_boots = Armor("Rare boots", 
                     "Description", 
                     durability_armor[2], 
                     value_armor[2], 
                     "drop chance", 
                     rarity[2], 
                     armor_modifier[2], 
                     "Any", 
                     "Armor",
                     "Boots")

epic_boots = Armor("Epic boots", 
                     "Description", 
                     durability_armor[3], 
                     value_armor[3], 
                     "drop chance", 
                     rarity[3], 
                     armor_modifier[3], 
                     "Any", 
                     "Armor",
                     "Boots")

legendary_boots = Armor("Legendary boots", 
                     "Description", 
                     durability_armor[4], 
                     value_armor[4], 
                     "drop chance", 
                     rarity[4], 
                     armor_modifier[4], 
                     "Any", 
                     "Armor",
                     "Boots")

mythic_boots = Armor("Mythic boots", 
                     "Description", 
                     durability_armor[5], 
                     value_armor[5], 
                     "drop chance", 
                     rarity[5], 
                     armor_modifier[5], 
                     "Any", 
                     "Armor",
                     "Boots")

boots_inventory = Shop_Category()
boots_inventory.add_item(common_boots)
boots_inventory.add_item(uncommon_boots)
boots_inventory.add_item(rare_boots)
boots_inventory.add_item(epic_boots)
boots_inventory.add_item(legendary_boots)
boots_inventory.add_item(mythic_boots)

# POTIONS (HEALTH/MANA)

common_health_potion = Potion("Basic potion", 
                              "Just a little potion", 
                              durability_potion, 
                              value_potions[0], 
                              40, 
                              10, 
                              0, 
                              rarity[0], 
                              "Health", 
                              "Potion",
                              None)
                              

uncommon_health_potion = Potion("Big potion", 
                              "Not just a little potion", 
                              1, 
                              20, 
                              30, 
                              25, 
                              0, 
                              rarity[1], 
                              "Health", 
                              "Potion",
                              None)

rare_health_potion = Potion("Really big potion", 
                              "Looks like a beer but it's not", 
                              1, 
                              50, 
                              20, 
                              50, 
                              0, 
                              rarity[2], 
                              "Health", 
                              "Potion",
                              None)

epic_health_potion = Potion("Huge potion", 
                              "Too much for a potion", 
                              1, 
                              75, 
                              10, 
                              75, 
                              0, 
                              rarity[3], 
                              "Health", 
                              "Potion",
                              None)

legendary_health_potion = Potion("Guargantuan potion", 
                              "This is stupidly big", 
                              1, 
                              100, 
                              5, 
                              100, 
                              0, 
                              rarity[4], 
                              "Health", 
                              "Potion",
                              None)

mythic_health_potion = Potion("DAAAAAMMMMMNNNN potion", 
                              "I can't even quantify this thing", 
                              durability_potion, 
                              value_potions[5], 
                              1, 
                              200, 
                              0, 
                              rarity[5], 
                              "Health", 
                              "Potion",
                              None)


health_pot_inventory = Shop_Category()
health_pot_inventory.add_item(common_health_potion)
health_pot_inventory.add_item(uncommon_health_potion)
health_pot_inventory.add_item(rare_health_potion)
health_pot_inventory.add_item(epic_health_potion)
health_pot_inventory.add_item(legendary_health_potion)
health_pot_inventory.add_item(mythic_health_potion)

common_mana_potion = Potion("Basic mana potion", 
                            "Same stuff but for mana", 
                            durability_potion, 
                            value_potions[0], 
                            40, 
                            0, 
                            10,
                            rarity[0], 
                            "Mana", 
                            "Potion",
                            None)

uncommon_mana_potion = Potion("Big mana potion", 
                            "You're using too much spells", 
                            1, 
                            20, 
                            30, 
                            0, 
                            25,
                            rarity[1], 
                            "Mana", 
                            "Potion",
                            None)

rare_mana_potion = Potion("Really big mana potion", 
                            "Do you eat mana ?", 
                            1, 
                            50, 
                            20, 
                            0, 
                            50,
                            rarity[2], 
                            "Mana", 
                            "Potion",
                            None)

epic_mana_potion = Potion("Huge mana potion", 
                            "You don't even have this amount of mana, why ?", 
                            1, 
                            75, 
                            10, 
                            0, 
                            75,
                            rarity[3], 
                            "Mana", 
                            "Potion",
                            None)

legendary_mana_potion = Potion("Guargantuan mana potion", 
                            "Are you stupid ?", 
                            1, 
                            100, 
                            5, 
                            1.5, 
                            100, 
                            rarity[4], 
                            "Mana", 
                            "Potion",
                            None)

mythic_mana_potion = Potion("DAAAAAMMMMMNNNN mana potion", 
                            "You're definitely insane", 
                            durability_potion, 
                            value_potions[5], 
                            1, 
                            0, 
                            200, 
                            rarity[5], 
                            "Mana", 
                            "Potion",
                            None)

mana_pot_inventory = Shop_Category()
mana_pot_inventory.add_item(common_mana_potion)
mana_pot_inventory.add_item(uncommon_mana_potion)
mana_pot_inventory.add_item(rare_mana_potion)
mana_pot_inventory.add_item(epic_mana_potion)
mana_pot_inventory.add_item(legendary_mana_potion)
mana_pot_inventory.add_item(mythic_mana_potion)

weapons = {
    rarity[0]: [common_sword, common_knife, common_hammer, common_stick],
    rarity[1]: [uncommon_sword, uncommon_knife, uncommon_hammer, uncommon_stick],
    rarity[2]: [rare_sword, rare_knife, rare_hammer, rare_stick],
    rarity[3]: [epic_sword, epic_knife, epic_hammer, epic_stick],
    rarity[4]: [legendary_sword, legendary_knife, legendary_hammer, legendary_stick],
    rarity[4]: [mythic_sword, mythic_knife, mythic_hammer, mythic_stick]
}

armor = {
    rarity[0]: [common_shield, common_helmet, common_chestplate, common_leggings, common_boots],
    rarity[1]: [uncommon_shield, uncommon_helmet, uncommon_chestplate, uncommon_leggings, uncommon_boots],
    rarity[2]: [rare_shield, rare_helmet, rare_chestplate, rare_leggings, rare_boots],
    rarity[3]: [epic_shield, epic_helmet, epic_chestplate, epic_leggings, epic_boots],
    rarity[4]: [legendary_shield, legendary_helmet, legendary_chestplate, legendary_leggings, legendary_boots],
    rarity[4]: [mythic_shield, mythic_helmet, mythic_chestplate, mythic_leggings, mythic_boots]
}

potions = {
    rarity[0]: [common_health_potion],
    rarity[1]: [uncommon_health_potion],
    rarity[2]: [rare_health_potion],
    rarity[3]: [epic_health_potion],
    rarity[4]: [legendary_health_potion],
    rarity[4]: [mythic_health_potion]
}
