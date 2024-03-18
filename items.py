class Items:
    def __init__(self, name, description, durability, value, drop_chance, tier) -> None:
        self.name = name
        self.durability = durability
        self.description = description
        self.value = value
        self.drop_chance = drop_chance
        self.tier = tier

    def __str__(self):
        print(f"{self.name} : {self.description}   {self.durability} durability {self.value} golds")


class Weapons(Items):
    def __init__(self, name, description, durability, value, drop_chance, tier, attack_modifier,item_class) -> None:
        super().__init__(name, description, durability, value, drop_chance, tier)
        self.attack_modifier = attack_modifier
        self.item_class = item_class


class Armor(Items):
    def __init__(self, name, description, durability, value, drop_chance, tier, armor_modifier,item_class) -> None:
        super().__init__(name, description, durability, value, drop_chance, tier)
        self.armor_modifier = armor_modifier
        self.item_class = item_class


class Potion(Items):
    def __init__(self, name, description, durability, value, drop_chance, health_amount, mana_amount, tier, type_potion) -> None:
        super().__init__(name, description, durability, value, drop_chance, tier)
        self.mana_amount = mana_amount
        self.health_amount = health_amount
        self.type_potion = type_potion

