COLORS = {
    "Common" : "white",
    "Uncommon" : "green4",
    "Rare" : "blue1",
    "Epic" : "purple",
    "Legendary" : "yellow1",
    "Mythic" :  "red1",
}

class Items:
    def __init__(self, name, description, durability, value, drop_chance, tier) -> None:
        self.name = name
        self.durability = durability
        self.description = description
        self.value = value
        self.drop_chance = drop_chance
        self.tier = tier
        self.color = COLORS[self.tier]

    def __str__(self):
        print(f"{self.name} : {self.description}   {self.durability} durability {self.value} golds")

class Weapons(Items):
    def __init__(self, name, description, durability, value, drop_chance, tier, attack_modifier,item_class, tools_type) -> None:
        super().__init__(name, description, durability, value, drop_chance, tier)
        self.attack_modifier = attack_modifier
        self.item_class = item_class
        self.type = tools_type


class Armor(Items):
    def __init__(self, name, description, durability, value, drop_chance, tier, armor_modifier, item_class, tools_type) -> None:
        super().__init__(name, description, durability, value, drop_chance, tier)
        self.armor_modifier = armor_modifier
        self.item_class = item_class
        self.type = tools_type


class Potion(Items):
    def __init__(self, name, description, durability, value, drop_chance, health_amount, mana_amount, tier, type_potion, tools_type) -> None:
        super().__init__(name, description, durability, value, drop_chance, tier)
        self.mana_amount = mana_amount
        self.health_amount = health_amount
        self.type_potion = type_potion
        self.type = tools_type

