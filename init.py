from character import *
from inventory import *
from items import *
from dice import Dice
from attack import Attack

'''############################################################   ATTACKS   #############################################################'''

damage = [5, 7]
crit_chance = [75, 55]
crit_multiplier = [1.5, 2.5]
miss_chance = [25, 40]

all_attacks = {"attack1": Attack("Normal attack", damage[0], crit_chance[0], crit_multiplier[0], miss_chance[0], "Just a normal sword strike", Dice(100)), 
               "attack2": Attack("Big attack", damage[1], crit_chance[1],crit_multiplier[1], miss_chance[1], "A big attack right on the head, 50/50 either you destroy the opponent or you just miss your attack", Dice(100))}


'''#############################################################   ITEMS   #############################################################'''

durability_weapons = [25, 50, 100, 200, 500, 666]
durability_armor = [25, 50, 100, 200, 500, 666]
durability_potion = 1
damage_modifier = [1, 1.1, 1.2, 1.3, .4, 1.5]
armor_modifier = [1, 1.1, 1.2, 1.3, 1.4, 1.5]
health_amount = [0, 2, 5, 10, 20, 50, 100]
mana_amount = [0, 2, 10, 20, 50, 100, 200]
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
                       drop_chance[0], 
                       rarity[0], 
                       damage_modifier[0], 
                       "Warrior", 
                       "Weapon",
                       "Sword")

uncommon_sword = Weapons("Simple sword", 
                         "Just a piece of forged iron", 
                         durability_weapons[1], 
                         value_weapons[1], 
                         drop_chance[1], 
                         rarity[1], 
                         damage_modifier[1], 
                         "Warrior", 
                         "Weapon",
                         "Sword")

rare_sword = Weapons("Knight sword", 
                     "Finally a good weapon", 
                     durability_weapons[2], 
                     value_weapons[2], 
                     drop_chance[2], 
                     rarity[2], 
                     damage_modifier[2], 
                     "Warrior", 
                     "Weapon",
                     "Sword")

epic_sword = Weapons("Claymore", 
                     "Big sword for big damage !", 
                     durability_weapons[3], 
                     value_weapons[3], 
                     drop_chance[3], 
                     rarity[3], 
                     damage_modifier[3], 
                     "Warrior", 
                     "Weapon",
                     "Sword")

legendary_sword = Weapons("Excalibur", 
                          "More than just a sword ", 
                          durability_weapons[4], 
                          value_weapons[4], 
                          drop_chance[4], 
                          rarity[4], 
                          damage_modifier[4], 
                          "Warrior", 
                          "Weapon",
                          "Sword")

mythic_sword = Weapons("Big Sword of DOOM !", 
                       "This sword came from hell, forged buy an ancient demon, anyway... BIIIGGG damage", 
                       durability_weapons[5], 
                       value_weapons[5], 
                       drop_chance[5], 
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
                       drop_chance[0], 
                       rarity[0], 
                       damage_modifier[0], 
                       "Thief", 
                       "Weapon",
                       "Knife")

uncommon_knife = Weapons("Kitchen knife", 
                         "Better than the opinel, it's perfect for big meat", 
                         durability_weapons[1], 
                         value_weapons[1], 
                         drop_chance[1], 
                         rarity[1], 
                         damage_modifier[1], 
                         "Thief", 
                         "Weapon",
                         "Knife")

rare_knife = Weapons("Butcher knife", 
                     "Really big one", 
                     durability_weapons[2], 
                     value_weapons[2], 
                     drop_chance[2], 
                     rarity[2], 
                     damage_modifier[2], 
                     "Thief", 
                     "Weapon",
                     "Knife")

epic_knife = Weapons("Hunting knife", 
                     "This knife is use for any kind of animals or living thing", 
                     durability_weapons[3], 
                     value_weapons[3], 
                     drop_chance[3], 
                     rarity[3], 
                     damage_modifier[3], 
                     "Thief", 
                     "Weapon",
                     "Knife")

legendary_knife = Weapons("Buttlefly knife Fade FN Statrack", 
                          "100% Fade this is worth a few minimal wages", 
                          durability_weapons[4], 
                          value_weapons[4], 
                          drop_chance[4], 
                          rarity[4], 
                          damage_modifier[4], 
                          "Thief", 
                          "Weapon",
                          "Knife")

mythic_knife = Weapons("Big Knife of DOOM", 
                       "Exactly the same as the sword but it's a knife", 
                       durability_weapons[5], 
                       value_weapons[5], 
                       drop_chance[5], 
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
                        drop_chance[0], 
                        rarity[0], 
                        damage_modifier[0], 
                        "Colossus", 
                        "Weapon",
                        "Hammer")

uncommon_hammer = Weapons("DIY Hammer", 
                          "It's meant for nails but it works on zombies too", 
                          durability_weapons[1], 
                          value_weapons[1], 
                          drop_chance[1], 
                          rarity[1], 
                          damage_modifier[1], 
                          "Colossus", 
                          "Weapon",
                          "Hammer")

rare_hammer = Weapons("Torbjörn's hammer", 
                      "You want to repair your turret , right ?", 
                      durability_weapons[2], 
                      value_weapons[2], 
                      drop_chance[2], 
                      rarity[2], 
                      damage_modifier[2], 
                      "Colossus", 
                      "Weapon",
                      "Hammer")

epic_hammer = Weapons("War hammer 40000", 
                      "Not the game bro", 
                      durability_weapons[3], 
                      value_weapons[3], 
                      drop_chance[3], 
                      rarity[3], 
                      damage_modifier[3], 
                      "Colossus", 
                      "Weapon",
                      "Hammer")

legendary_hammer = Weapons("Mjöllnir", 
                           "Be carefull, Thor is chasing you. Stealing is bad", 
                           durability_weapons[4], 
                           value_weapons[4], 
                           drop_chance[4], 
                           rarity[4], 
                           damage_modifier[4], 
                           "Colossus", 
                           "Weapon",
                           "Hammer")

mythic_hammer = Weapons("Big Hammer of DOOM !", 
                        "You know the Burj Khalifa ? This hammer if BIGGER", 
                        durability_weapons[5], 
                        value_weapons[5], 
                        drop_chance[5], 
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
                       drop_chance[0], 
                       rarity[0], 
                       damage_modifier[0], 
                       "Mage", 
                       "Weapon",
                       "Stick")

uncommon_stick = Weapons("Branch", 
                         "A piece of wood", 
                         durability_weapons[1], 
                         value_weapons[1], 
                         drop_chance[1], 
                         rarity[1], 
                         damage_modifier[1], 
                         "Mage", 
                         "Weapon",
                         "Stick")

rare_stick = Weapons("Makeup stick", 
                     "You have to be well made-up to be a mage", 
                     durability_weapons[2], 
                     value_weapons[2], 
                     drop_chance[2], 
                     rarity[2], 
                     damage_modifier[2], 
                     "Mage", 
                     "Weapon",
                     "Stick")

epic_stick = Weapons("The Baguette", 
                     "Oui oui baguette", 
                     durability_weapons[3], 
                      value_weapons[3], 
                     drop_chance[3], 
                     rarity[3], 
                     damage_modifier[3], 
                     "Mage", 
                     "Weapon",
                     "Stick")

legendary_stick = Weapons("Elderberry wand", 
                          "You're a wizard Harry", 
                          durability_weapons[4], 
                          value_weapons[4], 
                          drop_chance[4], 
                          rarity[4], 
                          damage_modifier[4], 
                          "Mage", 
                          "Weapon",
                          "Stick")

mythic_stick = Weapons("Big Stick of DOOM !", 
                       "It's still a piece of shit", 
                       durability_weapons[5], 
                       value_weapons[5], 
                       drop_chance[5], 
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
                      drop_chance[0], 
                      rarity[0], 
                      armor_modifier[0], 
                      "Any", 
                      "Armor",
                      "Shield")

uncommon_shield = Armor("Shiebre", 
                      "Some french shit", 
                      durability_armor[1], 
                      value_armor[1], 
                      drop_chance[1], 
                      rarity[1], 
                      armor_modifier[1], 
                      "Any", 
                      "Armor",
                      "Shield")

rare_shield = Armor("Medieval shield", 
                      "Back to XV", 
                      durability_armor[2], 
                      value_armor[2], 
                      drop_chance[2], 
                      rarity[2], 
                      armor_modifier[2], 
                      "Any", 
                      "Armor",
                      "Shield")

epic_shield = Armor("Reinhardt's shield", 
                      "It's pretty big , no ?", 
                      durability_armor[3], 
                      value_armor[3], 
                      drop_chance[3], 
                      rarity[3], 
                      armor_modifier[3], 
                      "Any", 
                      "Armor",
                      "Shield")

legendary_shield = Armor("Vibranium shield", 
                      "What did you do to captain america ?", 
                      durability_armor[4], 
                      value_armor[4], 
                      drop_chance[4], 
                      rarity[4], 
                      armor_modifier[4], 
                      "Any", 
                      "Armor",
                      "Shield")

mythic_shield = Armor("Big shield of DOOM !", 
                      "What are you doing with this in your hands ?", 
                      durability_armor[5], 
                      value_armor[5], 
                      drop_chance[5], 
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

common_helmet = Armor("Leather helmet", 
                      "You killed some cows , well done !", 
                      durability_armor[0], 
                      value_armor[0], 
                      drop_chance[0], 
                      rarity[0], 
                      armor_modifier[0], 
                      "Any", 
                      "Armor",
                      "Shield")

uncommon_helmet = Armor("Bike helmet", 
                      "you are too old for this ...", 
                      durability_armor[1], 
                      value_armor[1], 
                      drop_chance[1], 
                      rarity[1], 
                      armor_modifier[1], 
                      "Any", 
                      "Armor",
                      "Helmet")

rare_helmet = Armor("Arai helmet", 
                      "You just want to cruise on your T-max", 
                      durability_armor[2], 
                      value_armor[2], 
                      drop_chance[2], 
                      rarity[2], 
                      armor_modifier[2], 
                      "Any", 
                      "Armor",
                      "Helmet")

epic_helmet = Armor("Beats studio pro helmet", 
                      "Ok Dr.Dre", 
                      durability_armor[3], 
                      value_armor[3], 
                      drop_chance[3], 
                      rarity[3], 
                      armor_modifier[3], 
                      "Any", 
                      "Armor",
                      "Helmet")

legendary_helmet = Armor("Diamond Helmet", 
                      "Cover me in diamonds", 
                      durability_armor[4], 
                      value_armor[4], 
                      drop_chance[4], 
                      rarity[4], 
                      armor_modifier[4], 
                      "Any", 
                      "Armor",
                      "Helmet")

mythic_helmet = Armor("Magneto's helmet", 
                      "Good style bro", 
                      durability_armor[5], 
                      value_armor[5], 
                      drop_chance[5], 
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

common_chestplate = Armor("Holey shirt", 
                          "did you find it in the trash can ?", 
                          durability_armor[0], 
                          value_armor[0], 
                          drop_chance[0], 
                          rarity[0], 
                          armor_modifier[0], 
                          "Any", 
                          "Armor",
                          "Chestplate")

uncommon_chestplate = Armor("Barbarian chestplate", 
                          "This one significantly reduces your IQ", 
                          durability_armor[1], 
                          value_armor[1], 
                          drop_chance[1], 
                          rarity[1], 
                          armor_modifier[1], 
                          "Any", 
                          "Armor",
                          "Chestplate")

rare_chestplate = Armor("Gragas's belly", 
                          "Too much beer for you", 
                          durability_armor[2], 
                          value_armor[2], 
                          drop_chance[2], 
                          rarity[2], 
                          armor_modifier[2], 
                          "Any", 
                          "Armor",
                          "Chestplate")

epic_chestplate = Armor("Daedric chestplate", 
                          "Fus Ro Dah", 
                          durability_armor[3], 
                          value_armor[3], 
                          drop_chance[3], 
                          rarity[3], 
                          armor_modifier[3], 
                          "Any", 
                          "Armor",
                          "Chestplate")

legendary_chestplate = Armor("Diamond chestplate", 
                          "Cover me in diamonds", 
                          durability_armor[4], 
                          value_armor[4], 
                          drop_chance[4], 
                          rarity[4], 
                          armor_modifier[4], 
                          "Any", 
                          "Armor",
                          "Chestplate")

mythic_chestplate = Armor("Gucci coat", 
                          "3k$ for that , really ?", 
                          durability_armor[5], 
                          value_armor[5], 
                          drop_chance[5], 
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

common_leggings = Armor("Leather leggings", 
                        "You killed some cow, well done !", 
                        durability_armor[0], 
                        value_armor[0], 
                        drop_chance[0], 
                        rarity[0], 
                        armor_modifier[0], 
                        "Any", 
                        "Armor",
                        "Leggings")

uncommon_leggings = Armor("Levis Jeans", 
                        "Really durable trousers", 
                        durability_armor[1], 
                        value_armor[1], 
                        drop_chance[1], 
                        rarity[1], 
                        armor_modifier[1], 
                        "Any", 
                        "Armor",
                        "Leggings")

rare_leggings = Armor("Dagobert's Breeche", 
                      "Be careful to put it right side up", 
                      durability_armor[2], 
                      value_armor[2], 
                      drop_chance[2], 
                      rarity[2], 
                      armor_modifier[2], 
                      "Any", 
                      "Armor",
                      "Leggings")

epic_leggings = Armor("Sirwal Pants", 
                      "You really don't have good taste", 
                      durability_armor[3], 
                      value_armor[3], 
                      drop_chance[3], 
                      rarity[3], 
                      armor_modifier[3], 
                      "Any", 
                      "Armor",
                      "Leggings")

legendary_leggings = Armor("Diamond leggings", 
                            "Cover me with diamond", 
                            durability_armor[4], 
                            value_armor[4], 
                            drop_chance[4], 
                            rarity[4], 
                            armor_modifier[4], 
                            "Any", 
                            "Armor",
                            "Leggings")

mythic_leggings = Armor("Jean overalls", 
                        "The ultimate construction site armor", 
                        durability_armor[5], 
                        value_armor[5], 
                        drop_chance[5], 
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

common_boots = Armor("Leather boots", 
                     "You killed some cow, well done !", 
                     durability_armor[0], 
                     value_armor[0], 
                     drop_chance[0], 
                     rarity[0], 
                     armor_modifier[0], 
                     "Any", 
                     "Armor",
                     "Boots")

uncommon_boots = Armor("Seven league boots", 
                     "So much distance in a few seconds", 
                     durability_armor[1], 
                     value_armor[1], 
                     drop_chance[1], 
                     rarity[1], 
                     armor_modifier[1], 
                     "Any", 
                     "Armor",
                     "Boots")

rare_boots = Armor("Cinderella glass slipper", 
                     "You must go home before midnight", 
                     durability_armor[2], 
                     value_armor[2], 
                     drop_chance[2], 
                     rarity[2], 
                     armor_modifier[2], 
                     "Any", 
                     "Armor",
                     "Boots")

epic_boots = Armor("Dr Martens boots", 
                   "Big boots for big métal concerts", 
                   durability_armor[3], 
                   value_armor[3], 
                   drop_chance[3], 
                   rarity[3], 
                   armor_modifier[3], 
                   "Any", 
                   "Armor",
                   "Boots")

legendary_boots = Armor("Diamond boots", 
                        "Cover me with diamond", 
                        durability_armor[4], 
                        value_armor[4], 
                        drop_chance[4], 
                        rarity[4], 
                        armor_modifier[4], 
                        "Any", 
                        "Armor",
                        "Boots")

mythic_boots = Armor("CR7's shoes", 
                     "Can you believe it ?", 
                     durability_armor[5], 
                     value_armor[5], 
                     drop_chance[5], 
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
                              drop_chance[0], 
                              health_amount[1], 
                              mana_amount[0], 
                              rarity[0], 
                              "Health", 
                              "Potion",
                              None)

uncommon_health_potion = Potion("Big potion", 
                                "Not just a little potion", 
                                durability_potion, 
                                value_potions[1], 
                                drop_chance[1], 
                                health_amount[2], 
                                mana_amount[0], 
                                rarity[1], 
                                "Health", 
                                "Potion",
                                None)

rare_health_potion = Potion("Really big potion", 
                            "Looks like a beer but it's not", 
                            durability_potion, 
                            value_potions[2], 
                            drop_chance[2], 
                            health_amount[3], 
                            mana_amount[0], 
                            rarity[2], 
                            "Health", 
                            "Potion",
                            None)

epic_health_potion = Potion("Huge potion", 
                            "Too much for a potion", 
                            durability_potion, 
                            value_potions[3], 
                            drop_chance[3], 
                            health_amount[4], 
                            mana_amount[0], 
                            rarity[3], 
                            "Health", 
                            "Potion",
                            None)

legendary_health_potion = Potion("Guargantuan potion", 
                                 "This is stupidly big", 
                                 durability_potion, 
                                 value_potions[4], 
                                 drop_chance[4], 
                                 health_amount[5], 
                                 mana_amount[0], 
                                 rarity[4], 
                                 "Health", 
                                 "Potion",
                                 None)

mythic_health_potion = Potion("DAAAAAMMMMMNNNN potion", 
                              "I can't even quantify this thing", 
                              durability_potion, 
                              value_potions[5], 
                              drop_chance[5], 
                              health_amount[6], 
                              mana_amount[0], 
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
                            drop_chance[0], 
                            health_amount[0], 
                            mana_amount[1],
                            rarity[0], 
                            "Mana", 
                            "Potion",
                            None)

uncommon_mana_potion = Potion("Big mana potion", 
                              "You're using too much spells", 
                              durability_potion, 
                              value_potions[1], 
                              drop_chance[1], 
                              health_amount[0], 
                              mana_amount[2],
                              rarity[1], 
                              "Mana", 
                              "Potion",
                              None)

rare_mana_potion = Potion("Really big mana potion", 
                          "Do you eat mana ?", 
                          durability_potion, 
                          value_potions[2], 
                          drop_chance[2], 
                          health_amount[0], 
                          mana_amount[3],
                          rarity[2], 
                          "Mana", 
                          "Potion",
                          None)
  
epic_mana_potion = Potion("Huge mana potion", 
                          "You don't even have this amount of mana, why ?", 
                          durability_potion, 
                          value_potions[3], 
                          drop_chance[3], 
                          health_amount[0], 
                          mana_amount[4],
                          rarity[3], 
                          "Mana", 
                          "Potion",
                          None)

legendary_mana_potion = Potion("Guargantuan mana potion", 
                            "Are you stupid ?", 
                            durability_potion, 
                            value_potions[4], 
                            drop_chance[4], 
                            health_amount[0], 
                            mana_amount[5], 
                            rarity[4], 
                            "Mana", 
                            "Potion",
                            None)

mythic_mana_potion = Potion("DAAAAAMMMMMNNNN mana potion", 
                            "You're definitely insane", 
                            durability_potion, 
                            value_potions[5], 
                            drop_chance[5], 
                            health_amount[0], 
                            mana_amount[6], 
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
